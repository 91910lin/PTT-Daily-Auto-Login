import json
from PTTLibrary import PTT

try:
    with open('D:/PTT/file.json') as AccountFile:
        Account = json.load(AccountFile)
        username = Account['username']
        password = Account['password']
except FileNotFoundError:
    print("Please make sure the account file exists.")
    exit()
PTTBot = PTT.Library()
PTTBot.login(username, password)

PTTBot.logout()
