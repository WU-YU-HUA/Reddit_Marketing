import base64
import os
import subprocess
from  openpyxl import Workbook

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
        ws.append([title])

    wb.save(filename)