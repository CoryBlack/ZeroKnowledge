# Echo server program
import socket
import random as rnd

HOST = ''
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

#-------------------------------------------------------------------
# client sends true or false for if we are registering
# loop continues until false is sent - meaning we want to authenticate
while 1:
	register = conn.recv(1024)
	if (register == true)
		username = conn.recv(1024)
		Y = conn.recv(1024)
		usernames[username] = Y
	else
		break

rnd.seed(1) #just for tests
usernames = {}
n = 13
g = 5


#Begin Authentication
#Generate integer a
A = generateA()
conn.sendall(A)

#TODO: change the buffer size here ?
c = int(conn.recv(8192))
z = int(conn.recv(8192))
t = generateT()

# server calculates its expected c
cPrime = hash(str(y) + str(t) + str(A))

# if match, then client is authenticated
if c == cPrime:
	conn.sendall("You're in!")


def generateA():
	return rnd.randint(0,10000) #just a placeholder


#look up the y corresponding to the username
def generateT(username, c, z):
	if usernames.has_key(username):
                y = usernames.get(username)
	# We dont know if Mod is necessary or not TODO
	return ((y ** c) * (g ** z)) % n
