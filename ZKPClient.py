# Echo client program
import socket
import random as rnd

HOST = '85.227.190.201' #use your own ip address

PORT = 50055
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#-----------------------------------------------------------------------------------------

def doexp (base, exp):
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

def generateR():
    # TODO: arbitrarily making this 1024
    return rnd.randint(1, 1024)

def authenticate(username, password):
    # verify authentication works 10 times to beat chance
    for x in range(0, 10):
        r = generateR()
        t = doexp(g, r)
        # 8192 here is large enough for the int
        c = int(s.recv(8192))
        s = r + c * x
        s.sendall(str(s))
        resp = s.recv(1024)
        if resp != "authenticated":
            print "sorry - wrong information"
            break

# Server sends generator
g = int(s.recv(1024))

while True:

    while raw_input("Would you like to register? ").startswith('y'):
        s.sendall('register')
        input_user = raw_input("Enter your username: ")
        s.sendall(input_user)
        input_pass = raw_input("Enter your password: ")
        # TODO: arbitrarily modding this to make calculations go faster
        y = doexp(g, hash(input_pass) % 8192)
        s.sendall(str(y))

    s.sendall('authenticate')

    input_user = raw_input("Enter your username: ")
    input_pass = raw_input("Enter your password: ")
    authenticate(input_user, input_pass)
