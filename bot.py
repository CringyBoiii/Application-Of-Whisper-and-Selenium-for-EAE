from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
from parsel import Selector
import re

import pandas as pd
import time

def init():
    global driver
    os.system("taskkill /im chrome.exe /f")
    options = Options()
    #options.add_argument('--headless')#makes chrome invisible
    options.add_argument('--profile-directory=Default') #to get profile directory do chrome://version/
    options.add_argument('--user-data-dir=C:\\Users\\Cringy\\AppData\\Local\\Google\\Chrome\\User Data\\')#to get user path do chrome://version/
    driver  = uc.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", options=options)#to get exe path do chrome://version/
    driver.get("https://beta.character.ai/chat?char=mykmRGTY0YpvAYye-WpNUSP-2LN2xidGGy9wau_0b_k")
    #driver.minimize_window()

    return driver

    
def monika_ent(txt,tbox,send):
    tbox.send_keys(txt)
    send.click()
def monika_clear(tbox):
    tbox.clear()

def monika_out():
    l = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"markdown-wrapper.markdown-wrapper-last-msg.swiper-no-swiping"))
    )
    z = l.get_attribute("innerHTML").split("\n")
    r = []
    res = l.text.split("\n")
    for i in range(len(z)):
        if z[i][57:61] == "<em>":
            r.append(i)
    try:
        for i in r:
            res.pop(i)
    except:
        pass

    return " ".join(res).replace("Monika:", "").replace("- Monika", "")
    
def quit():
    driver.quit()
init()
print(monika_out())
#python bot.py