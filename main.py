import schedule

import time

import pyautogui as pd


def farm():
    print('Iniciando Farm...')
    list =[]
    c = 20
    pd.press('win')
    time.sleep(1)
    pd.write('edg')
    time.sleep(2)
    pd.press('enter')
    time.sleep(3)
    while c > 0:
        pd.hotkey('ctrl','l')
        list += 'a'
        pd.write(list)
        time.sleep(1)
        pd.press('enter')
        time.sleep(1)
        print(list)
        c -= 1
    else:
        list = ''
        pd.hotkey('alt','f4')

print('Start Verify...')
schedule.every().day.at("19:00").do(farm)

while 1:
    schedule.run_pending()
    time.sleep(1)
    print('verificando')

