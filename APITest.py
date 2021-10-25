import requests
import pprint
import json
import datetime

now = datetime.datetime.now()
date = str(now)
print(date[0:10])



#response = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=EE2617D0CA6B2A2A5EDB583F07C86DD7&format=json")

# data = response.json()
# with open("steamLibraryComplete.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)

#pprint.pprint(response.json())

# Steam API Key EE2617D0CA6B2A2A5EDB583F07C86DD7


# print("--------")
# print("  Open \n--------")
# print(response.json()["open"])
# print("")
#
# print("--------")
# print("  Close \n--------")
# print(response.json()["close"])
# print("")
#
# print("--------")
# print("  High \n--------")
# print(response.json()["high"])
# print("")
