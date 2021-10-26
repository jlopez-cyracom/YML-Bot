# import os
from datetime import datetime, timedelta
import random
import discord
import requests
from dotenv import load_dotenv

load_dotenv()
# Need to figure out how to work with .env to hide TOKEN & GUILD before release
TOKEN = 'ODk3MjU0MjYyNTUwMTY3NTcz.YWS_Jg.DOvRR_d8A0mO7FqPqiEKtJNfFVY'
GUILD = 'Test Server'

client = discord.Client()

# Users Dictionary
users = {
    "JesuSwag": 477280220890660894,
    "Femtoz": 382351636997341185,
    "Jalsonio": 510919516306407446,
    "angelqb23": 383097211262730250,
    "iuni": 165998316339855360
}

# Text channel dictionary
textChannel = {
    "YML": 382335548393783298,
    "Test Server": 897253083942375477
}

tts_voice = ["Shut the fuck up Psycho Pits", "Nobody cares what you have to say", "You're so gay",
             "Doesn't matter......you have a small P P", "Talk to the hand", "How the fuck do we mute this bitch?",
             "Go back to panama", "Suck...my...toe", "Shut up you herald MMR"]

about = "My name is Bully Bot! My sole purpose is to bully Femtoz AKA Femtitz. I can execute a couple commands and more to come!"\
    "I really enjoy what I do and has always been my life passion since I was born in early October of 2021."

# Features to add:
# PM message to directly bully Psycho pits
# Retrieve price for specific ticker
# Retrieve a random indie game to try


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # await client.get_channel(textChannel["YML"]).send("Hi, I have arrived! Try typing '!help'")
    await client.get_channel(textChannel["Test Server"]).send("Hi, I have arrived! Try typing '!help'")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == users["Femtoz"]:
        await message.channel.send(random.choice(tts_voice), tts=True, delete_after=5)
    # elif message.author.id == users["Femtoz"]:
    #     await message.channel.send("No....Fuck you!", tts=True)

    # if message.author.id == users["Femtoz"] and "fuck you" or "fuck u" in message.content.lower():
    #     await message.channel.send("No....Fuck you!", tts=True)
    # elif message.author.id == users["Femtoz"]:
    #     await message.channel.send(random.choice(tts_voice), tts=True, delete_after=5)

