from flask import Flask
from flask import request
import requests
import facebook
import urllib
import httplib
from pymongo import MongoClient
import json
from httplib import HTTPResponse
#https://teamtreehouse.com/community/can-someone-help-me-understand-flaskname-a-little-better
app = Flask(__name__)
FACEBOOK_APP_ID = '188725925227536'
FACEBOOK_APP_SECRET = '76cf7f4e23189441ed6a416f99380a2c'

#client = MongoClient()
client = MongoClient("mongodb://SallyHabib1:Jesus2016@ds119810.mlab.com:19810/mylife")
db = client['mylife']
coll = db['facebook']
print(coll)

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

@app.route("/facebook")
def zozo():
    #here request is request of flask not the requests library and it return the attribute specified f
    code = request.args.get('code')

    # print(code)
    #Exchanging Code for an Access Token
    r=requests.get('https://graph.facebook.com/v2.12/oauth/access_token?client_id={}&redirect_uri={}&client_secret={}&code={}'.format(FACEBOOK_APP_ID,'http://localhost:8080/facebook',FACEBOOK_APP_SECRET,code))
    data = r.json()
    access_token=data['access_token']

    graph = facebook.GraphAPI(access_token)
    permissions=requests.get('https://graph.facebook.com/me/permissions?access_token='+access_token)
    permissionsJson=permissions.json()
    
    declined=[]
    print(json.dumps(permissions.json()))
    i = 0
    while i < len(permissionsJson['data']):
       #print(json.dumps(permissionsJson['data'][i]))
       if permissionsJson['data'][i]['status']=='declined':
            declined.append(permissionsJson['data'][i]['permission'])
       i += 1
    print(declined)
    # me is of type dictionary
    me= graph.request('/me?fields=id,name,email,birthday,age_range,posts')
    #print(permissions.json())
    id=me.get('id')
    if declined.__contains__('name'):
        print "yes"
    else:
        print "no"
    name=me.get('name')
    email=me.get('email')
    posts=me.get('posts')
    result = db.facebook.insert_one({
        "name":name,
        "email":email
      })

    print(name)
    friends= graph.request('/me/friends')
    #data_friends=friends['data']
    #print(me)
    #print(friends)
    #print(data_friends)

    return 'Done'


  
app.run(host="0.0.0.0", port=int("8080"), debug=True)

