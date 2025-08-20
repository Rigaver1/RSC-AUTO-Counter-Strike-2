import re
from typing import Optional, Tuple


PRICE_RE = re.compile(r"[￥\s]*(\d+[.,]?\d*)(?:\s*-\s*(\d+[.,]?\d*))?")
MOQ_RE = re.compile(r"(\d+)")


def parse_price_range_cn(text: str) -> Tuple[Optional[float], Optional[float]]:
    if not text:
        return None, None
    if "面议" in text:
        return None, None
    m = PRICE_RE.search(text)
    if not m:
        return None, None
    price_min = float(m.group(1).replace(",", "."))
    price_max = m.group(2)
    if price_max:
        price_max = float(price_max.replace(",", "."))
    return price_min, price_max


def parse_moq_cn(text: str) -> Optional[int]:
    if not text:
        return None
    m = MOQ_RE.search(text)
    if not m:
        return None
    return int(m.group(1))
