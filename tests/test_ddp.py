from cargoos.models import DDPInput
from cargoos.ddp import calc_ddp


def test_ddp_manual_rate_positive():
    inp = DDPInput(
        exw_or_fob_cny=10,
        qty=100,
        duty_rate_pct=5,
        vat_rate_pct=20,
        freight_total_cny=100,
        inland_cn_cny=20,
        inland_ru_rub=1000,
        insurance_pct=1,
        fx_source='manual',
        fx_cny_rub=12,
    )
    result = calc_ddp(inp)
    assert result['per_unit_rub'] > 0
    assert result['fx_used']['cny_rub'] == 12
