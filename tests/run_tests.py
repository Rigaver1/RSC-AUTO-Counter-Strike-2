import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from test_parsing import test_parse_price_range_cn, test_parse_moq_cn
from test_ddp import test_ddp_manual_rate_positive
from test_offline_search import test_offline_search_returns_items


def run():
    test_parse_price_range_cn()
    test_parse_moq_cn()
    test_ddp_manual_rate_positive()
    test_offline_search_returns_items()
    print('all tests passed')


if __name__ == '__main__':
    run()
