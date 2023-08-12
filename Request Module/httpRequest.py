import requests
# import antigravity

url = requests.get("https://imgs.xkcd.com/comics/python.png")
# print(url.text)

with open("luffy.png", 'wb') as f:
    f.write(url.content)