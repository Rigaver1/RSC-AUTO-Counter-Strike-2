import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Tuple, Optional
from urllib.request import urlopen

CACHE_FILE = Path(__file__).with_name('fx_cache.json')
CACHE_TTL = timedelta(hours=1)


def _load_cache() -> Tuple[Optional[float], Optional[datetime]]:
    if not CACHE_FILE.exists():
        return None, None
    data = json.loads(CACHE_FILE.read_text())
    return data.get('rate'), datetime.fromisoformat(data.get('ts'))


def _save_cache(rate: float):
    CACHE_FILE.write_text(json.dumps({'rate': rate, 'ts': datetime.utcnow().isoformat()}))


def get_cny_rate(source: str = 'cbr', manual_rate: float = None) -> float:
    if source == 'manual':
        if manual_rate is None:
            raise ValueError('manual_rate required when fx_source=manual')
        return manual_rate
    rate, ts = _load_cache()
    if rate and ts and datetime.utcnow() - ts < CACHE_TTL:
        return rate
    with urlopen('https://www.cbr.ru/scripts/XML_daily.asp', timeout=10) as resp:
        text = resp.read().decode('windows-1251')
    start = text.find('<CharCode>CNY</CharCode>')
    if start == -1:
        raise RuntimeError('CNY rate not found')
    value_start = text.find('<Value>', start) + len('<Value>')
    value_end = text.find('</Value>', value_start)
    value = text[value_start:value_end].replace(',', '.')
    rate = float(value)
    _save_cache(rate)
    return rate
