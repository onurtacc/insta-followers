import instaloader

L = instaloader.Instaloader()

username = ""
password = ""

L.login(username, password)

profile = instaloader.Profile.from_username(L.context, username)
followers = profile.get_followers()
followed = profile.get_followees()

follower_list = list()
followed_list = list()

for i in followers:
    follower_list.append(i.username)

for j in followed:
    followed_list.append(j.username)

for follower in list(set(followed_list) - set(follower_list)):
    print(follower, " does not follow you")
