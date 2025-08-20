from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class SupplierItem:
    title: str
    url: str
    image_urls: List[str] = field(default_factory=list)
    price_min_cny: Optional[float] = None
    price_max_cny: Optional[float] = None
    moq: Optional[int] = None
    shop_name: Optional[str] = None
    location: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    is_factory: bool = False
    is_factory_confidence: float = 0.0
    audited: bool = False
    certifications: List[str] = field(default_factory=list)
    evidence: List[str] = field(default_factory=list)
    years_active: Optional[int] = None
    contacts: Optional[str] = None
    pack: Optional[str] = None
    score: float = 0.0
    captured_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class SearchParams:
    q: str
    mode: str = "fast"
    pages: int = 1
    only_factories: bool = True
    audited_only: bool = True
    min_years: int = 0
    moq_max: Optional[int] = None
    price_min_cny: Optional[float] = None
    price_max_cny: Optional[float] = None
    offline: bool = False


@dataclass
class DDPInput:
    exw_or_fob_cny: float
    qty: int
    cbm_total: Optional[float] = None
    gw_total: Optional[float] = None
    duty_rate_pct: float = 0.0
    vat_rate_pct: float = 20.0
    freight_total_cny: float = 0.0
    freight_total_rub: float = 0.0
    inland_cn_cny: float = 0.0
    inland_ru_rub: float = 0.0
    insurance_pct: float = 0.0
    mode: str = "sea_lcl"
    fx_source: str = "cbr"
    fx_cny_rub: Optional[float] = None
