import requests

find=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
id_data=find.json()
number=123
print(id_data["data"])
#for i in range(len(id_data["data"])):
 #   print(id_data["data"][i]["id"])
#a={"id":123,"money":555}
#id_data["data"].append(a)
#update=requests.put('https://jsonstorage.net/api/items/',params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},
#        json=id_data)

