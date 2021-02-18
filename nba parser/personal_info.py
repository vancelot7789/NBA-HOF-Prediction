from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re

headers = {'User-Agent': 'Mozilla/5.0'}
player_url_list = open("nba_players_url.csv","r")

w = open("nba_player_detail_info.csv","w")

columns = ["Name","Pos","Height","Weight","Born","Draft","School","Exp","Photo_url"]

for i in range(len(columns)):
    if i == len(columns)-1:
        w.write("%s\n"%(columns[i]))
    else:
        w.write("%s,"%(columns[i]))

# player_url_list = ["https://www.basketball-reference.com/players/b/bornhja01.html"]
# player_url_list = ["https://www.basketball-reference.com/players/b/balllo01.html"]
for player_url in player_url_list:
    player = player_url.replace("\n","")
    res = requests.get(player,headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    if soup.find("div",{"class":"stats_pullout"}) != None:
        player_name = soup.find("h1").text
        print(player_name)

        weight = "-"
        height ="-"
        position = "-"
        born = "-"
        draft = "-"
        school = "No College"
        exp = "-"
        details = (soup.find_all("p"))
        if(soup.find("span",{"itemprop":"height"}))!=None:
            height = soup.find("span",{"itemprop":"height"}).text
        if (soup.find("span",{"itemprop":"weight"}))!=None:
            weight = soup.find("span",{"itemprop":"weight"}).text



        for detail in details:
            if detail.find("strong") != None:
                if "Position" in detail.find("strong").text:
                    position = detail.text
                    position = (position.replace("\n","").split(":")[1].split("▪")[0].replace(" ","").split("and")[0])
                if "Born" in detail.find("strong").text:
                    if (detail.find("span",{"id":"necro-birth"}))!=None:
                        born = (detail.find("span",{"id":"necro-birth"}))
                        born = (born.get("data-birth"))
                if "Draft" in detail.find("strong").text:
                    draft = detail.text
                    draft = (draft.replace("\n","").replace(",","").split(":")[1]).lstrip()
                if "College" in detail.find("strong").text:
                    school = detail.text
                    school = (school.replace("\n","").split(":")[1]).lstrip()
                if "Experience" in detail.find("strong").text:
                    exp = detail.text
                    exp = (exp.replace("\n","").split(":")[1].lstrip())

        photo_url = "-"
        if soup.find("div",{"class":"media-item"})!=None:

            media = soup.find("div",{"class":"media-item"})
            pic  = (media.find("img"))
            photo_url = pic.get('src')

        print(draft)

        w.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(player_name,position,height,weight,born,draft,school,exp,photo_url))

w.close()
