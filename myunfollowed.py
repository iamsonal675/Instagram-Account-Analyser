from json import load
from time import time

def open_data():
     followers_1 = load(open("./data/connections/followers_and_following/followers_1.json"))
     following = load(open("./data/connections/followers_and_following/following.json"))
     return [
          followers_1,
          following
     ]

def handle_followers(blo):
     blo = blo[0]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     return lst

def handle_following(blo):
     blo = blo[1]["relationships_following"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     return lst

def save_in_file(lst:list):
     with open(file=str(f"{int(time())}.txt"),mode="x") as f:
          for i in lst:
               f.write(f"{str(i)}\n")

def main():
     d = open_data()
     a = handle_followers(d)
     b = handle_following(d)
     n_follow:list = []
     for i in a:
          if i in b:
               pass
          else:
               n_follow.append(i)
     print("DONE!")
     save_in_file(n_follow)

main()