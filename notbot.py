import json
import requests
import random
import time
from headers import headers
from threading import Thread
import secrets
import string


channels = ["899940607802372116","899940625485533224","899940640845070357","899940655768412180"]


nonce = "722789522290923712"


def generate_nonce(nonce):
    return str(int(nonce) + random.randint(1, 100))

def sendMessage():
    while True:
        f = open("data.json")
        data = json.load(f)
        res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(random.randint(7,150)))
        data["content"] = res
        data["nonce"] = generate_nonce(nonce)
        data = json.dumps(data)
        r = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(random.choice(channels)), headers=headers, data=data)
        print("\nI said:",res)
        x = random.randint(10, 1500)
        print("sleeping for:", x)
        time.sleep(x)

def sendM(message:str):
    f = open("data.json")
    data = json.load(f)
    data["content"] = message
    data["nonce"] = generate_nonce(nonce)
    data = json.dumps(data)
    r = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(random.choice(channels)), headers=headers, data=data)