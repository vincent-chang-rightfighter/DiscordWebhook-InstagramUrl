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

#### line 10
Replace to your discord server webhook link
>替換成你的伺服器 webhook 連結
```py
webHookUrl = 'https://discord.com/api/webhooks/...'
```

#### line 11
Use imginn.org search instagram account id and replace this link
>用 imginn.org 搜尋 instagram 帳號並替換成該連結
```py
RequestUrl = "https://imginn.org/Accountid/"
```

#### line 56
Change webhook embed post author name and icon_url
>修改 webhook 嵌入的作者名字及作者icon
```py
embed.set_author(name='Accountid',icon_url='https://Accountid_icon.png')
```

#### line 60
Change webhook post content to your style
>修改 webhook 傳送內容成你的風格
```py
webhook.send( content=f"Accountid send a post\n{hyperLink}", embed=embed)
```