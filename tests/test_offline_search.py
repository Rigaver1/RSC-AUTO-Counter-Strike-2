from cargoos.models import SearchParams
from cargoos.search import search_1688


def test_offline_search_returns_items():
    params = SearchParams(q='测试', offline=True, only_factories=False, audited_only=False, min_years=0)
    items = search_1688(params)
    assert len(items) >= 2
    assert items[0].score >= items[1].score
