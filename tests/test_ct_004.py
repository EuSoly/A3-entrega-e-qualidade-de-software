# tests/test_ct_004.py
# Cenário CT-004 | Requisito RF-002 (negativo)
# Caso de teste: Pesquisar com o campo vazio.
# Resultado esperado: o botão de busca permanece desabilitado, impedindo a busca.

from pages.busca_page import Pagina_inicial


def test_ct_004(driver):
    pagina = Pagina_inicial(driver)

    # Caso negativo: com o campo de busca vazio, o botão de pesquisa fica
    # desabilitado e a busca não pode ser realizada.
    assert pagina.busca_vazia_bloqueada()
