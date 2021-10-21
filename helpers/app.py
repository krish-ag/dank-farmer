from flask import Flask
from threading import Thread
import logging, click


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def secho(text, file=None, nl=None, err=None, color=None, **styles):
    pass

def echo(text, file=None, nl=None, err=None, color=None, **styles):
    pass

click.echo = echo
click.secho = secho

app = Flask('')

@app.route('/')
def home():
    return "Working bruh"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()