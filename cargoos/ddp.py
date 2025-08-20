from datetime import datetime
from .models import DDPInput
from .fx import get_cny_rate


def calc_ddp(inp: DDPInput) -> dict:
    rate = get_cny_rate(inp.fx_source, inp.fx_cny_rub)
    goods_cny = inp.exw_or_fob_cny * inp.qty
    goods_rub = goods_cny * rate
    freight_rub = inp.freight_total_rub + inp.freight_total_cny * rate
    inland_rub = inp.inland_ru_rub + inp.inland_cn_cny * rate
    insurance_rub = goods_rub * (inp.insurance_pct / 100)
    duty_rub = goods_rub * (inp.duty_rate_pct / 100)
    vat_rub = (goods_rub + duty_rub + freight_rub) * (inp.vat_rate_pct / 100)
    total_rub = goods_rub + freight_rub + inland_rub + insurance_rub + duty_rub + vat_rub
    per_unit_rub = total_rub / inp.qty
    return {
        'fx_used': {'cny_rub': rate},
        'goods': goods_rub,
        'freight_rub': freight_rub,
        'inland_rub': inland_rub,
        'insurance_rub': insurance_rub,
        'duty_rub': duty_rub,
        'vat_rub': vat_rub,
        'total_rub': total_rub,
        'per_unit_rub': per_unit_rub,
        'mode': inp.mode,
        'ts': datetime.utcnow().isoformat(),
    }
