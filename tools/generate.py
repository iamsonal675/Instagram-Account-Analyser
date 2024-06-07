# This will Generate dumpy instagram data for Experimenting this tool 

from faker import Faker
from time import time
from json import dump
from random import choice

fake = Faker()

def get_data():
    first:str = fake.first_name()
    last:str = fake.first_name()
    name:str = first+last
    id:str = f"https://www.instagram.com/{name}"
    a = int(time())
    return {
          "title": "",
          "media_list_data": [
               
          ],
          "string_list_data": [
          {
               "href": id,
               "value": name,
               "timestamp": a
          }
          ]
     }

def hide_story_from(lst:list, iter:int)->list:
     new:list = []
     final:list = [{"relationships_hide_stories_from":[]}]
     for _ in range(0,iter,1):
          a = choice(lst)
          res = a
          new.append(res)
     for i in new:
          final[0]["relationships_hide_stories_from"].append(i)
     return final

def blocked_accounts(lst:list, iter:int)->list:
     new:list = []
     final:list = [{"relationships_blocked_users":[]}]
     for _ in range(0,iter,1):
          a = choice(lst)
          res = a
          new.append(res)
     for i in new:
          final[0]["relationships_blocked_users"].append(i)
     return final

def close_friends(lst:list, iter:int)->list:
     new:list = []
     final:list = [{"relationships_close_friends":[]}]
     for _ in range(0,iter,1):
          a = choice(lst)
          res = a
          new.append(res)
     for i in new:
          final[0]["relationships_close_friends"].append(i)
     return final

def pending_follow_requests(lst:list, iter:int)->list:
     new:list = []
     final:list = [{"relationships_follow_requests_sent":[]}]
     for _ in range(0,iter,1):
          a = choice(lst)
          res = a
          new.append(res)
     for i in new:
          final[0]["relationships_follow_requests_sent"].append(i)
     return final

def recent_follow_requests(lst:list, iter:int)->list:
     new:list = []
     final:list = [{"relationships_permanent_follow_requests":[]}]
     for _ in range(0,iter,1):
          a = choice(lst)
          res = a
          new.append(res)
     for i in new:
          final[0]["relationships_permanent_follow_requests"].append(i)
     return final

def recently_unfollowed_accounts(lst:list, iter:int)->list:
     new:list = []
     final:list = [{"relationships_unfollowed_users":[]}]
     for _ in range(0,iter,1):
          a = choice(lst)
          res = a
          new.append(res)
     for i in new:
          final[0]["relationships_unfollowed_users"].append(i)
     return final

def removed_suggestions(lst:list, iter:int)->list:
     new:list = []
     final:list = [{"relationships_dismissed_suggested_users":[]}]
     for _ in range(0,iter,1):
          a = choice(lst)
          res = a
          new.append(res)
     for i in new:
          final[0]["relationships_dismissed_suggested_users"].append(i)
     return final

def restricted_accounts(lst:list, iter:int)->list:
     new:list = []
     final:list = [{"relationships_restricted_users":[]}]
     for _ in range(0,iter,1):
          a = choice(lst)
          res = a
          new.append(res)
     for i in new:
          final[0]["relationships_restricted_users"].append(i)
     return final

def following(lst:list):
     new:list = []
     for _ in range(51):
          a = choice(lst)
          new.append(a)
     return new

def save_data(lst:list,filename:str):
     with open(filename,"x") as TextIO:
          dump(obj=lst,fp=TextIO,indent=6)
          TextIO.close()

if __name__=="__main__":
     from time import time
     a_ = time()
     data:list = []
     for i in range(75000):
          a = get_data()
          data.append(a)
     a = hide_story_from(data,10)
     b = blocked_accounts(data,10)
     c = close_friends(data,3)
     d = pending_follow_requests(data,25)
     e = recent_follow_requests(data,120)
     f = recently_unfollowed_accounts(data,13)
     g = removed_suggestions(data,520)
     h = restricted_accounts(data,310)
     i = following(data)
     save_data(data,"followers_1.json")
     save_data(i, "following.json")
     save_data(a,"hide_story_from.json")
     save_data(b,"blocked_accounts.json")
     save_data(c,"close_friends.json")
     save_data(d,"pending_follow_requests.json")
     save_data(e,"recent_follow_requests.json")
     save_data(f,"recently_unfollowed_accounts.json")
     save_data(g,"removed_suggestions.json")
     save_data(h,"restricted_accounts.json")
     b_ = time()
     res = int(b_-a_)
     print(f"Took {res} seconds..")
