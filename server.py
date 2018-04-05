from flask import Flask
from flask import request
import requests
import facebook
from pymongo import MongoClient
import json
import csv
import nltk
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import  WordNetLemmatizer as wnl
from nltk.corpus import wordnet as wn
from nltk.tokenize import TweetTokenizer
import re
import string
import codecs

app = Flask(__name__)
FACEBOOK_APP_ID = '188725925227536'
FACEBOOK_APP_SECRET = '76cf7f4e23189441ed6a416f99380a2c'

#client = MongoClient()
client = MongoClient("mongodb://SallyHabib1:Jesus2016@ds119810.mlab.com:19810/mylife")
db = client['mylife']
coll = db['facebook']
#print(coll)

global resp
global data
data={}
global json_data
json_data = json.dumps(data)

@app.route("/")
def hello():
    #here request is request of flask not the requests library and it return the attribute specified f
    code = request.args.get('code')

    #print(code)
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
    if(data.__contains__("access_token")):
        access_token=data['access_token']
        print(access_token)
        
        headers1 = {
            'Authorization': 'Bearer '+ access_token
    }
    
        
        r2 = requests.get('https://api.fitbit.com/1/user/-/profile.json', headers=headers1)
        resp=r2
        #print(r2.content)
        data2=r2.json()
        if(data2.__contains__("user")):

            user=data2['user']
            
            global data 
            global json_data
            data['key'] = user
            json_data = json.dumps(data)
            #print(json_data)

        return json.dumps(r2.json())
    else:
        return "you donot provide the app with needed permissions"

    #debug=True print out errors on the web page

@app.route("/response")
def response():
    user_id2 = request.args.get('database_id')
    print(str(user_id2)+"here")
    if(data.__contains__("key")):
        key=data.get("key")
        print("key")

        if(key.__contains__("fullName")):
            fullName=key.get("fullName")
        else:
            fullName=""

        if(key.__contains__("dateOfBirth")):
            birthdayFitness=key.get("dateOfBirth")
        else:
            birthdayFitness=""

        if(data.__contains__("user_id")):
            client_id=data.get("user_id")
        else:
            client_id=""

        if(key.__contains__("height")):
            height=key.get("height")
            heightString=str(height)
        else:
            heightString=""

        if(key.__contains__("weight")):
            weight=key.get("weight")
            weightString=str(weight)
        else:
            weightString=""
            
        db.fitness.update_one({"user_ID":user_id2},{
        "$set":{
            "client_id":client_id,
            "name":fullName,
            "birthday":birthdayFitness,
            "height":heightString,
            "weight":weightString,
            "user_ID":str(user_id2)
        }}
        ,  upsert=True )

    #print(json_data)
    return json_data

