import requests
import json

r=requests.get('http://api.open-notify.org/iss-now.json')
r_json=json.loads(r.text)
latitude=r_json['iss_position']['latitude']
longitude=r_json['iss_position']['longitude']

print(f"{latitude}  {longitude}")
