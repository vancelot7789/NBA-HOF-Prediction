from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import time
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
browser = webdriver.Chrome(chrome_options=options)
# # res = requests.get("https://www.basketball-reference.com/players/o/onealsh01.html")
# res = requests.get("https://www.basketball-reference.com/players/d/davisan02.html")
# res = requests.get('https://www.basketball-reference.com/players/j/jamesle01.html')
# res = requests.get("https://www.basketball-reference.com/players/a/abdulza01.html")
# res = requests.get('https://www.basketball-reference.com/players/a/abdulza01.html')
# soup = BeautifulSoup(res.text, "html.parser")

# soup = BeautifulSoup(driver.page_source, "html.parser")
player_url_list = open("nba_players_url.csv","r")
#
w = open("nba_player_file_new.csv","w")
# w = open("a.csv","w")
headers=['Name','Pos','Active','HoF','All_Star','All_Nba','All_Def','Score_Champ','Assit_Champ','Trb_Champ','MVP','GP','PPG','TRPG','APG','BPG','SPG','3PG','TP','TR','TAST','TBLKS','TSTLS','T3PS','FG%','3P%','FT%','EF%','DRTG','ORTG','VORP','BPM','EFF','Win_Shares']
#
for i in range(len(headers)):
    if i == len(headers)-1:
        w.write("%s\n"%(headers[i]))
    else:
        w.write("%s,"%(headers[i]))

