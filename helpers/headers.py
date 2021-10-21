import os

token = os.environ['token']
token1 = os.environ['token1']
#token2 = os.environ['token2']
#token3 = os.environ['token3']



sProps = os.environ['sProps']
sProps1 = os.environ['sProps1']
#sProps2 = os.environ['sProps2']
#sProps3 = os.environ['sProps3']


referer = os.environ['referer']
referer1 = os.environ['referer1']
#referer2 = os.environ['referer2']
#referer3 = os.environ['referer3']


cookies = os.environ['cookies']
cookies1 = os.environ['cookies1']
#cookies2 = os.environ['cookies3']
#cookies3 = os.environ['cookies4']

headers = [{
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
},
{
    'authority': 'discordapp.com',
    'x-super-properties': f'{sProps1}',
    'origin': 'https://discordapp.com',
    'authorization': f'{token1}',
    'accept-language': 'en-US',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    'content-type': 'application/json',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': f"{referer1}",
    'accept-encoding': 'gzip, deflate, br',
    'cookie': f"{cookies1}",
}]