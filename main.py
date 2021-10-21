import json
import requests
import random
import time
from helpers.headers import headers
from threading import Thread
from helpers.app import keep_alive
from helpers.notbot import sendMessage, sendM
from helpers.randomwords import words

print("Script is started...")

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
    "pls give <@898853543375683595> 99k",
    "pls sell stickbug all",
    "pls sell skunk all",
    "pls sell seaweed all",
    "pls sell deer all",
    "pls sell duck all",
    "pls sell boar all",
    "pls sell fish all",
    "pls sell rarefish all",
    "pls sell exoticfish all",
    "pls sell jellyfish all"
    "pls sell rabbit all",
    "pls sell garbage all",
    "pls sell sand all",
    "pls sell worm all",
    "pls sell junk all"
]

def depositItems():
    while True:
        for i in deposit:
            sendM(i)
            print(i)
            time.sleep(30)

save = Thread(target=depositItems).start()

print("Script started successfully...")