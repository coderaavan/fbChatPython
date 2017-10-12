import fbchat

from fbchat import Client
from fbchat.models import *

def login(username,password):
	return fbchat.Client(username, password, max_tries = 1)

def iLI(client):
	return client.isLoggedIn()

def sendmsg(client, msg, name, groupname, broadcast):
	friendlist = []
	
	if (len(broadcast) > 0):
		friendlist = broadcast.split(',')

	if (len(name) > 0):
		if name not in friendlist:
			friendlist.append(name)

	if (len(friendlist) > 0):
		for eachfriend in friendlist:
			friends = client.searchForUsers(eachfriend)
			friend = friends[0]

			sent = client.sendMessage(msg, thread_id = friend.uid, thread_type = ThreadType.USER)

			if not sent:
				print("Message not sent to " + eachfriend + "!")
		if sent:
			print("Message sent!")

	if (len(groupname) > 0):
		groups = client.searchForGroups(groupname)
		group = groups[0]
		sent = client.sendMessage(msg, thread_id = group.uid, thread_type = ThreadType.GROUP)

		if sent:
			print("Message sent!")
