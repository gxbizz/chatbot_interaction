from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def comunicar_distribuidoras(numero, mensagem):
    # Configurações do Chrome
    options = Options()
    # Adicionar argumento para usar perfil existente (opcional)
    # options.add_argument("user-data-dir=/caminho/para/seu/perfil/do/chrome")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com")

    # Pausa para aguardar o login manual
    input("Escaneie o QR Code e pressione ENTER para continuar...")

    try:
        # Localiza o campo de busca
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.send_keys(numero)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        # Envia a mensagem
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
        message_box.click()
        message_box.send_keys(mensagem)
        message_box.send_keys(Keys.RETURN)
        time.sleep(5)

        # Captura as mensagens recebidas
        mensagens_recebidas = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in")]')
        ultima_resposta = mensagens_recebidas[-1].text if mensagens_recebidas else "Nenhuma resposta recebida."
        return ultima_resposta

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return "Erro ao se comunicar com a distribuidora."

    finally:
        # Garante que o driver será fechado
        driver.quit()

# Exemplo de uso
numero = "+5511999998888"  # Substitua pelo número da distribuidora
mensagem = "12345678000195"
resposta = comunicar_distribuidoras(numero, mensagem)
print("Resultado final:", resposta)
