import requests
from bs4 import BeautifulSoup

input_name = input('以下有南部威秀跟國賓兩電影院\n請輸入你要查詢的電影名稱：')
print("\n")
# GET國賓
# 上圖(Http Verb)中的Request URL
url = "https://www.ambassador.com.tw/home/TheaterList"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
req = requests.get(url, headers=headers)
req.encoding = 'utf8'
soup = BeautifulSoup(req.text, "html.parser")  # 將網頁資料以html.parser
links = soup.find_all("div", class_="grid-x grid-margin-x small-up-1 medium-up-2 large-up-3 news-list-page theater")
name2 = []
name4 = []
day = []
print("國賓:高雄義大世界:\n")
for link in links:
    url2 = link.find_all("div", class_="cell")
    for href in url2:
        name = href.select('a')
        name2.append(name[0].get('href'))
url = "https://www.ambassador.com.tw"
req = requests.get(url + name2[8], headers=headers)
soup = BeautifulSoup(req.text, "html.parser")  # 將網頁資料以html.parser
name2.clear()
links = soup.find_all("div", class_="tabs-content")
for link in links:
    url2 = link.find_all("li", class_="has-submenu")
    for uri in url2:
        name3 = uri.select('a')
        for i in range(len(name3)):
            day.append(name3[i].text)
            name4.append(name3[i].get('href'))

    for i in range(7):
        if i >= 1:
            req = requests.get(url + name4[i], headers=headers)
            soup = BeautifulSoup(req.text, "html.parser")  # 將網頁資料以html.parser
            link2 = soup.find_all("div", class_="showtime-item")
            print(day[i])

            for link3 in link2:
                name = link3.find_all("div", class_='theater-box')
#                print(name[0])
                for fuck in name:
                    fuck2 = fuck.find_all("p", class_="tag-seat")
                time = link3.find_all('h6')
                if len(fuck2[0]) > 0:
                    fuck3 = str(fuck2[0].text)
                    if fuck3.find(input_name) >= 0:
                        print(fuck3)
                        for i in range(len(time)):
                            print(time[i].text, end=" ")
                        print(end="\n")
            print(end="\n\n")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# POST威秀
url = "https://www.vscinemas.com.tw/ShowTimes//ShowTimes/GetShowTimes"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
payload = {'CinemaCode': 'KS'}
req = requests.post(url, data=payload, headers=headers)
req.encoding = 'utf8'
# print(req.text)
soup = BeautifulSoup(req.text, "html.parser")  # 將網頁資料以html.parser
links = soup.find_all("div", class_="col-xs-12")
print("威秀:高雄大源百:\n")
for link in links:
    name = link.find_all('strong', class_='col-xs-12 LangTW MovieName')
    day = link.find_all('strong', class_='col-xs-12 LangTW RealShowDate')
    time = link.find_all('div', class_='col-xs-12 SessionTimeInfo')
    if len(name) > 0:
#        print(type(name[0]))
        name[0] = name[0].string
#        print(type(name[0]))
        if name[0].find(input_name) >= 0:
            print(name[0].strip())
            i = 0
            for times in time:
                print(end="     ")
                print(day[i].text.strip())
                time2 = times.find_all('div', class_='col-xs-0')
                print(end="     ")
                for j in range(len(time2)):
                    print(time2[j].text.strip(), end=" ")
                print("\n")
                i = i + 1
            print(end="\n\n")