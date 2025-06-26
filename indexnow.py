import requests

data = {
    "host": "www.sprunkr.online/",
    "key": "e98cb211bb2b449fa04f59acc629bc6c",
    "keyLocation": "https://sprunkr.online/e98cb211bb2b449fa04f59acc629bc6c.txt",
    "urlList": [
        "https://sprunkr.online/dadish"

    ]
}

response = requests.post(
    "https://api.indexnow.org/IndexNow",
    json=data,
    headers={"Content-Type": "application/json; charset=utf-8"}
)

print("状态码：", response.status_code)
print("返回内容：", response.text)