# -------------------------------------------- Commands ----------------------------------------------------------------
    if message.content.startswith("!help"):
        await message.channel.send("AVAILABLE COMMANDS\n"
                                   "----------------------------------------------"
                                   "\n **!help** - Do I really need to tell you what this does?"
                                   "\n **!about** - Want to know more about me?"
                                   "\n **!bullyFemtits** - Send a message to Femtoz that he will absolutely LOVE"
                                   "\n **!stock {ticker}** - Shows the Open, High, Low and Close of the specified ticker\n"
                                   "\nCOMING SOON\n"
                                   "----------------------------------------------"
                                   "\n**!crypto {coin}** - Show the Open, High, Low and Close of the specified coin"
                                   "\n**!newGame** - When you don't know what to play and are willing to buy a new cheap game"
                                   "\n**!newGameCoop** - In case you don't like to try new games alone"
                                   "\n**!randomGame** - Becasue we all have huge steam libraries and can never decide what to play, this will choose one for you")

    if message.content.startswith("!about"):
        await message.channel.send(about)

    if message.content.startswith("!bullyFemtits"):
        await message.channel.send(random.choice(tts_voice), tts=True)

    # Detecting a ticker and sending an API call to find the OPEN/CLOSE for that ticker
    if message.content.startswith("!stock "):
        # --------------------- Grab the last valid date to use in API call ---------------------
        yesterday = datetime.now() - timedelta(1)
        if yesterday.weekday() == 5:
            yesterday -= timedelta(1)
        elif yesterday.weekday() == 6:
            yesterday -= timedelta(2)
        validDate = str(yesterday)  # Casting to string

        # --------------------- Grabbing the ticker from the command ---------------------
        ticker = message.content.replace("!stock ", "")

        # --------------------- Make the call ---------------------
        apiCall = "https://api.polygon.io/v1/open-close/" + ticker.upper() + "/" + validDate[0:10] +"?adjusted=true&apiKey=ox0cWEbdfMMTQTDO2reGQ9TaGpWf7ugp"
        response = requests.get(apiCall)

        print(apiCall)
        print(response.json())

        # --------------------- Error handling for different status responses ---------------------
        # *******Implement status codes instead of strings
        status = response.status_code
        if status == 404:
            await message.channel.send("The ticker you searched for is not supported/invalid: " + str(response.json()["message"]))
        elif status == 200:
            await message.channel.send("-----------------------" +
                                       "\n             " + ticker.upper() +
                                       "\n-----------------------" +
                                       "\n* ᴰᵘᵉ ᵗᵒ ᵗʰᵉ ⁿᵃᵗᵘʳᵉ ᵒᶠ ᵗʰᵉ ˢᵒᵘʳᶜᵉ ᵒᶠ ᵗʰᵉ ⁱⁿᶠᵒʳᵐᵃᵗⁱᵒⁿ, ᵗʰᵉ ⁿᵘᵐᵇᵉʳˢ ʸᵒᵘ ˢᵉᵉ ᵃʳᵉ ᵇᵃˢᵉᵈ ᵒⁿ ᵗʰᵉ ˡᵃˢᵗ ᵛᵃˡⁱᵈ ᵗʳᵃᵈⁱⁿᵍ ᵈᵃᵗᵉ" +
                                       "\nOpen - " + str(response.json()["open"]) +
                                       "\nHigh - " + str(response.json()["high"]) +
                                       "\nLow - " + str(response.json()["low"]) +
                                       "\nClose - " + str(response.json()["close"])
                                       )
        # --------------------- Formulate the message that is going to be sent ---------------------
        else:
            await message.channel.send("You should never see this...if you do, you royaly fucked up haha")

    if message.content.startswith("!crypto "):
        today = str(datetime.now())
        ticker = message.content.replace("!crypto ", "")
        apiCall = "https://api.polygon.io/v1/open-close/crypto/" + ticker.upper() + "/USD/" + today[0:10] + "?adjusted=true&apiKey=ox0cWEbdfMMTQTDO2reGQ9TaGpWf7ugp"
        response = requests.get(apiCall)
        jsonResponse = response.json()

        print(apiCall)
        print(jsonResponse)

        await message.channel.send("-----------------------" +
                                   "\n             " + ticker.upper() +
                                   "\n-----------------------" +
                                   "\n* ᴰᵘᵉ ᵗᵒ ᵗʰᵉ ⁿᵃᵗᵘʳᵉ ᵒᶠ ᵗʰᵉ ˢᵒᵘʳᶜᵉ ᵒᶠ ᵗʰᵉ ⁱⁿᶠᵒʳᵐᵃᵗⁱᵒⁿ, ᵗʰᵉ ⁿᵘᵐᵇᵉʳˢ ʸᵒᵘ ˢᵉᵉ ᵃʳᵉ ᵇᵃˢᵉᵈ ᵒⁿ ᵗʰᵉ ˡᵃˢᵗ ᵛᵃˡⁱᵈ ᵗʳᵃᵈⁱⁿᵍ ᵈᵃᵗᵉ" +
                                   "\nOpen - " + str(jsonResponse["open"]) +
                                   "\nHigh - " + str(jsonResponse["high"]) +
                                   "\nLow - " + str(jsonResponse["low"]) +
                                   "\nClose - " + str(jsonResponse["close"])
                                   )

    # How to send DM's
    if message.content.startswith("!test"):
        await message.author.send("Test Message for PM Messaging")

client.run(TOKEN)
