# tests/test_caracteristicas.py
# Teste unitário de apoio: confere a separação das características a partir de
# títulos reais do KaBuM, sem abrir o navegador.
import pytest
from utils.caracteristicas import separar


@pytest.mark.parametrize("titulo, esperado", [
    ("Memória RAM Kingston Fury Beast, 8GB, 3200MHz, DDR4, CL16, Preto - KF432C16BB/8",
     {"marca": "Kingston", "capacidade": "8", "frequencia": "3200", "tipo": "DDR4", "notebook": False}),
    ("Memoria 8GB Kingston Ddr4 3200mhz Kvr32n22s8/8",
     {"marca": "Kingston", "capacidade": "8", "frequencia": "3200", "tipo": "DDR4", "notebook": False}),
    ("Memória RAM Corsair Vengeance, 32GB (2x16GB), 6000MHz, DDR5, CL38, Intel XMP, Preto - CMK32GX5M2B6000C38",
     {"marca": "Corsair", "capacidade": "32", "frequencia": "6000", "tipo": "DDR5", "notebook": False}),
    ("Memória RAM Para Notebook Kingston, 8GB, 1600MHz, DDR3L - KVR16LS11/8",
     {"marca": "Kingston", "capacidade": "8", "frequencia": "1600", "tipo": "DDR3L", "notebook": True}),
    ("Memoria RAM Kingston Fury Beast, 16GB, 3200MT/s, DDR4, CL16, DIMM, Preto - KF432C16BB/16",
     {"marca": "Kingston", "capacidade": "16", "frequencia": "3200", "tipo": "DDR4", "notebook": False}),
])
def test_separar_titulo(titulo, esperado):
    assert separar(titulo) == esperado
