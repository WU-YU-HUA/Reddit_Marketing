from utilize import run_bat, make_xlsx
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time as timesleep
from bs4 import BeautifulSoup

titles = []

def with_keyword(social="OLED_Gaming", time="month", sorted="top", keyword="GIGABYTE"):
    url = f"https://www.reddit.com/r/{social}/search/?q={keyword}&sort={sorted}&t={time}"
    option = Options()
    option.add_experimental_option("debuggerAddress", f"127.0.0.1:{8888}")
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    #滾滾輪
    last_height = 0
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        timesleep.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        else:
            last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")

    articles = soup.find_all("a", {"data-testid": "post-title"})
    for art in articles:
        title = art.get('aria-label')
        if title not in titles:
            titles.append(title)
    # driver.close()

def with_main(social="OLED_Gaming", time="month", sorted="top", keyword="GIGABYTE"):
    #開始執行
    with_keyword(social, time, sorted, keyword)

    make_xlsx(titles=titles, filename=f"{social}_{time}_{sorted}_with_{keyword}.xlsx")
