import json
import requests
import random
import time
from helpers.headers import headers
from threading import Thread
from helpers.app import keep_alive
from helpers.notbot import sendMessage, sendM
from helpers.randomwords import words

keep_alive()
notbot = Thread(target=sendMessage).start()

nonce = "722789522290923712"


def generate_nonce(nonce):
    return str(int(nonce) + random.randint(1, 100))


def plsBeg():
    n = 0
    while True:
        sendM("pls beg")
        if n == 100:
            time.sleep(random.randint(60*60*3, 60*60*4))
        else:
            time.sleep(50)

def plsFish():
    n = 0
    while True:
        sendM("pls fish")
        if n == 100:
            time.sleep(random.randint(random.randint(60*60*3, 60*60*4), 60*60*4))
        else:
            time.sleep(50)

def plsHunt():
    n = 0
    while True:
        sendM("pls hunt")
        if n == 100:
            time.sleep(random.randint(60*60*3, 60*60*4))
        else:
            time.sleep(50)

def plsDig():
    n = 0
    while True:
        sendM("pls dig")
        if n == 100:
            time.sleep(random.randint(60*60*3, 60*60*4))
        else:
            time.sleep(50)

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
        for i in deposit:
            sendM(i)
            time.sleep(30)

save = Thread(target=depositItems).start()