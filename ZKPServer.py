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

# map from username to Y value
usernames = {}
n = 13
g = 5
# send generator
conn.sendall(str(n))
conn.sendall(str(g))

# generates random challenge
# see writeup for why we bound it by a multiple of n - 1
def generateC():
    return rnd.randint(0, 100 * (n - 1))

# fast exponentiation mod n
def doexp (base, exp):
    workingB = base
    workingE = exp
    total = 1
    while(workingE > 0):
        if workingE % 2 == 0:
            # square for every position in the binary rep
            workingB = (workingB * workingB) % n
            workingE = workingE / 2
        else:
            # if reach a 1 in the binary rep, add 1 more of total
            total = (total * workingB) % n
            workingE = workingE - 1
    return total

def authenticate():
        i=0
        # repeat process multiple times
        while i<10:
                i += 1
                username = conn.recv(8192)
                if (username not in usernames):
                    conn.sendall("not a user")
                    break
                else:
                    conn.sendall("ok")
                t = int(conn.recv(8192))
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
