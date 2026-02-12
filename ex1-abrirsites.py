import pyautogui
import time

# tempo de reposta
pyautogui.PAUSE = 0.5

# pyautogui.press() -> apertar 1 tecla
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=696, y=492)

# entrar no site
pyautogui.write("https://docs.google.com/forms/d/e/1FAIpQLScIMl1Fbc0uYwaaYQLYRU9hkFO7t4yd4bq1pd6Ya3WcsJD4Pg/viewform")
pyautogui.press("enter")

# pausar o código
time.sleep(2)

# preencher o formulário
pyautogui.click(x=506, y=302)
pyautogui.write("Helder Paulino")
pyautogui.press("tab")

pyautogui.write("20")
pyautogui.press("tab")

# enviar o formulário
time.sleep(2)
pyautogui.press("enter")
