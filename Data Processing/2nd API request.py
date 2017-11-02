import requests
from operator import itemgetter
import json
import pygal

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
#print("Status Code: ", r.status_code)

submission_ids = r.json()
submission_dicts = []

#print(submission_ids)

for submission_id in submission_ids[:15]:
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) +".json"
    r = requests.get(url)
    dict = r.json()
    submission_dict = {
        'title': dict['title'],
        'link': dict['url'],
        'comments': dict.get('descendants',0)
    }
    submission_dicts.append(submission_dict)

submission_dicts=sorted(submission_dicts,key = itemgetter('comments'),reverse = True )

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])