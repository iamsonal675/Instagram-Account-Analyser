from json import load
from time import time

def open_data():
     followers_1 = load(open("./crosscheck/v1/followers_1.json"))
     followers_12 = load(open("./crosscheck/v2/following.json"))
     return [
          followers_1,
          followers_12
     ]

def handle_followers_1(blo):
     blo = blo[0]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     return lst

def handle_followers_12(blo):
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
     a = handle_followers_1(d)
     b = handle_followers_12(d)
     new_follower:list = []
     if len(a) > len(b):
          for i in a:
               if i in b:
                    pass
               else:
                    new_follower.append(i)
          print("DONE!")
          save_in_file(new_follower)
     elif len(b) > len(a):
          for i in b:
               if i in a:
                    pass
               else:
                    new_follower.append(i)
          print("DONE!")
          save_in_file(new_follower)
     else:
          for i in b:
               if i in a:
                    pass
               else:
                    new_follower.append(i)
          print("DONE!")
          save_in_file(new_follower)


main()