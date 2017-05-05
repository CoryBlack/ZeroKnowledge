# Echo server program
import socket
import random as rnd

HOST = ''
PORT = 50055
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

rnd.seed(1) #just for tests
usernames = {}
n = 13
g = 5

def generateA():
	return rnd.randint(0,10000) #just a placeholder


#look up the y corresponding to the username
def generateT(y, c, z):
	# We dont know if Mod is necessary or not TODO
	return ((y ** c) * (g ** z)) % n


def authenticate():
	A = generateA()
	conn.sendall(str(A))

	#TODO: change the buffer size here ?
	# server receives the username, c, and z
	curr_username = conn.recv(1024)
	c = int(conn.recv(8192))
	z = int(conn.recv(8192))
	y = usernames[curr_username]

	t = generateT(y, c, z)
	# server calculates its expected c
	cPrime = hash(str(y) + str(t) + str(A))

	# if match, then client is authenticated
	if c == cPrime:
		conn.sendall("You're in!")


#-------------------------------------------------------------------
# client sends true or false for if we are registering
# loop continues until false is sent - meaning we want to authenticate
while 1:
	action = conn.recv(1024)
	if (action == "register"):
		username = conn.recv(1024)
		Y = conn.recv(1024)
		usernames[username] = Y
	elif (action == "authenticate"):
		# want to authenticate
		authenticate()
	else:
		break
