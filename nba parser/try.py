
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import time
# player_url_list = open("nba_players_url.csv","r")
player_url_list=["https://www.basketball-reference.com/players/h/hardeja01.html","https://www.basketball-reference.com/players/p/pettibo01.html","https://www.basketball-reference.com/players/a/abdulza01.html"]
# player_url_list = ["https://www.basketball-reference.com/players/j/jamesle01.html"]
# for player_url in player_url_list:

# driver = webdriver.Chrome('/usr/local/bin/chromedriver')


# url='https://www.basketball-reference.com/players/d/davisan02.html'
# time.sleep(5)
# driver.get(url)

options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
browser = webdriver.Chrome(chrome_options=options)

for player_url in player_url_list:

    player = player_url.replace("\n","")
    # res = requests.get(player)
    browser.get(player)
    # print(browser.page_source)
    soup = BeautifulSoup(browser.page_source, "html.parser")



    if soup.find("div",{"class":"stats_pullout"}) != None:




        total_points = ((soup.find("div",{"id":"content"})).find("div",{"id":"div_totals"})).find("tfoot").find("td",{"data-stat":"pts"}).text
        total_rebounds = ((soup.find("div",{"id":"content"})).find("div",{"id":"div_totals"})).find("tfoot").find("td",{"data-stat":"trb"}).text
        total_assits = ((soup.find("div",{"id":"content"})).find("div",{"id":"div_totals"})).find("tfoot").find("td",{"data-stat":"ast"}).text

        if ((soup.find("div",{"id":"content"})).find("div",{"id":"div_totals"})).find("tfoot").find("td",{"data-stat":"blk"}) != None:
            total_blocks =  ((soup.find("div",{"id":"content"})).find("div",{"id":"div_totals"})).find("tfoot").find("td",{"data-stat":"blk"}).text
        else:
            total_blocks = '-'
        if ((soup.find("div",{"id":"content"})).find("div",{"id":"div_totals"})).find("tfoot").find("td",{"data-stat":"stl"}) != None:
            total_stls =  ((soup.find("div",{"id":"content"})).find("div",{"id":"div_totals"})).find("tfoot").find("td",{"data-stat":"stl"}).text

        else:
            total_stls = '-'


        print(total_points," ",total_rebounds," ",total_assits," ",total_blocks," ",total_stls)


        if ((soup.find("div",{"id":"content"})).find("div",{"id":"div_per_poss"})) !=None:

            drtg = ((soup.find("div",{"id":"content"})).find("div",{"id":"div_per_poss"})).find("tfoot").find("td",{"data-stat":"def_rtg"}).text
            ortg = ((soup.find("div",{"id":"content"})).find("div",{"id":"div_per_poss"})).find("tfoot").find("td",{"data-stat":"off_rtg"}).text

        else:
            drtg = '-'
            ortg = '-'

        if ((soup.find("div",{"id":"content"})).find("div",{"id":"div_advanced"})).find("tfoot").find("td",{"data-stat":"vorp"}) !=None:
            vorp = ((soup.find("div",{"id":"content"})).find("div",{"id":"div_advanced"}).find("tfoot").find("td",{"data-stat":"vorp"})).text
        else:
            vorp = '-'

        if ((soup.find("div",{"id":"content"})).find("div",{"id":"div_advanced"})).find("tfoot").find("td",{"data-stat":"bpm"}) !=None:
            bpm = ((soup.find("div",{"id":"content"})).find("div",{"id":"div_advanced"}).find("tfoot").find("td",{"data-stat":"bpm"})).text

        else:
            bpm = '-'


        print(drtg)
        print(ortg)
        print(vorp)
        print(bpm)
        # print('\n')
browser.close()
