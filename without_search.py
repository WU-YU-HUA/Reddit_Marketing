from utilize import encrypt
import requests
from bs4 import BeautifulSoup
import csv
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import subprocess

event = threading.Event()

def run_bat():
    #取得當前資料夾
    current = os.getcwd()
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    user_data_dir = os.path.join(current, "google")
    #建立google資料夾
    os.makedirs(user_data_dir, exist_ok=True)
    port = 8888
    cmd = f'"{chrome_path}" --remote-debugging-port={port} --user-data-dir="{user_data_dir}"'
    subprocess.run(cmd, shell=False)

def back_work(social, time, sorted):
    run_bat()
    url = f"https://www.reddit.com/r/{social}/{sorted}/?t={time}"
    option = Options()
    option.add_experimental_option("debuggerAddress", f"127.0.0.1:{8888}")
    driver = webdriver.Chrome(options=option)
    driver.get(url)

    #滾滾輪
    while not event.is_set():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    driver.close()

def without(socialName, time, sorted, after=""):
    url = f"https://www.reddit.com/svc/shreddit/community-more-posts/{sorted}/"
    param = {
        "feedViewType": "compactView",
        "name": socialName,
        "after": encrypt(after),
        "t": time
    }

    resp = requests.get(url, params=param, headers={
        "User-Agent": "Mozilla/5.0"
    })

    soup = BeautifulSoup(resp.text, "html.parser")

    articles = soup.find_all("article")
    id = ""
    if articles:
        for art in articles:
            t = art.find("a", attrs={"data-ks-id": True})
            
            title = art.get('aria-label')
            id = t.get('data-ks-id')
            if title not in titles:
                titles.append(title)

        without(socialName, time, sorted, id)
    else:
        return

titles = []
social = input("Plz Enter Social Name (e.g. OLED_Gaming): ")
time = input("Plz Enter SortedTime (e.g. day): ")
sorted = input("Plz Enter Sorted (e.g. top, best): ")

#小互動
thread = threading.Thread(target=back_work, args=(social, time, sorted))
thread.start()
#主程式
without(socialName=social, time=time, sorted=sorted)
#結束停止
event.set()
thread.join()

with open(f"{social}_{time}_{sorted}.csv", "w", newline="", encoding='utf-8') as f:
    writer = csv.writer(f)
    for title in titles:
        writer.writerow([title])