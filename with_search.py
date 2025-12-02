from utilize import make_xlsx, get_upvote_content
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time as timesleep
from bs4 import BeautifulSoup
import datetime
titles = []

def with_keyword(social="OLED_Gaming", time="month", sorted="top", keyword="GIGABYTE"):
    url = f"https://www.reddit.com/r/{social}/search/?q={keyword}&sort={sorted}&t={time}"
    option = Options()
    option.add_experimental_option("debuggerAddress", f"127.0.0.1:{8888}")
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    #滾滾輪
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

    articles = soup.find_all("a", {"data-testid": "post-title"})
    for art in articles:
        title = art.get('aria-label')
        path = art.get('href')
        upvote, body = get_upvote_content(path)
        if title not in titles:
            titles.append([title, upvote, body])
    # driver.close()

def with_main(social="OLED_Gaming", time="month", sorted="top", keyword="GIGABYTE"):
    timestamp = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    #開始執行
    with_keyword(social, time, sorted, keyword)

    make_xlsx(titles=titles, filename=f"{social}_{time}_{sorted}_with_{keyword}_{timestamp}.xlsx")
