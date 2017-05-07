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
# TODO: we don't use n anywhere ?
n = 13
g = 5
conn.sendall(str(g))


def generateC():
	# TODO: arbitrarily making this 1024
	return rnd.randint(0, 1024)


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

def authenticate():
	c = generateC()
	conn.sendall(str(c))
	s = int(conn.recv(8192))
	t1 = doexp(g, s)
	t2 = t * doexp(y, c)
	if (t1 == t2):
		conn.sendall("authenticated")


# determines what action server should take based
# on what the client wants to do
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
