from typing import List
from .models import SupplierItem

RULES = {
    'threshold': 1,
    'positive': ['源头工厂', '工厂直供', '生产加工', '自有工厂', '实地认证', '实力商家', '可定制', '支持OEM/ODM'],
    'negative': ['贸易', '批发', '代理'],
}


def score_supplier(item: SupplierItem) -> SupplierItem:
    text = ' '.join(item.tags)
    pos_hits: List[str] = [m for m in RULES['positive'] if m in text]
    neg_hits: List[str] = [m for m in RULES['negative'] if m in text]
    score_val = len(pos_hits) - len(neg_hits)
    threshold = RULES.get('threshold', 1)
    item.is_factory = score_val >= threshold
    item.is_factory_confidence = max(0.0, min(1.0, score_val / max(len(RULES['positive']), 1)))
    item.audited = any(tag in item.tags for tag in ['实地认证', '实力商家'])
    item.evidence = pos_hits + neg_hits
    base_score = score_val * 10
    if item.audited:
        base_score += 20
    item.score = base_score
    return item
