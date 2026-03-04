import pyautogui
import time

pyautogui.PAUSE = 1

# Abrir o Edge
pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('chrome')
time.sleep(0.5)

pyautogui.press('enter')
time.sleep(6)

# Focar na barra de endereços
pyautogui.hotkey('ctrl', 'l')
time.sleep(0.3)

pyautogui.press('backspace') 

# Abrir Spotify
pyautogui.write('https://open.spotify.com/intl-pt/album/3LDV2xGL9HiqCsQujEPQLb', interval=0.03)
pyautogui.press('enter')
print('Abrindo Spotify...')
time.sleep(6)

# Procurar botão play
button_location = None
while button_location is None:
    button_location = pyautogui.locateOnScreen('play3.png', confidence=0.7)
    print("procurando botão de play...")
    time.sleep(3)

button_point = pyautogui.center(button_location)
pyautogui.click(button_point)
print("Botão play localizado")
time.sleep(1)

# Nova aba
pyautogui.hotkey("ctrl", "t")
time.sleep(0.5)

# Focar barra de endereços novamente
pyautogui.hotkey('ctrl', 'l')
time.sleep(0.3)

# Abrir YouTube
pyautogui.write("https://youtu.be/sYC5BfJy2nw?si=luy1Lz9-HHNNaKsp")
pyautogui.press("enter")
print("Abrindo o Youtube...")
time.sleep(3)

# Atalhos do YouTube
pyautogui.press("m") 
time.sleep(1) # mute
pyautogui.press("f")  # fullscreen

print("Automação concluída!")