@app.route("/facebook")
def zozo():
    #here request is request of flask not the requests library and it return the attribute specified f
    code = request.args.get('code')

    # print(code)
    #Exchanging Code for an Access Token
    r=requests.get('https://graph.facebook.com/v2.12/oauth/access_token?client_id={}&redirect_uri={}&client_secret={}&code={}'.format(FACEBOOK_APP_ID,'http://localhost:8080/facebook',FACEBOOK_APP_SECRET,code))
    dataFacebook = r.json()
    if(dataFacebook.__contains__("access_token")):

        access_token=dataFacebook['access_token']
        #print(access_token)

        graph = facebook.GraphAPI(access_token)
        permissions=requests.get('https://graph.facebook.com/me/permissions?access_token='+access_token)
        permissionsJson=permissions.json()
        
        declined=[]
        #print(json.dumps(permissions.json()))
        i = 0
        while i < len(permissionsJson['data']):
            #print(json.dumps(permissionsJson['data'][i]))
            if permissionsJson['data'][i]['status']=='declined':
                declined.append(permissionsJson['data'][i]['permission'])
            i += 1
        print(declined)
        # me is of type dictionary
        me= graph.get_object('/me?fields=id,name,likes.limit(10){about,name},posts.since(2017).limit(10){story,with_tags,created_time,message},birthday,email')
        #print(permissions.json())
        id=me['id']
        if declined.__contains__('name'):
            name = ""
        else:
            if(me.__contains__("name")):
                name = me['name']
            else:
                name=""
                
        if declined.__contains__('user_birthday'):
            bd=""
        else:
            if(me.__contains__("birthday")):
                bd=me['birthday']  
            else:
                bd="" 
        
        if declined.__contains__('user_posts'):
            posts=""  
        else:
            if(me.__contains__("posts")):
                posts=me['posts']
                p=posts['data']
            else:
                posts=""

        if declined.__contains__('user_likes'):
            likes=""  
        else:
            if(me.__contains__("likes")):
                likes=me['likes']
                l=likes['data']
                #print(json.dumps(l))
            else:
                likes=""
        
        if(me.__contains__("email")):
            email=me['email']
        else:
            email=""
        

        db.facebook.update_one({"_id":id},{
            "$set":{
            "_id":id,
            "name":name,
            "email":email,
            "birthday":bd
        }},  upsert=True)

    # postsJson=posts.json()
        

        #print(json.dumps(p))
        if(me.__contains__("posts")):
            j = 0
            while j < len(p):

                message= p[j].get("message", "empty")
                story =  p[j].get("story", "empty")
                tags=[]
                if(p[j].__contains__('with_tags')):
                    withTagCount=0
                    while(withTagCount<len(p[j]['with_tags']['data'])):
                        # name=posts['data'][postCount].get("with_tags")[withTagCount].get("name")
                        name=p[j]['with_tags']['data'][withTagCount].get("name")
                        idTag=p[j]['with_tags']['data'][withTagCount].get("id")
                        if(~(tags.__contains__(idTag))):
                            tags.append(idTag)
                        withTagCount+=1

                if(story=="empty"):
                    db.posts.update_one({"_id": p[j].get("id")},{
                        "$set": {
                        "_id": p[j].get("id"),
                        "message": message ,
                        "story": "below",
                        "created_time": p[j].get("created_time"),
                        "users_id": id,
                        "tags":tags
                    }},  upsert=True)

                elif(message=="empty"):
                    db.posts.update_one({"_id": p[j].get("id")},{
                        "$set": {
                        "_id": p[j].get("id"),
                        "message": "below",
                        "story": story,
                        "created_time": p[j].get("created_time"),
                        "users_id": id,
                        "tags":tags
                    }},  upsert=True)
                
                else:
                    db.posts.update_one({"_id": p[j].get("id")},{
                        "$set": {
                        "_id": p[j].get("id"),
                        "message": message,
                        "story": story,
                        "created_time": p[j].get("created_time"),
                        "users_id": id,
                        "tags":tags
                    }},  upsert=True)
                        
                #print(json.dumps(p[j]))
                j += 1
        else:
            posts=""
        if(me.__contains__("likes")):
            k=0
            while k < len(l):
                likeName=l[k].get("name","empty")
                about=l[k].get("about","empty")
                if (likeName=="empty"):

                    db.likes.update_one({"_id": l[k].get("id")},{
                        "$set":{
                        "_id":l[k].get("id"),
                        "name":"",
                        "about":about,
                        "user_id":id
                    }},  upsert=True)
                
                elif(about=="empty"):
                    db.likes.update_one({"_id": l[k].get("id")},{
                        "$set":{
                        "_id":l[k].get("id"),
                        "name":likeName,
                        "about":"",
                        "user_id":id
                    }},  upsert=True)
                
                else:
                    db.likes.update_one({"_id": l[k].get("id")},{
                        "$set":{
                        "_id":l[k].get("id"),
                        "name":likeName,
                        "about":about,
                        "user_id":id
                    }},  upsert=True) 

                k+=1
         
                print(k)
        else:
            likes=""  

        return 'Done'
    else:
        return 'please provide app with needed permissions'
        
export= db.posts.find()
out= csv.writer(open('some.csv', 'wb'),delimiter=(','))
b=[]
a=[]
for items in export:
    a.append(items['story'].encode("utf-8").strip())
    a.append(items['message'].encode("utf-8").strip())
    a.append(items['created_time'].encode("utf-8").strip())
    b.append(a)
    out.writerows(b)
    a=[]
    b=[]

  
app.run(host="0.0.0.0", port=int("8080"), debug=True, threaded=True)