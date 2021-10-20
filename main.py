import json
import requests
import random
import time
from headers import headers
from threading import Thread
from app import keep_alive
from notbot import sendMessage, sendM
from randomwords import words

keep_alive()
notbot = Thread(target=sendMessage).start()


COMMANDS = [("pls beg", 50), ("pls fish", 50), ("pls hunt", 50),
            ("pls dig", 50)]

channel_url = 'https://discordapp.com/api/v6/channels/{}/messages'.format(
    str(873122878319636490))
nonce = "722789522290923712"


def generate_nonce(nonce):
    return str(int(nonce) + random.randint(1, 100))


def plsBeg():
    n = 0
    while True:
        f = open("data.json")
        data = json.load(f)
        data["content"] = COMMANDS[0][0]
        data["nonce"] = generate_nonce(nonce)
        data = json.dumps(data)
        r = requests.post(channel_url, headers=headers, data=data)
        print("Executed: ", COMMANDS[0][0])
        n += 1
        if n == 30:
            time.sleep(random.randint(900, 1500))
        else:
            time.sleep(COMMANDS[0][1])

def plsFish():
    n = 0
    while True:
        f = open("data.json")
        data = json.load(f)
        data["content"] = COMMANDS[1][0]
        data["nonce"] = generate_nonce(nonce)
        data = json.dumps(data)
        r = requests.post(channel_url, headers=headers, data=data)
        print("Executed: ", COMMANDS[1][0])
        n += 1
        if n == 30:
            time.sleep(random.randint(900, 1500))
        else:
            time.sleep(COMMANDS[1][1])

def plsHunt():
    n = 0
    while True:
        f = open("data.json")
        data = json.load(f)
        data["content"] = COMMANDS[2][0]
        data["nonce"] = generate_nonce(nonce)
        data = json.dumps(data)
        r = requests.post(channel_url, headers=headers, data=data)
        print("Executed: ", COMMANDS[2][0])
        n += 1
        if n == 30:
            time.sleep(random.randint(900, 1500))
        else:
            time.sleep(COMMANDS[2][1])

def plsDig():
    n = 0
    while True:
        f = open("data.json")
        data = json.load(f)
        data["content"] = COMMANDS[3][0]
        data["nonce"] = generate_nonce(nonce)
        data = json.dumps(data)
        r = requests.post(channel_url, headers=headers, data=data)
        print("Executed: ", COMMANDS[3][0])
        n += 1
        if n == 30:
            time.sleep(random.randint(900, 1500))
        else:
            time.sleep(COMMANDS[3][1])

beg = Thread(target=plsBeg).start()
time.sleep(5)
fish = Thread(target=plsFish).start()
time.sleep(5)
hunt = Thread(target=plsHunt).start()
time.sleep(5)
dig = Thread(target=plsDig).start()

deposit = [
    "pls gift 1 bank <@898853543375683595>",
    "pls gift 1 bank <@898853543375683595>",
    "pls gift 1 bank <@898853543375683595>",
    "pls give all <@898853543375683595>",
    "pls gift 3 shovel <@898853543375683595>",
    "pls gift 1 stickbug <@898853543375683595>",
    "pls gift 4 skunk <@898853543375683595>",
    "pls gift 5 seaweed <@898853543375683595>",
    "pls gift 2 deer <@898853543375683595>",
    "pls gift 2 duck <@898853543375683595>",
    "pls gift 2 boar <@898853543375683595>",
    "pls gift 30 fish <@898853543375683595>",
    "pls gift 3 rarefish <@898853543375683595>",
    "pls gift 2 exoticfish <@898853543375683595>",
    "pls gift 5 rabbit <@898853543375683595>",
    "pls gift 15 garbage <@898853543375683595>",
    "pls gift 5 sand <@898853543375683595>",
    "pls gift 10 worm <@898853543375683595>",
    "pls gift 10 junk <@898853543375683595>"
]

def depositItems():
    while True:
        time.sleep(600)
        print("saving progress")
        for i in deposit:
            f = open("data.json")
            data = json.load(f)
            data["content"] = i
            data["nonce"] = generate_nonce(nonce)
            data = json.dumps(data)
            r = requests.post(channel_url, headers=headers, data=data)
            time.sleep(20)

def actLikeHuman():
    n = 0
    while True:
        lenght = random.randint(1,20)
        sentence = ""
        for i in range(lenght):
            sentence += random.choice(words) + " "
        
        sendM(sentence)
        print("I said:", sentence)
        n += 1
        if n != 60:
            time.sleep(random.randint(10, 100))
        else:
            n = 0
            time.sleep(random.randint(1500,3000))

save = Thread(target=depositItems).start()
acthuman = Thread(target=actLikeHuman).start()
print("---------------------end-------------------------")