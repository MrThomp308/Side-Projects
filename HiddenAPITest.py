import requests

def GetUsers():
    url = "https://onlyfans.com/api2/v2/subscriptions/subscribes"

    querystring = {"offset":"0","type":"active","sort":"desc","field":"expire_date","limit":"10"}

    payload = ""
    headers = {
        "cookie": "csrf=78OzzWwg58a83da7634c611d8adce18cfa232acc; fp=fa76fc4e05106ce3766f6e3255a0ecb4; sess=6m2ef7ootttov7589dqk4pjfpp; auth_id=276944659; ref_src=https^%^3A^%^2F^%^2Faccounts.youtube.com^%^2F; st=a22625c67c613d8da7152ed3fe8f86bd352005d5e66f120bc69bebb48b8b6921; cookiesAccepted=true",
        "authority": "onlyfans.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "app-token": "33d57ade8c02dbc5a333db99ff9ae26a",
        "dnt": "1",
        "referer": "https://onlyfans.com/my/subscriptions/active?order_field=expire_date",
        "sec-ch-ua": "^\^Google",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sign": "5655:0c33379ee14533aeca6d52b838d536117cf496c7:a9b:636a156f",
        "time": "1667928194546",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "user-id": "276944659",
        "x-bc": "e71f1f10a9b3c73ac783f471ff6fd07b3446664d"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)

def GetMedia():

    url = "https://onlyfans.com/api2/v2/users/24212759/posts"

    querystring = {"limit":"10","order":"publish_date_desc","skip_users":"all","pinned":"0","format":"infinite"}

    payload = ""
    headers = {
        "cookie": "csrf=78OzzWwg58a83da7634c611d8adce18cfa232acc; fp=fa76fc4e05106ce3766f6e3255a0ecb4; sess=6m2ef7ootttov7589dqk4pjfpp; auth_id=276944659; ref_src=https^%^3A^%^2F^%^2Faccounts.youtube.com^%^2F; st=a22625c67c613d8da7152ed3fe8f86bd352005d5e66f120bc69bebb48b8b6921; cookiesAccepted=true",
        "authority": "onlyfans.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "app-token": "33d57ade8c02dbc5a333db99ff9ae26a",
        "dnt": "1",
        "referer": "https://onlyfans.com/badgirlblair",
        "sec-ch-ua": "^\^Google",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sign": "5655:5560f018d759eb8e16e73d160fddd881b768b2f3:b84:636a156f",
        "time": "1667926772173",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "user-id": "276944659",
        "x-bc": "e71f1f10a9b3c73ac783f471ff6fd07b3446664d"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)