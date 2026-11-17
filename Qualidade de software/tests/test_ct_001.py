# tests/test_ct_001.py
# Cenário CT-001 | Requisito RF-001
# Caso de teste: Acessar a página inicial.
# Resultado esperado: A página carrega e a barra de busca está visível.
# Usa os Page Objects de pages/ e valida o resultado com assert.
# Evidência gerada: evidencias/CT-001_APROVADO.png ou evidencias/CT-001_REPROVADO.png

from pages.busca_page import Pagina_inicial

def test_ct_001(driver):
    pagina = Pagina_inicial(driver)
    pagina.acessar_navegador()

    assert driver.current_url.startswith(pagina.url)




