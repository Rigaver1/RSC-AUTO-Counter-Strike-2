from cargoos.parsing import parse_price_range_cn, parse_moq_cn


def test_parse_price_range_cn():
    assert parse_price_range_cn("￥1.20-2.10") == (1.20, 2.10)
    assert parse_price_range_cn("1.28 起") == (1.28, None)
    assert parse_price_range_cn("价格面议") == (None, None)


def test_parse_moq_cn():
    assert parse_moq_cn("起订量 500 个") == 500
    assert parse_moq_cn("MOQ 1000") == 1000
    assert parse_moq_cn("不限") is None
