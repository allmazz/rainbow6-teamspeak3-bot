# cluster top
import ts3
import threading
import json
import datetime
import traceback
import requests
import time
import sys

getByID = "https://r6tab.com/api/player.php?p_id="
rankR6 = {}
rank2R6 = {}

r6Stat = {}

def updateStat():
  with open("r6Stat", "r") as stfile:
    global r6Stat
    r6Stat = json.loads(stfile.read())

def r6s_statF():
  print("[", datetime.datetime.now(), "]", "R6S function started!")
  while True:
    try:
     updateStat()
     for client in r6sconn.clientlist(away=True):
      if client["client_database_id"] in r6Stat:
        t2 = requests.get("https://r6tab.com/" + r6Stat[client["client_database_id"]], params={"updatenow": "true"})
        t1 = requests.get(getByID + r6Stat[client["client_database_id"]])
        client_stat = json.loads(t1.text)
        rankR6[client["client_database_id"]] = client_stat["p_currentmmr"]
        rank2R6[client["client_database_id"]] = client_stat["p_currentrank"]
        if client_stat["playerfound"] == True:
         stde = "Статистика в Siege: Никнейм: " +  client_stat["p_name"] + "; Уровень: " + str(client_stat["p_level"]) + "; MMR: " + str(client_stat["p_currentmmr"]) + "; Наивысший MMR в сезоне: " + str(client_stat["p_maxmmr"]) # + "; K/D " + str(client_stat["p_maxmmr"])
         r6sconn.clientdbedit(cldbid=client["client_database_id"], client_description=stde)
         #update_top(client["client_nickname"], client_stat["p_currentmmr"])
         #r6sconn.clientaddperm(cldbid=client["client_database_id"], permsid="i_icon_id", permvalue=R6ids[str(client_stat["p_currentrank"])],permskip=True)
        else:
         print("[", datetime.datetime.now(), "]", "Player with DB id " + client["client_database_id"] + "not founded! Request URL= " + getByID + r6Stat[client["client_database_id"]])
    except Exception as e:
     print("[", datetime.datetime.now(), "]", 'Excepition in R6Stat function: ', traceback.format_exc())
    time.sleep(90)

if len(sys.argv) < 6:
  print('Run example: bot.py 192.168.1.1 serveradmin 1A2b3C4V "TeamSpeak Bot"')
  raise Exception("Not all arguments")

print("Coonnecting to TeamSpeak server...")
r6sconn = ts3.query.TS3Connection(sys.argv[1])
r6sconn.login(client_login_name=sys.argv[3], client_login_password=sys.argv[4])
r6sconn.use(sid=1)
r6sconn.clientupdate(client_nickname=sys.argv[5])
print("Conncted!")
statThread = threading.Thread(target=r6s_statF)
statThread.start()
