from datetime import datetime
import csv
with open('user_posts_1641812829207516.csv') as File:
    tfidfReader = csv.reader(File)
    i=1
    for row in tfidfReader:
        datetime_object = datetime.strptime(row[3][:-4],"%Y-%m-%dT%H:%M:%S+")
        month=datetime_object.month
        year=datetime_object.year
        day=datetime_object.day
        hour=datetime_object.hour
        minute=datetime_object.minute
        sec=datetime_object.second
        #print(datetime.today())
        zozo=datetime(year, month, day)
        print(zozo.weekday())
        i+=1
        