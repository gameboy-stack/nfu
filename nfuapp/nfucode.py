import instaloader

L = instaloader.Instaloader()
username = "ntf_u"
password = "=-0987654321`"
# Login or load session
L.login(username, password)        # (login)
# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "sanjay.jpeg_")


followers_list = []
count=0
for followee in profile.get_followers():
    followers_list.append(followee.username)

following_list = []
counts=0
for followe in profile.get_followees():
    following_list.append(followe.username)

notfllwingu = []

notfllwingu = list(set(following_list) - set(followers_list))

res = list(dict.fromkeys(notfllwingu))

res.sort()

print(res)
nfu = len(res)
print(nfu)
