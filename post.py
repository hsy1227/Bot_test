import requests

data={'api_dev_key': '8c908cb27f27a3b870f7cf7991f61fd4',
        'api_paste_format': 'python',
        'api_option': 'paste',
        'api_paste_code':'hello'}
r=requests.post("https://pastebin.com/api/api_post.php",data=data)
print(r.text)
