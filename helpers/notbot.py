import json
import requests
import random
import time
from helpers.headers import headers
from threading import Thread
import secrets
from helpers.randomwords import words
import string


channels = ["900277119807000609","900296982332067841","900296996085174292","900297007585955840","900297031032127489","900277282998980661","900301547613847552","900301558191910923","900301568178544650","900301578353901569","900277339794059267","900301745966698497","900301756418908160","900301766204223500","900301776333451274","900277445675061261","900301924782460958","900301934949445632","900301946597031976","900301957766479932"]


nonce = "722789522290923712"


def generate_nonce(nonce):
    return str(int(nonce) + random.randint(1, 100))

def sendM(message:str, channel=False):
    f = open("helpers/data.json")
    data = json.load(f)
    data["content"] = message
    data["nonce"] = generate_nonce(nonce)
    data = json.dumps(data)
    try:
        r = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(random.choice(channels) if not channel else channel), headers=random.choice(headers), data=data)
    except Exception:
        print("Exception")

def sendMessage():
    n = 0
    while True:
        mLen = random.randint(1,30)
        message = ""
        for i in range(1, mLen):
            message += random.choice(words) + ""
        sendM(message=message)
        n += 1
        if n == 100:
            time.sleep(random.randint(60*60*3, 60*60*4))
        else:
            time.sleep(random.randint(30, 200))