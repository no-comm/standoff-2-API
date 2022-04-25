import requests
def account(id):
    headers = {
        "Host": "store.standoff2.com",
        "Referer": "https://store.standoff2.com/",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    r = requests.get(f"https://store.standoff2.com/api/v1/accounts/{id}", headers=headers).json()
    name = r['name']
    avatar = r['avatar']
    return name, avatar
def avatar(url):
    f=open(r'../gg.webp', "wb")
    ufr = requests.get(url)
    f.write(ufr.content)
    f.close()