from flask import Flask
from flask import request
import requests
import facebook
import urllib
import httplib

import json
from httplib import HTTPResponse
#https://teamtreehouse.com/community/can-someone-help-me-understand-flaskname-a-little-better
app = Flask(__name__)
global r3
r3='ddd'
global resp
global data
data={}
global json_data
json_data = json.dumps(data)

@app.route("/")
def hello():
    #here request is request of flask not the requests library and it return the attribute specified f
    code = request.args.get('code')

    print(code)
    #r=requests.post('https://api.fitbit.com/oauth2/tokenAuthorization: Basic a15632dcdbebd9fab89d07a10783c8d0=Content-Type: application/x-www-form-urlencodedclient_id=22CMZV&grant_type=authorization_code&redirect_uri=http%3A%2F%2Flocalhost%3A8080&code={}'.format(code))
    url = 'https://api.fitbit.com/oauth2/token'
    payload = {
"clientId":"22CMZV",
"grant_type":"authorization_code",
"redirect_uri":"http://10.0.2.2:8080",
"code":code
    }
    

# Adding empty header as parameters are being sent in payload
    headers = {
        'Authorization': 'Basic MjJDTVpWOmExNTYzMmRjZGJlYmQ5ZmFiODlkMDdhMTA3ODNjOGQw',
        'Content-Type': 'application/x-www-form-urlencoded' 
   }
    r = requests.post(url, params=payload, headers=headers)
    data=r.json()
    #print(r.content)
    # g=data['content'][0]
    access_token=data['access_token']
    print(access_token)
    
    headers1 = {
        'Authorization': 'Bearer '+ access_token
   }
   
    
    r2 = requests.get('https://api.fitbit.com/1/user/-/profile.json', headers=headers1)
    resp=r2
    #print(r2.content)
    data2=r2.json()
    user=data2['user']
    #HTTPResponse(json.dumps(r2.json()))
    #print(user)
    global data 
    global json_data
    data['key'] = user
    json_data = json.dumps(data)
    print(json_data)

    return json.dumps(r2.json())

    #debug=True print out errors on the web page

@app.route("/response")
def response():
 
  print(json_data)
  return json_data

  
app.run(host="0.0.0.0", port=int("8080"), debug=True)

