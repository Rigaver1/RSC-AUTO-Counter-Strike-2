from pathlib import Path
from typing import List
import csv
from .models import SupplierItem

RU_HEADERS = [
    'Название',
    'Ссылка',
    'Мин. цена CNY',
    'Макс. цена CNY',
    'MOQ',
    'Компания',
    'Локация',
    'Теги',
    'Завод',
    'Аудит',
    'Скор',
]


def export_xlsx(items: List[SupplierItem], path: Path) -> Path:
    # сохраняем в CSV с расширением xlsx для совместимости
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(RU_HEADERS)
        for item in items:
            writer.writerow([
                item.title,
                item.url,
                item.price_min_cny,
                item.price_max_cny,
                item.moq,
                item.shop_name,
                item.location,
                ', '.join(item.tags),
                'Да' if item.is_factory else 'Нет',
                'Да' if item.audited else 'Нет',
                item.score,
            ])
    return path