# player_url_list=["https://www.basketball-reference.com/players/a/ablefo01.html"]
# for player_url in player_url_list:
for player_url in player_url_list.readlines():

    player = player_url.replace("\n","")
    # res = requests.get(player)
    browser.get(player)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    # soup = BeautifulSoup(res.text, "html.parser")

    if soup.find("div",{"class":"stats_pullout"}) != None:

        """name"""
        player_name = soup.find("h1").text
        print(player_name)
        w.write("%s," % (player_name))

        """position"""
        details = (soup.find_all("p"))
        for detail in details:
            if detail.find("strong") != None:
                if "Position" in detail.find("strong").text:
                    position = detail.text

                    position = (position.replace("\n","").split(":")[1].split("▪")[0].replace(" ","").split("and")[0])
                    if (position == 'PointGuard') or (position=='Guard'):
                        w.write("1,")

                    elif (position == 'ShootingGuard') or (position=='Guard/Forward'):
                        w.write("2,")

                    elif (position == 'SmallForward') or (position=='Forward/Guard'):
                        w.write("3,")

                    elif (position == 'PowerForward') or (position=='Forward/Center') or (position=='Forward'):
                        w.write("4,")

                    elif (position == 'Center') or (position=='Center/Forward'):
                        w.write("5,")


        """active or retired"""
        info = soup.find("div",{"class":"stats_pullout"})
        if info.find("strong").text == "":
            # print("not active")
            w.write('0,')

        else :
            w.write('1,')
        """accolades"""
        accolades_list = [0] * 8

        if soup.find("ul",{"id":"bling"}) != None:
            accolades = soup.find("ul",{"id":"bling"})
            if accolades.find("li",{"class":"bling_special bling_hof"}) != None:
                hall_of_fame = accolades.find("li",{"class":"bling_special bling_hof"}).text
                # print(1)
                accolades_list[0] = 1
                # print(0)
                # print(hall_of_fame)

            if accolades.find("li",{"class":"bling_special bling_all_star"}) !=None:
                all_star = accolades.find("li",{"class":"bling_special bling_all_star"}).text
                if 'x' in (all_star):
                    # print(all_star.split("x")[0])
                    accolades_list[1]  = all_star.split("x")[0]
                else:
                    accolades_list[1] = 1

            other = accolades.find_all("li")
            for x in other:
                if 'All-NBA' in x.text:
                    all_nba_team  = (x.text)
                    if 'x' in (all_nba_team):
                        # print(all_nba_team.split("x")[0])
                        accolades_list[2] = all_nba_team.split("x")[0]
                    else:
                        accolades_list[2] = 1

                if 'All-Defensive' in x.text:
                    defensive_team = x.text
                    if 'x' in (defensive_team):
                        # print(defensive_team.split("x")[0])
                        accolades_list[3] = defensive_team.split("x")[0]
                    else:
                        # print(1)
                        accolades_list[3] = 1
                if 'Scoring' in x.text:
                    scores_champ = x.text
                    if 'x' in (scores_champ):
                        # print(scores_champ.split("x")[0])
                        accolades_list[4] = scores_champ.split("x")[0]
                    else:
                        # print(1)
                        accolades_list[4] = 1
                if 'AST' in x.text:
                    assits_champ = x.text
                    if 'x' in (assits_champ):
                        # print(assits_champ.split("x")[0])
                        accolades_list[5] = assits_champ.split("x")[0]
                    else:
                        # print(1)
                        accolades_list[5] = 1

                if 'TRB' in x.text:
                    trbs_champ = x.text
                    if 'x' in (trbs_champ):
                        # print(trbs_champ.split("x")[0])
                        accolades_list[6] = trbs_champ.split("x")[0]
                    else:
                        # print(1)
                        accolades_list[6] = 1

                if 'MVP' in x.text:
                    if ('Finals' not in x.text) and ('AS' not in x.text):
                        mvp = x.text
                        if 'x' in (mvp):
                            # print(mvp.split("x")[0])
                            accolades_list[7] = mvp.split("x")[0]
                        else:
                            accolades_list[7] = 1
                            # print(1)
        for k in range(len(accolades_list)):
            w.write('%s,'%(accolades_list[k]))
        """average_stats"""

        average_stats = info.find("div",{"class":"p1"})
        games_played = average_stats.find_all("p")[1].text
        points_per_game = average_stats.find_all("p")[3].text
        rebounds_per_game = average_stats.find_all("p")[5].text
        assists_per_game = average_stats.find_all("p")[7].text
        w.write("%s,%s,%s,%s,"%(games_played,points_per_game,rebounds_per_game,assists_per_game))

        tables = ((soup.find("tfoot")).find_all("tr")[0])
        # print(tables)
        if tables.find("td",{"data-stat":"blk_per_g"}) == None:
            blocks_per_game  = "-"
        else:
            blocks_per_game = tables.find("td",{"data-stat":"blk_per_g"}).text
        if tables.find("td",{"data-stat":"stl_per_g"}) == None:
            steals_per_game = "-"
        else:
            steals_per_game = tables.find("td",{"data-stat":"stl_per_g"}).text
        if tables.find("td",{"data-stat":"fg3_per_g"}) == None:
            three_point_per_game = "-"
        else:
            three_point_per_game = tables.find("td",{"data-stat":"fg3_per_g"}).text
        w.write("%s,%s,%s,"%(blocks_per_game,steals_per_game,three_point_per_game))
        # print(games_played," ",points_per_game," ",rebounds_per_game," ",assists_per_game," ",blocks_per_game," ",steals_per_game," ",three_point_per_game)

        """total_stats"""
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
        if ((soup.find("div",{"id":"content"})).find("div",{"id":"div_totals"})).find("tfoot").find("td",{"data-stat":"fg3"}) != None:
            total_three_pointers = ((soup.find("div",{"id":"content"})).find("div",{"id":"div_totals"})).find("tfoot").find("td",{"data-stat":"fg3"}).text
        else:
            total_three_pointers = '-'
        w.write("%s,%s,%s,%s,%s,%s,"%(total_points,total_rebounds,total_assits,total_blocks,total_stls,total_three_pointers))
        # print(career_pts," ",career_blk," ",career_stl," ",career_ast," ",career_trb)


        """shooting performance"""
        shooting_percentage = info.find("div",{"class","p2"})

        check  = (len(shooting_percentage.find_all("p")))
        if check == 4:
            field_goal_percentage =  shooting_percentage.find_all("p")[1].text
            free_throw_percentage = shooting_percentage.find_all("p")[3].text
            three_point_percentage = "-"
            effective_field_goal = "-"

        elif check == 8:
            field_goal_percentage = shooting_percentage.find_all("p")[1].text
            three_point_percentage = shooting_percentage.find_all("p")[3].text
            free_throw_percentage = shooting_percentage.find_all("p")[5].text
            effective_field_goal = shooting_percentage.find_all("p")[7].text
        # print(field_goal_percentage," ",three_point_percentage," ",free_throw_percentage," ",effective_field_goal)
        # print(field_goal_percentage," ",three_point_percentage)
        w.write("%s,%s,%s,%s,"%(field_goal_percentage,free_throw_percentage,three_point_percentage,effective_field_goal))

        """advanced stats"""
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


        w.write("%s,%s,%s,%s,"%(drtg,ortg,vorp,bpm))



        other_stats = info.find("div",{"class":"p3"})
        efficiency_rating = other_stats.find_all("p")[1].text
        win_shares = other_stats.find_all("p")[3].text

        w.write("%s,%s\n"%(efficiency_rating,win_shares))
        # print(ortg," ",drtg )
        # print(efficiency_rating," ",win_shares)
        #
        #
browser.close()
w.close()
