# Echo server program
import socket
import random as rnd
import sys

HOST = ''
PORT = 50055
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

# rnd.seed(1) #just for tests
usernames = {}
n = 13
g = 5


def generateA():
	return rnd.randint(0, sys.maxsize) #just a placeholder


def domodexp (base, exp):
    workingB = base
    workingE = exp
    total = 1
    while(workingE > 0):
        if workingE % 2 == 0:
            # square for every position in the binary rep
            workingB = (workingB * workingB)
            workingE = workingE / 2
        else:
            # if reach a 1 in the binary rep, add 1 more of total
            total = (total * workingB)
            workingE = workingE - 1
    return total


#look up the y corresponding to the username
def generateT(y, c, z):
	# We dont know if Mod is necessary or not TODO
	return ((domodexp(y, c)) * (domodexp(g, z)))


def authenticate():
	A = generateA()
	conn.sendall(str(A))

	#TODO: change the buffer size here ?
	# server receives the username, c, and z
	curr_username = conn.recv(1024)
	# t = int(conn.recv(8192))
	print "d"
	y = int(usernames[curr_username])

	c = int(conn.recv(8192)) % y
	z = int(conn.recv(8192)) % y
	print c
	print z

	t = generateT(y, c, z)
	# server calculates its expected c
	print
	print
	print y
	print t
	print A
	print
	print
	cPrime = hash(str(y) + "&" + str(t) + "&" + str(A))
	print cPrime
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
		print "a"
		authenticate()
	else:
		s.close()
		break
