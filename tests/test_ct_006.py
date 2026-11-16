# tests/test_ct_006.py
# Cenário CT-006 | Requisito RF-003
# Caso de teste: Coletar nome e preço de cada anúncio.
# Resultado esperado: todo anúncio coletado tem título e preço preenchidos.

from pages.busca_page import Pagina_inicial


def test_ct_006(driver):
    pagina = Pagina_inicial(driver)
    pagina.Pesquisar("mouse")
    anuncios = pagina.Listar(1)

    assert len(anuncios) > 0

    # RF-03: todo anúncio coletado deve ter nome (título) e preço preenchidos.
    for a in anuncios:
        assert a["titulo"].strip()
        assert a["preco"].strip()
