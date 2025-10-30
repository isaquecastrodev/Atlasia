# modules/report_module.py
"""Módulo de exemplo que gera um relatório CSV simples com dados fictícios."""
import os, csv
from datetime import datetime
from core.logger import get_logger

logger = get_logger(__name__)

OUT_DIR = os.path.join(os.getcwd(), 'data', 'reports')
os.makedirs(OUT_DIR, exist_ok=True)

def run(params: dict):
    rng = params.get('range', 'today')
    filename = os.path.join(OUT_DIR, f"report_{rng}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    rows = [
        ['id', 'name', 'value'],
        [1, 'Alice', 123],
        [2, 'Bob', 456],
    ]
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for r in rows:
            writer.writerow(r)
    logger.info(f"Relatório gerado: {filename}")
    return {'status': 'ok', 'file': filename}
