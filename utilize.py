import base64
import os
import subprocess
from  openpyxl import Workbook
import requests
from bs4 import BeautifulSoup
import time

def encrypt(input: str):
    return base64.b64encode(input.encode("utf-8")).decode('utf-8')

def run_bat():
    #取得當前資料夾
    current = os.getcwd()
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    user_data_dir = os.path.join(current, "google")
    #bat指令
    port = 8888
    cmd = f'"{chrome_path}" --remote-debugging-port={port} --user-data-dir="{user_data_dir}"'
    #建立google資料夾
    os.makedirs(user_data_dir, exist_ok=True)
    p = subprocess.Popen(cmd, shell=False)

def make_xlsx(titles: list, filename: str):
    wb = Workbook()
    ws = wb.active

    for title in titles:
        if int(title[1]) > 0 or title[2] != "":
            ws.append(title)

    wb.save(filename)

def get_upvote_content(url):
    full_url = f"https://www.reddit.com{url}"
    res = requests.get(full_url, headers={
        "User-Agent": "Mozilla/5.0"
    })

    soup = BeautifulSoup(res.text, 'html.parser')
    body = soup.find('shreddit-post-text-body')
    if body:
        body = body.find('p')
        if body:
            body = body.text.strip()
    if body is None:
        body = ""
        
    upvote = soup.find("shreddit-post", attrs={"score": True})
    if upvote:
        upvote = upvote.get('score')
    else:
        upvote = 0
    time.sleep(1)
    return upvote, body