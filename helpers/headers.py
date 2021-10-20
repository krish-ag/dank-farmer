import os

token = os.environ['token']

sProps = os.environ['s-props']

referer = os.environ['referer']

cookies = os.environ['cookies']

headers = {
    'authority': 'discordapp.com',
    'x-super-properties': f'{sProps}',
    'origin': 'https://discordapp.com',
    'authorization': f'{token}',
    'accept-language': 'en-US',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    'content-type': 'application/json',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': f"{referer}",
    'accept-encoding': 'gzip, deflate, br',
    'cookie': f"{cookies}",
}