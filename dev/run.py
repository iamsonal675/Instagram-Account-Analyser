from json import load

def open_data():
     blocked_account = load(open("./data/connections/followers_and_following/blocked_accounts.json"))
     close_friends = load(open("./data/connections/followers_and_following/close_friends.json"))
     hide_story_from = load(open("./data/connections/followers_and_following/hide_story_from.json"))
     pending_follow_requests = load(open("./data/connections/followers_and_following/pending_follow_requests.json"))
     recently_follow_requests = load(open("./data/connections/followers_and_following/recent_follow_requests.json"))
     recently_unfollow_account = load(open("./data/connections/followers_and_following/recently_unfollowed_accounts.json"))
     removed_suggestions = load(open("./data/connections/followers_and_following/removed_suggestions.json"))
     restricted_accounts = load(open("./data/connections/followers_and_following/restricted_accounts.json"))
     followers_1 = load(open("./data/connections/followers_and_following/followers_1.json"))
     following = load(open("./data/connections/followers_and_following/following.json"))
     return [
          blocked_account,
          close_friends,
          hide_story_from,
          pending_follow_requests,
          recently_follow_requests,
          recently_unfollow_account,
          removed_suggestions,
          restricted_accounts,
          followers_1,
          following
     ]

def handle_blocked_accounts(blo):
     blo = blo[0]["relationships_blocked_users"]
     lst:list = []
     for i in blo:
          lst.append(i["title"])
     print(lst)

def handle_close_friends(blo):
     blo = blo[1]["relationships_close_friends"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     print(lst)

def handle_hide_story_from(blo):
     blo = blo[2]["relationships_hide_stories_from"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     print(lst)

def handle_pending_follow_requests(blo):
     blo = blo[3]["relationships_follow_requests_sent"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     print(lst)

def handle_recently_follow_requests(blo):
     blo = blo[4]["relationships_permanent_follow_requests"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     print(lst)

def handle_recently_unfollow_account(blo):
     blo = blo[5]["relationships_unfollowed_users"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     print(lst)

def handle_removed_suggestions(blo):
     blo = blo[6]["relationships_dismissed_suggested_users"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     print(lst)

def handle_restricted_accounts(blo):
     blo = blo[7]["relationships_restricted_users"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     print(lst)

def handle_followers(blo):
     blo = blo[8]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     print(lst)

def handle_following(blo):
     blo = blo[9]["relationships_following"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     print(lst)

def test():
     a = open_data()
     handle_following(a)

def load_data():
     pass

test()
