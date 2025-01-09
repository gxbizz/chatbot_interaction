from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()

driver = webdriver.Chrome(options=options) # finalizar driver ao acabar
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code e pressione ENTER para continuar...")

def entrar_na_conversa(contato):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(contato)
    search_box.send_keys(Keys.RETURN)

def mandar_mensagem(mensagem):
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.click()
    message_box.send_keys(mensagem)
    message_box.send_keys(Keys.RETURN)

def ultima_resposta(anten):
    if(not anten): anten = 1
    mensagens_recebidas = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in")]//div[contains(@class, "copyable-text")]')
    ultima_resposta = mensagens_recebidas[-anten].text if mensagens_recebidas else "Nenhuma resposta recebida."
    return ultima_resposta

def estrategia_teste(cpf):
    entrar_na_conversa("energisa")
    time.sleep(5)
    mandar_mensagem("oi")
    time.sleep(10)
    mandar_mensagem("Não")
    time.sleep(15)
    mandar_mensagem("Faturas e Pagamentos")
    time.sleep(15)
    mandar_mensagem("Pagar Fatura")
    time.sleep(15)
    mandar_mensagem(cpf)
    time.sleep(15)
    mandar_mensagem("Continuar com CPF")
    time.sleep(15)
    mandar_mensagem("sim")
    time.sleep(15)
    print(ultima_resposta(4))
    mandar_mensagem("Encerrar")
    time.sleep(10)
    mandar_mensagem("Não")
    time.sleep(10)
    mandar_mensagem("10")
    time.sleep(5)
    mandar_mensagem("encerrar")
    time.sleep(5)
    mandar_mensagem("sim")
    

estrategia_teste("84573309187")
