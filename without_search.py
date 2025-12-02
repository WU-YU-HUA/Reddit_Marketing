from utilize import encrypt, make_xlsx, get_upvote_content
import requests
from bs4 import BeautifulSoup
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time as timesleep

event = threading.Event()
titles = []

def back_work(social, time, sorted):
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
            link = art.find("shreddit-post", attrs={"permalink": True}).get('permalink')

            title = art.get('aria-label')
            id = t.get('data-ks-id')
            upvote, body = get_upvote_content(link)
            if title not in titles:
                titles.append([title, upvote, body])

        without(socialName, time, sorted, id)
    else:
        return

def roll_without(socialName, time, sorted):
    url = f"https://www.reddit.com/r/{socialName}/{sorted}/?t={time}&feedViewType=compactView"
    option = Options()
    option.add_experimental_option("debuggerAddress", f"127.0.0.1:{8888}")
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    last_height = 0
    i = 0
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        timesleep.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            if i == 5:
                break
            i += 1
        else:
            last_height = new_height
            i = 0

    soup = BeautifulSoup(driver.page_source, "html.parser")

    articles = soup.find_all("article", {"aria-label": True})
    for art in articles:
        title = art.get('aria-label')
        path = art.find('a', attrs={"href": True})
        path = path.get('href')
        upvote, body = get_upvote_content(path)
        if title not in titles:
            titles.append([title, upvote, body])

def without_main(social, time, sorted):
    timestamp = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    #互動
    thread = threading.Thread(target=back_work, args=(social, time, sorted))
    thread.start()
    #主程式
    without(socialName=social, time=time, sorted=sorted)
    #結束停止
    event.set()
    thread.join()

    make_xlsx(titles=titles, filename=f"{social}_{time}_{sorted}_{timestamp}.xlsx")