import requests
import pprint
import json
from datetime import datetime, timedelta

today = datetime.now()
yesterday = datetime.now() - timedelta(1)
print("today =", today)
print("yesterday =", yesterday)

# now = datetime.datetime.now()
# date = str(now)
# print(date[0:10])


string = "!stock AAPL"
newString = string.replace("!stock ", "", 1)
print(newString)

# Check to see if there was en error with the call
if response.json()["status"] == "ERROR":
    if response.json()["error"] == "today's Date not supported yet":
        # Make the call again but with yesterday's date
        yesterday = now - timedelta(2)
        stringYesterday = str(yesterday)
        newApiCall = "https://api.polygon.io/v1/open-close/" + stockSearch + "/" + stringYesterday[
                                                                                   0:10] + "?adjusted=true&apiKey=ox0cWEbdfMMTQTDO2reGQ9TaGpWf7ugp"
        newResponse = requests.get(newApiCall)
        # https://api.polygon.io/v1/open-close/AAPL/2021-10-02?adjusted=true&apiKey=ox0cWEbdfMMTQTDO2reGQ9TaGpWf7ugp
        # https://api.polygon.io/v1/open-close/AAPL/2020-10-14?adjusted=true&apiKey=ox0cWEbdfMMTQTDO2reGQ9TaGpWf7ugp
        print(newApiCall)
        print(newResponse.json())
        await message.channel.send(
            "Fucken early bird, you beat the market open. You should be asleep right now. It's people like"
            " you that keep me up programming shit like this. Here is yesterday's information you cunt")
        await message.channel.send("Open - " + newResponse.json()["open"] +
                                   "\nHigh - " + newResponse.json()["high"] +
                                   "\nLow - " + newResponse.json()["low"] +
                                   "\nClose - " + newResponse.json()["close"])

    else:
        await message.channel.send(response.json()["error"])

# Steam API Key EE2617D0CA6B2A2A5EDB583F07C86DD7