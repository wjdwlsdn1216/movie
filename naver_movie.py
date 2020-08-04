import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://movie.naver.com/movie/running/current.nhn"

URL = base_url
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

selection = soup.select('div[id=content] > div.article > div.obj_section > div.lst_wrap > ul.lst_detail_t1 > li')


for movie_data in selection:
    title = movie_data.select_one('dl.lst_dsc > dt.tit > a').text
    code = movie_data.select_one('dl.lst_dsc > dt.tit > a')['href'].split('=')[1]

    print(f'title: {title} code: {code}')
    data = {
        "title":title,
        "code":code
    }
    with open("naver_movie.csv", "a", encoding="utf-8", newline="") as csvfile:
        fieldnames = ["title","code"]
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writerow(data)