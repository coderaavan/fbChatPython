import fbchat
from fbchat import Client
from fbchat.models import *
def login(username,password):
	return fbchat.Client(username,password, max_tries=1)
def iLI(client):
	return client.isLoggedIn()
def sendmsg(client,msg,name):
	friends=client.searchForUsers(name)
	friend=friends[0]
	sent=client.sendMessage(msg,thread_id=friend.uid, thread_type=ThreadType.USER)
	if sent:
		print("Message sent!")