# DiscordWebhook-InstagramUrl

## Usage
1. Install dependencies - `python3 -m pip install -r requirements.txt`

>安裝依賴 - `python3 -m pip install -r requirements.txt`

2. Modify main.py file 

>修改 main.py 檔案

3. Run the script - `sh run.sh` 

>執行腳本 `sh run.sh` 

this script run main.py 5 minutes again
>此腳本每5分鐘執行1次

## Configuration

### Modify main.py 

#### line 10 & line 12

Replace to your discord server webhook link
>替換成你的伺服器 webhook 連結
```py
webHookUrl = ['https://discord.com/api/webhooks/...AccountidA',
              'https://discord.com/api/webhooks/...AccountidB']
```

Use imginn.org search instagram account id and replace it
>用 imginn.org 搜尋 instagram 帳號並替換成它
```py
Instagram_Accounts_id = ['AccountidA', 'AccountidB']
```
A webhook to receive an IG account
Increase or decrease according to the number of IG accounts
The following relation table is for reference.

|IG Account| Webhook|
|---|---|
|AccountidA|https://discord.com/api/webhooks/...AccountidA|
|AccountidB|https://discord.com/api/webhooks/...Accountidb|

#### line 67
Change webhook post content to your style
>修改 webhook 傳送內容成你的風格
```py
webhook.send( content=f"{Accountname} send a post\n{hyperLink}", embed=embed)
```