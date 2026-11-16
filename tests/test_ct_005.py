# tests/test_ct_005.py
# Cenário CT-005 | Requisito RF-003
# Caso de teste: Os anúncios exibidos devem ser relacionados ao termo pesquisado.
# Resultado esperado: a maioria dos títulos retornados contém o termo buscado.

from pages.busca_page import Pagina_inicial


def test_ct_005(driver):
    termo = "mouse"
    pagina = Pagina_inicial(driver)
    pagina.Pesquisar(termo)
    anuncios = pagina.Listar(1)

    assert len(anuncios) > 0

    # RF-03: os anúncios devem ser relacionados ao termo pesquisado.
    relacionados = [a for a in anuncios if termo.lower() in a["titulo"].lower()]
    assert len(relacionados) / len(anuncios) >= 0.8
