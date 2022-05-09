from urllib.request import Request
from bs4 import BeautifulSoup
import requests
import sqlite3
from discord import Webhook, RequestsWebhookAdapter, Embed, Colour

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

webHookUrl = ['https://discord.com/api/webhooks/...AccountidA',
              'https://discord.com/api/webhooks/...AccountidB']
Instagram_Accounts_id = ['AccountidA', 'AccountidB']


def build_webhook(Webhookurl):
    webhook = Webhook.from_url(Webhookurl, adapter=RequestsWebhookAdapter())
    return webhook


def main(Webhookurl: str, InstagramAccountId: str):
    con = sqlite3.connect('ig.db')
    cur = con.cursor()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS Stuff(url TEXT PRIMARY KEY NOT NULL)''')
    webhook = build_webhook(Webhookurl)
    res = requests.get("https://imginn.org/" +
                       InstagramAccountId+"/", headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    for item in soup.select('#wrapper > div.user-wrapper > div.hd'):
        for ic in item.select('div.avatar'):
            iconUrl = ic.find("img")['src']
        for name in item.select('div.name'):
            Accountid = name.find("div").get_text() + \
                " ( " + name.h1.get_text()+" ) "
            Accountname = name.find("div").get_text()
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
                if item.find("a", class_="video-wrap") is None:
                    imgurl = item.a.get('href')[:-5]
                elif item.find("a", class_="video-wrap") is not None:
                    imgurl = item.find("img")["src"]

            embed = Embed()
            embed.colour = Colour.blue()
            embed.set_image(url=imgurl)
            embed.set_author(name=Accountid,
                             icon_url=iconUrl)
            embed.description = ImageMessage
            embed.set_footer(text='Powered by vincent-chang-rightfighter/DiscordWebhook-InstagramUrl',
                             icon_url='https://raw.githubusercontent.com/vincent-chang-rightfighter/DiscordWebhook-InstagramUrl/main/icon.png')
            webhook.send(
                content=f"{Accountname} send a post\n{hyperLink}", embed=embed)
            break
        else:
            print("Yep exists")
            break
    con.close()


if __name__ == "__main__":
    # main()
    for i in range(len(Instagram_Accounts_id)):
        main(webHookUrl[i], Instagram_Accounts_id[i])
