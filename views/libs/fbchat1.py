import fbchat

from fbchat import Client
from fbchat.models import *

def login(username,password):
	return fbchat.Client(username, password, max_tries = 1)

def iLI(client):
	return client.isLoggedIn()

def sendmsg(client, msg, names, groupnames):
    for name in names:
        try:
            friends = client.searchForUsers(name)

            if (len(friends) > 0):
                friend = friends[0]
                sent = client.sendMessage(msg, thread_id = friend.uid, thread_type = ThreadType.USER)

                if sent:
                    print("Message sent!")

            else:
                print("Can't find a user name : ", name)

        except FBchatException:
            continue

    for name in groupnames:
        try:
            groups = client.searchForGroups(name)

            if (len(groups) > 0):
                group = groups[0]
                sent = client.sendMessage(msg, thread_id = group.uid, thread_type = ThreadType.GROUP)

                if sent:
                    print("Message sent!")

            else:
                print("Can't find a group name : ", name)

        except FBchatException:
            continue

