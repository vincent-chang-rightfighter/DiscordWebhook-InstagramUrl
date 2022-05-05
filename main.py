from urllib.request import Request
from bs4 import BeautifulSoup
import requests
import sqlite3
from discord import Webhook, RequestsWebhookAdapter, Embed

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

webHookUrl = 'https://discord.com/api/webhooks/...'
RequestUrl = "https://imginn.org/Accountid/"


def build_webhook():
    webhook = Webhook.from_url(webHookUrl, adapter=RequestsWebhookAdapter())
    return webhook


def main():
    con = sqlite3.connect('ig.db')
    cur = con.cursor()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS Stuff(url TEXT PRIMARY KEY NOT NULL)''')
    webhook = build_webhook()
    res = requests.get(RequestUrl, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    for item in soup.select('#wrapper > div.user-wrapper > div.post-items'):
        shorTcode = item.a.get('href')
        hyperLink = "https://www.instagram.com"+shorTcode
        exist = con.execute(
            "SELECT * FROM Stuff WHERE url = ?", ([hyperLink])).fetchone()
        if exist is None:
            # print(shorTcode)
            cur.execute(
                "INSERT INTO Stuff VALUES(?)", [hyperLink])
            con.commit()
            print(hyperLink)
            print("Not exist. Send webhook")
            embed = Embed()
            embed.url = hyperLink
            webhook.send(content=f"Accountid send a post\n{embed.url}")
            break
        else:
            print("Yep exists")
            break
    con.close()


if __name__ == "__main__":
    main()
