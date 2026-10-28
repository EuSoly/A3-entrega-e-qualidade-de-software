## conftest pra gerar as evidencias, ele faz um hook que roda antes de cada teste para gerar uma print com o nome do teste e se foi aprovado ou nao na pasta de evidencias


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
    yield navegador          
    navegador.quit()         


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