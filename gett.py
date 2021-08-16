import requests
r=requests.get("https://google.com")
with open("class2.txt","w") as f2:
    f2.write(r.text)

