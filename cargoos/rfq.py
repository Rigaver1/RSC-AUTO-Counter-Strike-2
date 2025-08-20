from pathlib import Path
from typing import Dict
from .models import SupplierItem

TEMPLATES: Dict[str, str] = {
    'ru': (
        'Здравствуйте!\n'
        'Интересуемся товаром {title} ({url}). Минимальная партия {moq} шт.\n'
        'Просим сообщить цену EXW и сроки производства.\n'
        'С уважением,\n'
    ),
    'en': (
        'Hello,\n'
        'We are interested in product {title} ({url}). MOQ {moq} pcs.\n'
        'Please quote EXW price and lead time.\n'
        'Best regards,\n'
    ),
    'cn': (
        '您好!\n'
        '我们对产品 {title} ({url}) 感兴趣, MOQ {moq}.\n'
        '请告知EXW价格和生产周期。\n'
        '谢谢!\n'
    ),
}


def generate_rfq(item: SupplierItem, lang: str, path: Path) -> Dict[str, str]:
    if lang not in TEMPLATES:
        raise ValueError('unsupported language')
    body = TEMPLATES[lang].format(title=item.title, url=item.url, moq=item.moq or '')
    path.write_text(body, encoding='utf-8')
    preview = '\n'.join(body.splitlines()[:3])
    return {'path': str(path), 'preview': preview}
