# tests/test_ct_002.py
# Cenário CT-002 | Requisito RF-002

from pages.busca_page import Pagina_inicial


def test_ct_002(driver):
    pagina = Pagina_inicial(driver)
    pagina.Pesquisar("Memoria ram")      
    anuncios = pagina.Listar(1)          

    assert len(anuncios) > 0
