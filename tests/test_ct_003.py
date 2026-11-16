# tests/test_ct_003.py
# Cenário CT-003 | Requisito RF-002 (negativo)
# Caso de teste: Pesquisar um produto inexistente.


from pages.busca_page import Pagina_inicial


def test_ct_003(driver):
    pagina = Pagina_inicial(driver)
    pagina.Pesquisar("zzzzzzqqqwwweee999")

    assert pagina.sem_resultado()
