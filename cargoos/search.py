from __future__ import annotations
from typing import List
from pathlib import Path
from urllib.request import urlopen, Request
from xml.etree import ElementTree as ET
from .models import SearchParams, SupplierItem
from .parsing import parse_price_range_cn, parse_moq_cn
from .scoring import score_supplier

OFFLINE_HTML = Path(__file__).with_name('data').joinpath('offline_demo.html')


def _parse_html(html: str) -> List[SupplierItem]:
    root = ET.fromstring(html)
    items: List[SupplierItem] = []
    for div in root.findall('.//div'):
        if div.get('class') != 'item':
            continue
        def find_text(tag):
            el = div.find(f".//{tag}")
            return el.text.strip() if el is not None and el.text else ''
        title_el = div.find(".//a[@class='title']")
        price_text = find_text('span[@class="price"]') or find_text('span')
        moq_text = find_text('span[@class="moq"]')
        years_text = find_text('span[@class="years"]')
        price_min, price_max = parse_price_range_cn(price_text)
        moq = parse_moq_cn(moq_text)
        years = parse_moq_cn(years_text.replace('年', '') if years_text else '')
        item = SupplierItem(
            title=title_el.text.strip() if title_el is not None and title_el.text else '',
            url=title_el.get('href') if title_el is not None else '',
            image_urls=[div.find('.//img').get('src')] if div.find('.//img') is not None else [],
            price_min_cny=price_min,
            price_max_cny=price_max,
            moq=moq,
            shop_name=find_text('span[@class="shop"]') or None,
            location=find_text('span[@class="location"]') or None,
            tags=[t.strip() for t in find_text('span[@class="tags"]').split(',') if t.strip()],
            years_active=years,
        )
        score_supplier(item)
        items.append(item)
    return items


def search_1688(params: SearchParams) -> List[SupplierItem]:
    html = None
    if not params.offline:
        try:
            req = Request('https://s.1688.com/selloffer/offer_search.htm?keywords=' + params.q)
            with urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
        except Exception:
            html = None
    if html is None:
        html = OFFLINE_HTML.read_text(encoding='utf-8')
    items = _parse_html(html)
    res = []
    for item in items:
        if params.only_factories and not item.is_factory:
            continue
        if params.audited_only and not item.audited:
            continue
        if params.moq_max is not None and item.moq and item.moq > params.moq_max:
            continue
        if params.price_min_cny and (item.price_min_cny is None or item.price_min_cny < params.price_min_cny):
            continue
        if params.price_max_cny and (item.price_max_cny is None or item.price_max_cny > params.price_max_cny):
            continue
        if item.years_active is not None and item.years_active < params.min_years:
            continue
        res.append(item)
    res.sort(key=lambda x: (-x.score, x.price_min_cny or 0))
    return res
