# conftest.py
# Configuração compartilhada por todos os testes (o pytest carrega este arquivo sozinho).
# - Fixture `driver`: abre o Chrome antes de cada teste e fecha ao final,
#   mesmo quando o teste falha (item 7 do enunciado).
# - Hook de evidência: ao fim de cada teste tira um print e salva em
#   evidencias/CT-XXX_APROVADO.png ou evidencias/CT-XXX_REPROVADO.png (item 8).


import re
from pathlib import Path

import pytest
from selenium import webdriver

EVIDENCIAS = Path(__file__).parent / "evidencias"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    })
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=1366,900")
    navegador = webdriver.Chrome(options=options)
    yield navegador          # o teste roda aqui
    navegador.quit()         # roda mesmo se o teste falhar


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    relatorio = yield
    if relatorio.when == "call" and "driver" in item.funcargs:
        ct = re.search(r"ct_(\d{3})", item.name)
        if ct:
            status = "APROVADO" if relatorio.passed else "REPROVADO"
            EVIDENCIAS.mkdir(exist_ok=True)
            item.funcargs["driver"].save_screenshot(
                str(EVIDENCIAS / f"CT-{ct.group(1)}_{status}.png"))
    return relatorio