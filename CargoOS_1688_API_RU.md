# CargoOS 1688 — Ядро (RU)

Простое ядро API для работы с поставщиками 1688.

## GET /health
Проверка работоспособности сервиса. Возвращает `{ "ok": true }`.

## GET /search_1688
Онлайн или офлайн поиск поставщиков. Параметры (`SearchParams`):
- `q` — строка запроса на китайском.
- `mode` — `fast` или `precise`.
- `pages` — число страниц (не используется в офлайн демо).
- `only_factories` — показывать только «заводы» (по умолчанию `true`).
- `audited_only` — только с метками аудита (по умолчанию `true`).
- `min_years` — минимальный стаж.
- `moq_max` — максимальный MOQ.
- `offline` — использовать встроенный офлайн снимок.

Возвращает список `SupplierItem`:
- `title` — название товара.
- `url` — ссылка на карточку 1688.
- `image_urls` — изображения.
- `price_min_cny`, `price_max_cny` — диапазон цены.
- `moq` — MOQ.
- `shop_name` — компания.
- `location` — регион.
- `tags` — теги 1688.
- `is_factory` — флаг «завод».
- `is_factory_confidence` — уверенность (0..1).
- `audited` — наличие аудита.
- `score` — итоговый балл.

## POST /export/xlsx
Принимает список `SupplierItem`, сохраняет файл `suppliers.xlsx` и возвращает путь.

## POST /rfq
Генерация письма-запроса (RFQ). Параметры: объект `SupplierItem` и `lang` (`ru`/`en`/`cn`). Возвращает путь к созданному файлу и превью.

## POST /calc/ddp
Расчёт стоимости DDP. Параметры (`DDPInput`):
- `exw_or_fob_cny` — цена EXW/FOB в CNY.
- `qty` — количество.
- `duty_rate_pct` — ставка пошлины, %.
- `vat_rate_pct` — ставка НДС, %.
- `freight_total_cny`, `freight_total_rub` — фрахт.
- `inland_cn_cny`, `inland_ru_rub` — внутренняя логистика.
- `insurance_pct` — страховка, %.
- `mode` — режим доставки.
- `fx_source` — источник курса (`cbr` или `manual`).
- `fx_cny_rub` — курс для `manual`.

Возвращает раскладку статей и `per_unit_rub` — цену за единицу в рублях.
