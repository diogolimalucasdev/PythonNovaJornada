""""
primeiro eu instalei o seleneium: pip install selenium
depois fui ate pypi.org e pesquisei selenium e fui ate o driver do chrome que é o navegador que utilizo
https://pypi.org/project/selenium/
e extraio o pacote para meu projeto
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from dados_git_hub import usuario, senha

"esse codigo da classe é padrao para instanciar "
class ChromeAuto:
    def __init__(self):
        "caminho de onde ta meu chromedriver"
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir=C:\Users\Administrador\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome(self.driver_path,options=self.options)

    "aqui eu defino o site em que eu quero acessar "
    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_sign_in(self):
        try:
            "encontrando o elemento, Lembrando que o nome tem que estar indentico"
            btn_sig_in = self.chrome.find_element(By.LINK_TEXT, 'Sign in')
            btn_sig_in.click()

        except Exception as e:
            print('Erro ao cliclar em sign in: ', e)

    def faz_login(self):
        try:
            input_login = self.chrome.find_element(By.ID, 'text').send_keys(usuario)
            input_password = self.chrome.find_element(By.ID, 'password').send_keys(senha)
        except Exception as e:
            print('Erro ao fazer login: ', e)



if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    chrome.clica_sign_in()
    chrome.faz_login()
    sleep(3)
    chrome.sair()
