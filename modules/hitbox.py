import json
import requests

account = ""
password = ""


def get_auth():
    data = {"login": account, "pass": password, "app": "desktop"}
    url = 'https://api.hitbox.tv/auth/token'
    rep = requests.post(url, data=json.dumps(data))
    print rep.text
    json_data = json.loads(rep.text)
    return json_data["authToken"]


def get_streamKey(authKey):
    url = 'https://api.hitbox.tv/mediakey/'+account+'?authToken='+authKey
    rep = requests.get(url)
    print rep.text
    json_data = json.loads(rep.text)
    return json_data["streamKey"]


def reset_streamKey(authKey):
    url = 'https://api.hitbox.tv/mediakey/'+account+'?authToken='+authKey
    rep = requests.put(url)
    print rep.text
    json_data = json.loads(rep.text)
