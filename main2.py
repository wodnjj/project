from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

address = "https://sports.news.naver.com/wfootball/schedule/index?year=2023&month=05&category=premier"
request = requests.get(address)
html = request.text
soup = BeautifulSoup(html, 'html.parser')
soupData = [soup.findAll("div", {"class" : "sch_tb"}), soup.findAll("div", {"class" : "sch_tb2"})] #sch_tb랑 tb2둘다 저장

dataList = [] #dataList에 저장하기

for data_tb in soupData: #div 리스트 개개를 data_tb라고 정의하고 soupData에서 순서대로 불러오기
    for data in data_tb: #날짜별 한줄씩
        data_val = data.findAll("span", {"class" : "td_data"})[0].text #날짜뽑기
        match_cnt = data.findAll("td")[0]['rowspan'] # 경기 수 뽑기
        if int(match_cnt) == 5: #rowspan 5개면 패스(경기없는 날)
            continue

        for i in range(0, int(match_cnt)) : #경기당 한줄씩
            matchData = {}
            matchData["날짜"] = date_val
            matchData["시간"] = data.findAll("tr")[i].findAll("span", {"class":"td_hour"})[0].text #시간
            matchData["홈팀"] = data.findAll("tr")[i].findAll("span", {"class":"team_lft"})[0].text
            matchData["원정팀"] = data.findAll("tr")[i].findAll("span", {"class":"team_rgt"})[0].text
            matchData["구장"] = data.findAll("tr")[i].findAll("span", {"class":"td_stadium"})[0].text

            dataList.append(matchData) #matchdata를 datalist 저장

#df = pd.DataFrame(dataList)    #pandas로 출력        
#df.T.to_csv('premier.csv', encoding='cp949')   #csv파일 출력 

print('premier.csv')