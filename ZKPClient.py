# Echo client program
import socket
import random as rnd

HOST = 'localhost' #use your own ip address

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
            workingB = (workingB * workingB)%n
            workingE = workingE / 2
        else:
            # if reach a 1 in the binary rep, add 1 more of total
            total = (total * workingB)%n
            workingE = workingE - 1
    return total

def generateR():
    # TODO: arbitrarily making this 1024
    return rnd.randint(1, 1024)


def authenticate(username, password):
    # verify authentication works 10 times to beat chance
    i = 0
    while i<10:
        s.sendall(username)
        if (s.recv(8192) == "not a user"):
            resp = "User not registered"
            break
        i += 1
        r = generateR()
        t = doexp(g, r)
        s.sendall(str(t))
        # 8192 here is large enough for the int
        c = int(s.recv(8192))
        x = hash(password)%2048
        numS = r + c * x
        s.sendall(str(numS))
        resp = s.recv(1024)
        if resp != "authenticated":
            break
    print resp

# Server sends generator
n = int(s.recv(1024))
g = int(s.recv(1024))

while True:

    action = raw_input("Would you like to register? ")
    if action.startswith('y'):
        s.sendall('register')
        input_user = raw_input("Enter your username: ")
        s.sendall(input_user)
        input_pass = raw_input("Enter your password: ")
        y = g**(hash(input_pass)%2048)
        s.sendall(str(y))
        print

    else :
        s.sendall('authenticate')
        input_user = raw_input("Enter your username: ")
        input_pass = raw_input("Enter your password: ")
        authenticate(input_user, input_pass)
        print
