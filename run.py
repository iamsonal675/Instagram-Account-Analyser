from json import load

followers = load(open("./followers_1.json"))
following = load(open("./following.json"))
following = following["relationships_following"]

followers_data = []
following_data = []

not_following = []
u_not_following = []

for i in followers:
    followers_data.append(i["string_list_data"][0]["value"])

for i in following:
    following_data.append(i["string_list_data"][0]["value"])

for i in following_data:
    if i in followers_data:
        pass
    else:
        not_following.append(i)

for i in followers_data:
    if i in following_data:
        pass
    else:
        u_not_following.append(i)

with open("not_following.txt",mode="x") as f:
    for i in not_following:
        f.write(f"{str(i)}\n")
with open("u_not_following.txt",mode="x") as f:
    for i in u_not_following:
        f.write(f"{str(i)}\n")
