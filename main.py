from urllib.request import Request
from bs4 import BeautifulSoup
import requests
import sqlite3
from discord import Webhook, RequestsWebhookAdapter, Embed, Colour

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
        ImageMessage = item.find('img')['alt']
        hyperLink = "https://www.instagram.com"+shorTcode

        exist = con.execute(
            "SELECT * FROM Stuff WHERE url = ?", ([hyperLink])).fetchone()
        if exist is None:
            # print(shorTcode)
            cur.execute(
                "INSERT INTO Stuff VALUES(?)", [hyperLink])
            con.commit()
            print("Not exist. Send webhook\n"+str(hyperLink))
            res2 = requests.get("https://imginn.org" +
                                str(shorTcode), headers=headers)
            soup2 = BeautifulSoup(res2.text, 'lxml')
            for item in soup2.select('#wrapper > div.post-wrapper > div.content'):
                # Picture url
                # print(item.a.get('href')[:-5])
                if item.find("a", class_="video-wrap") is None:
                    imgurl = item.a.get('href')[:-5]
                elif item.find("a", class_="video-wrap") is not None:
                    imgurl = item.find("img")["src"]

            embed = Embed()
            embed.colour = Colour.blue()
            embed.set_image(url=imgurl)
            embed.set_author(name='Accountid',
                             icon_url='https://Accountid_icon.png')
            embed.description = ImageMessage
            embed.set_footer(
                text='Powered by vincent-chang-rightfighter/DiscordWebhook-InstagramUrl')
            webhook.send(
                content=f"Accountid send a post\n{hyperLink}", embed=embed)
            break
        else:
            print("Yep exists")
            break
    con.close()


if __name__ == "__main__":
    main()
