from utilize import encrypt
import requests
from bs4 import BeautifulSoup
import csv


def without(socialName, time, after=""):
    url = "https://www.reddit.com/svc/shreddit/community-more-posts/top/"
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

        without(socialName, time, id)
    else:
        return

titles = []
social = input("Plz Enter Social Name (e.g. OLED_Gaming): ")
time = input("Plz Enter SortedTime (e.g. day): ")
without(socialName=social, time=time)

with open(f"{social}_{time}.csv", "w", newline="", encoding='utf-8') as f:
    writer = csv.writer(f)
    for title in titles:
        writer.writerow([title])