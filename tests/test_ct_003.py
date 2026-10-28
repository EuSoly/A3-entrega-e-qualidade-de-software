# tests/test_ct_003.py
# Cenário CT-003 | Requisito RF-002 (negativo)
# Caso de teste: Pesquisar um produto inexistente.
# Resultado esperado: A busca não retorna anúncios (lista vazia).
# Evidência gerada: evidencias/CT-003_APROVADO.png ou evidencias/CT-003_REPROVADO.png

from pages.busca_page import Pagina_inicial


def test_ct_003(driver):
    pagina = Pagina_inicial(driver)
    pagina.Pesquisar("nabucodonosor2000")  
    anuncios = pagina.Listar(1)

    assert len(anuncios) == 0
