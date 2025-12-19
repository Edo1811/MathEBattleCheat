from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pynput import keyboard

driver = webdriver.Chrome()
driver.get("https://mathebattle.de/edu_battles/response/97877579?result=1")
input("Log in and then press ENTER here...")

# Global variables
btnend = None
alt_pressed_flag = False

# ALT listener
def on_press(key):
    global btnend, alt_pressed_flag
    try:
        if key == keyboard.Key.shift_r and btnend is not None:
            print("r shift pressed!")
            alt_pressed_flag = True
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()  # runs in background

# Main loop
while True:
    try:
        # Click first two buttons
        btn2 = driver.find_element(By.ID, "content-type-524")
        btnsubm = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[5]/div/div/form/div[2]/input")
        btn2.click()
        btnsubm.click()
        time.sleep(0.5)  # let END button appear

        # Fetch END button
        btnend = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div[2]/form/div/input")

        # Wait until ALT is pressed
        print("Waiting for ALT to click END...")
        while not alt_pressed_flag:
            time.sleep(0.1)

        # Click END
        btnend.click()
        print("END clicked!")
        alt_pressed_flag = False  # reset flag for next loop
        time.sleep(0.5)

    except Exception as e:
        print("Loop error:", e)
        time.sleep(1)
