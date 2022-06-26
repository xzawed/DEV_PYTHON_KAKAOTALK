import requests
import json
from mysql import *

DB = MYSQL
url = 'https://kauth.kakao.com/oauth/token'
client_id = '80a5b2bd85b513d07198e52e8e192875'
redirect_uri = 'https://example.com/oauth'
code = DB.selmysql(self=DB, opt='TOKEN', data=('KAKAO', '80a5b2bd85b513d07198e52e8e192875'))

data = {
    'grant_type':'authorization_code',
    'client_id':client_id,
    'redirect_uri':redirect_uri,
    'code': code,
    }

response = requests.post(url, data=data)
tokens = response.json()

#발행된 토큰 저장
with open("token.json","w") as kakao:
    json.dump(tokens, kakao)
