import requests
from utilize import run_bat
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

#打開網頁
run_bat()

url = "https://www.reddit.com/login/"
option = Options()
option.add_experimental_option("debuggerAddress", f"127.0.0.1:{8888}")
driver = webdriver.Chrome(options=option)
driver.get(url)
#等待登入動作完成
ok = input("If login success: Please input OK: ")
# profile_url = "https://www.reddit.com/user/Fearless_Mousse1763/comments/"
profile_url = "https://www.reddit.com/user/lolzzz0601/comments/"
driver.get(profile_url)
#滾滾輪
last_height = 0
i = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        if i == 5:
            break
        i += 1
    else:
        last_height = new_height
        i = 0

soup = BeautifulSoup(driver.page_source, "html.parser")
arts = soup.find_all("span", attrs={"class": "ml-xs"})
total = 0
for art in arts:
    if "views" in art.text:
        total += art.text
        print(art.text)
        print("============================================")