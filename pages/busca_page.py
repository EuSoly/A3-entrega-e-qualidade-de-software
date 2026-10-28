# pages/busca_page.py
# Page Object da página de resultados da busca.
# Responsável por: ler os anúncios exibidos e devolver os dados de cada um
# (nome, preço e link do produto).
# Contém só seletores, esperas explícitas e ações. Sem asserts.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.caracteristicas import separar

class Pagina_inicial:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.kabum.com.br/'
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)

    def acessar_navegador(self):
        self.driver.get(self.url)
        


    def Pesquisar(self,produto):
        self.acessar_navegador()
        barra = self.wait.until(EC.element_to_be_clickable((By.ID, 'inputBusca')))
        barra.send_keys(produto)
        ##print('produto digitado')
        self.wait.until(EC.text_to_be_present_in_element_value((By.ID, 'inputBusca'), produto))
        ##print('ok para clicar em pesquisar')
        botao = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-testid="buttonBuscaKabum"]')))
        botao.click()
        ##print('pesquisar clicado')
        self.wait.until(EC.url_changes(self.url))


    
    def Listar(self, max_paginas):
        cards = (By.CSS_SELECTOR, "#main-content a[href*='/produto/']")
        proximo = (By.CSS_SELECTOR, "a.nextLink")
        anuncios = []
        for paginar in range(max_paginas):
            try:
                num_cards = self.wait.until(EC.presence_of_all_elements_located(cards))
            except TimeoutException:
                break   
            for card in num_cards:
                dados = self.extrair(card)
                dados.update(separar(dados['titulo']))
                anuncios.append(dados)
           
            if paginar + 1 == max_paginas or not self.proxima_pagina(proximo, num_cards[0]):
                break
        return anuncios

    def proxima_pagina(self, proximo, primeiro_card):
        botao = self.driver.find_element(*proximo)
        if botao.get_attribute("aria-disabled") == "true":
            return False
       
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'})", botao)
        botao.click()
        
        self.wait.until(EC.staleness_of(primeiro_card))
        return True

    def extrair(self, card):
        partes_preco = card.find_elements(By.CSS_SELECTOR,"span.text-base.font-semibold")
        return{
        "titulo": card.find_element(By.CSS_SELECTOR, "span.line-clamp-2").text,
        "preco": " ".join(p.text for p in partes_preco),
        "link": card.get_attribute("href"),
        }

        




if __name__ == '__main__':
    ## COnfigurações do navegador
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    produto = "Memoria Ram"

    try:
        pagina = Pagina_inicial(driver)
        pagina.Pesquisar(produto)
        print("URL:", driver.current_url)
        anuncios = pagina.Listar(2)

        for a in anuncios:
            print(f"{a['preco']:>12} | {a['marca']} | {a['capacidade']}GB | "
                  f"{a['frequencia']} | {a['tipo']} | {a['titulo'][:60]}")

        # resumo: quantos anúncios ficaram com cada campo vazio
        print(f"\nTotal: {len(anuncios)} anúncios")
        for campo in ["titulo", "preco", "link", "marca", "capacidade", "frequencia", "tipo"]:
            vazios = [a["titulo"] for a in anuncios if not a[campo]]
            print(f"{campo:>10}: {len(vazios)} vazios")
            for t in vazios[:3]:
                print("            ex.:", t)

        input("Enter para fechar...")
    finally:
        driver.quit()
        
