import os

#token = os.environ['token']
token = "OTAwMjc3MDA2NzI0Mzg2ODI2.YW--1g.vmNzAfQ6uxW2Iyoofq2Cmr7zrT0"

#sProps = os.environ['s-props']
sProps = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk0LjAuNDYwNi44MSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTQuMC40NjA2LjgxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2JvYXJkLm9yZy8iLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzYm9hcmQub3JnIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwMTQ1MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

#referer = os.environ['referer']
referer = "https://discord.com/channels/900277119807000606/900277119807000609"

#cookies = os.environ['cookies']
cookies = "__dcfduid=b8e498c0510cb8d38ff7e8cc2e97f27a; _ga=GA1.2.934111061.1627328775; __sdcfduid=87799680f44711eb957a798ddcdb995e7fd772bda3c7427c64f661c313171b0468bde5af9573dcc61cd3669631f1129a; __stripe_mid=dc7149a1-7e32-4064-b4de-038afebce8b28225a3; OptanonConsent=isIABGlobal=false&datestamp=Fri+Oct+08+2021+13%3A58%3A07+GMT%2B0530+(India+Standard+Time)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false"

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