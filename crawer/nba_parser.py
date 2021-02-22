from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re

table=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
list = []

out = open("nba_players_url.csv","w")
for alphabet in range(len(table)):
    res = requests.get("https://www.basketball-reference.com/players/"+table[alphabet]+"/")
    soup = BeautifulSoup(res.text, "html.parser")
    str = soup.find("caption").text
    number_of_players= [int(s) for s in str.split() if s.isdigit()]
    number_of_players = number_of_players[0]+1
    headrows = soup.find_all('tr')

    for j in range(1,number_of_players):
        player = headrows[j].find("th").text
        player_url = headrows[j].find("th").find("a").get('href')
        list.append(player_url)
        out.write("https://www.basketball-reference.com"+player_url)
        out.write("\n")

print(list)
