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
conn.sendall(str(n))
conn.sendall(str(g))


def generateC():
	# TODO: arbitrarily making this 1024
	return rnd.randint(0, 1024)


def doexp (base, exp):
    workingB = base
    workingE = exp
    total = 1
    while(workingE > 0):
        if workingE % 2 == 0:
            # square for every position in the binary rep
            workingB = (workingB * workingB)%n
            workingE = workingE / 2
        else:
            # if reach a 1 in the binary rep, add 1 more of total
            total = (total * workingB)%n
            workingE = workingE - 1
    return total

def authenticate():
        i=0
        while i<10:
                i += 1
                t = int(conn.recv(8192))
                username = conn.recv(8192)
                c = generateC()
                conn.sendall(str(c))
                s = int(conn.recv(8192))
                t1 = doexp(g, s)
                y = int(usernames[username])
                t2 = (t * doexp(y, c))%n
                if (t1 == t2):
                        conn.sendall("authenticated")
                else:
                        conn.sendall("Wrong password")
                        break


# determines what action server should take based
# on what the client wants to do
while 1:
	action = conn.recv(1024)
	if (action == "register"):
		username = conn.recv(1024)
		Y = conn.recv(8192)
		usernames[username] = Y
	elif (action == "authenticate"):
		# want to authenticate
		authenticate()
	else:
		print action
		s.close()
		break
