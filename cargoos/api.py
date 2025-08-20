from pathlib import Path
from typing import List
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .models import SearchParams, SupplierItem, DDPInput
from .search import search_1688
from .export import export_xlsx
from .rfq import generate_rfq
from .ddp import calc_ddp

app = FastAPI(title="CargoOS 1688 — Ядро (RU)")


@app.get('/health')
def health():
    return {'ok': True}


@app.get('/search_1688', response_model=List[SupplierItem])
def api_search(params: SearchParams):
    return search_1688(params)


@app.post('/export/xlsx')
def api_export(items: List[SupplierItem]):
    path = export_xlsx(items, Path('suppliers.xlsx'))
    return {'path': str(path)}


@app.post('/rfq')
def api_rfq(item: SupplierItem, lang: str = 'ru'):
    info = generate_rfq(item, lang, Path(f'rfq_{lang}.txt'))
    return info


@app.post('/calc/ddp')
def api_ddp(inp: DDPInput):
    return calc_ddp(inp)
