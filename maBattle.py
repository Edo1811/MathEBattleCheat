from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pynput import keyboard
from colorama import Fore, Style, init

init()

print(Fore.RED + "Egg error")
print(Fore.YELLOW + "Egg warning")
print("test")
print(Style.RESET_ALL)
print("test again")

driver = webdriver.Chrome()
driver.get("https://mathebattle.de/edu_battles/response/97877579?result=1")
print("Driver aqquired, proceding to Login")
inputuser = input("Log in and then press ENTER here...")
print(f"Login successfull for user <{inputuser}>")
print(Fore.RED + "Error (most recent call):\n    Error in class webdriver.Chrome (geainnosstudios.software.apps.webdriver.Chrome): \n        webdriver.Chrome says: Thread exclusive variable <inputuser> was not read properly or contains NONE\n    The Process on thread <4x8241B> can continue")
print(Style.RESET_ALL)

# Global variables
btnend = None
alt_pressed_flag = False

# ALT listener
def on_press(key):
    global btnend, alt_pressed_flag
    try:
        if key == keyboard.Key.shift_r and btnend is not None:
            print("keyboard.Key.shift_r says: 'Keyboard SHIFT_R pressed' \nStarting process 'keyboard.Listener(on_press=on_press)" + Fore.YELLOW + "\nWARNING! The process <keyboard.Listener()> runs in background and may affect your RAM!")
            print(Style.RESET_ALL)
            alt_pressed_flag = True
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()  # runs in background


erroredalready = False
# Main loop
while not erroredalready:
    try:
        # Click first two buttons
        btn2 = driver.find_element(By.ID, "content-type-524")
        btnsubm = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[5]/div/div/form/div[2]/input")
        print("Looking for object: </html/body/div[1]/div/div[2]/div[5]/div/div/form/div[2]/input> by XPATH")
        btn2.click()
        btnsubm.click()
        time.sleep(0.5)  # let END button appear
        

        # Fetch END button
        btnend = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div[2]/form/div/input")
        print("Looking for object: </html/body/div[1]/div/div[2]/div[4]/div[2]/form/div/input> by XPATH...\
              \nObject found: Process webdriver.Chrome.find_element(by.XPATH) says: 'Object with type <BUTTON> was successfully found")

        # Wait until ALT is pressed
        print("Waiting for keyboard.Key.shift_r to return <Pressed>...")
        while not alt_pressed_flag:
            time.sleep(0.1)
        print(Fore.YELLOW + "keyboard.Key.shift_r says: 'Keyboard SHIFT_R pressed'")
        print(Style.RESET_ALL)

        # Click END
        btnend.click()
        print("Object </html/body/div[1]/div/div[2]/div[4]/div[2]/form/div/input> with type <BUTTON> has been clicked\nResetting alt_flag." + Fore.YELLOW + "\nWARNING! Class webdriver.Chrome.main did not load properly, press STRG+C to end the process")
        print(Style.RESET_ALL)
        alt_pressed_flag = False  # reset flag for next loop
        time.sleep(0.5)

    except Exception as e:
        erroredalready = True
        print(Fore.RED + "Class webdriver.Chrome.main (software.apps.webdriver.Chrome.main.driver) has ended unexpectedly: \nLoop error:", e)
        time.sleep(1)
        print(Style.RESET_ALL)
        input("Press ENTER to exit...")
