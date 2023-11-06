import webbrowser

import pyautogui, pyperclip, yaml

global c
global cars
time = 1
vezes = 10

# if __name__ == '__main__':
#     stream = open('config.yaml', 'r')
#     c = yaml.safe_load(stream)
#
# refuel = c['time_intervals_refuel']
# claim = c['time_intervals_claim']
#
# print(f'Tempo do Refuel: {refuel}')
# print(f'Tempo do Claim: {claim}')

browser = pyautogui.getWindowsWithTitle('CryptoCars Play')
print(browser)

def checkCars():
    if pyautogui.locateOnScreen('Targets/cars_clicked.png'):
        cars = pyautogui.locateOnScreen('Targets/cars_clicked.png')
        print('Cars tab was already selected...')

    if pyautogui.locateOnScreen('Targets/cars_nocliked.png'):
        cars = pyautogui.locateOnScreen('Targets/cars_nocliked.png')
        print("Cars tab don't clicked yet...")
        pyautogui.click(cars)
        print('Cars tab clicked...')

def clickRefuel():
    pass

def scrollCars():
    pyautogui.scroll(-1200, 0, 0)

def clickReward():
    reward = pyautogui.locateOnScreen('Targets/rewards.png')
    pyautogui.click(reward)

def clickClaim():
    claim = pyautogui.locateOnScreen('Targets/claim.png')
    print(claim)
    # pyautogui.sleep(3)
    # print(pyautogui.position())
    pyautogui.click(claim)

def check_refuel():
    if pyautogui.locateOnScreen('Targets/refuel_not_ready.png'):
        print("Refuel don't ready yet...")

    if pyautogui.locateOnScreen('Targets/refuel_ready.png'):
        refuel = pyautogui.locateOnScreen('Targets/refuel_ready.png')
        print("Reafuel ready! Clicking...")
        pyautogui.click(refuel)
        pyautogui.sleep(2)
        # refuel_ok = pyautogui.locateOnScreen('Targets/refuel_ok.png')
        # pyautogui.click(refuel_ok)
        pyautogui.press('enter')

c = 1
def racing():
    for c in range(10):
        print(f'Trying close pop-up... {c} of 10')
        if pyautogui.locateOnScreen('Targets/close_button.png'):
            close = pyautogui.locateOnScreen('Targets/close_button.png')
            pyautogui.click(close)

        pyautogui.sleep(10)
        c+=1

def check_low_mp():
    try:
        if pyautogui.locateOnScreen('Targets/marketplace_not_ready.png'):
            marketplace = pyautogui.locateOnScreen('Targets/marketplace_not_ready.png')
            pyautogui.click(marketplace)
    except:
        print('Fail verifying if Marketplace button is clicked. Trying again...')
    try:
        if pyautogui.locateOnScreen('Targets/buy_button_mp.png'):
            buy_button = pyautogui.locateOnScreen('Targets/buy_button_mp.png')
            print(f'Achou {buy_button}')
            count = 3
        else:
            print('Não achou...')
            pyautogui.scroll(-700)

        pyautogui.sleep(5)
        pyautogui.scroll(2000)
        reload = pyautogui.locateOnScreen('Targets/btn_reload_mp.png')
        pyautogui.click(reload)
    except:
        print('Fail verifying Marketplace cars. Trying again...')

# while range(1):
# checkCars()
# check_refuel()
    # if pyautogui.locateOnScreen('Targets/start_not_ready.png'):
    #     scrollCars()
    # clickReward()
    # pyautogui.sleep(3)
    # clickClaim()
    # msg = f'Waiting for {time} minute...'
    # for c in range(time * 60):
    #     msg+='.'
    #     print(msg)
    #     c+=1
    #     pyautogui.sleep(1)
    # # pyautogui.sleep(5)
# racing()
while c <= vezes:
    check_low_mp()
    print(f'Verificado {c}/{vezes}')
    c+=1


# pyautogui.hotkey('alt', 'tab')
