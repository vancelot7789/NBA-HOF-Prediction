from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re


headers = {'User-Agent': 'Mozilla/5.0'}
player_url_list = open("nba_players_url.csv","r")
#
# url = "https://www.basketball-reference.com/players/a/adamsst01.html"
# url = "https://www.basketball-reference.com/players/a/abdelal01.html"
for player_url in player_url_list:

    player = player_url.replace("\n","")
    res = requests.get(player,headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    player_name = soup.find("h1").text
    print(player_name)


    if soup.find("div",{"class":"media-item"})!=None:

        media = soup.find("div",{"class":"media-item"})
        pic  = (media.find("img"))
        photo = pic.get('src')
        html = requests.get(photo)


        with open("./nba_player_image/"+player_name+".jpg",'wb') as file:
            file.write(html.content)
            file.flush()
