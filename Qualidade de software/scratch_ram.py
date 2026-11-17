import io, sys, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from selenium import webdriver
from pages.busca_page import Pagina_inicial

def norm(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(options=options)
try:
    termo = "Memoria ram"
    pagina = Pagina_inicial(driver)
    pagina.Pesquisar(termo)
    anuncios = pagina.Listar(1)
    total = len(anuncios)
    print("total:", total)

    # CT-05 relacao termo
    bruto = sum(1 for a in anuncios if termo.lower() in a["titulo"].lower())
    normd = sum(1 for a in anuncios if norm(termo) in norm(a["titulo"]))
    so_ram = sum(1 for a in anuncios if "ram" in a["titulo"].lower())
    print(f"CT05  match_bruto={bruto}/{total}  match_norm={normd}/{total}  contem_ram={so_ram}/{total}")

    # CT-06 nome e preco
    sem_tit = sum(1 for a in anuncios if not a["titulo"].strip())
    sem_preco = sum(1 for a in anuncios if not a["preco"].strip())
    print(f"CT06  sem_titulo={sem_tit}  sem_preco={sem_preco}")

    # CT-07 marca
    sem_marca = [a for a in anuncios if not a["marca"]]
    print(f"CT07  sem_marca={len(sem_marca)}/{total}")
    for a in sem_marca[:8]:
        print("   sem marca:", a["titulo"][:75])
finally:
    driver.quit()
