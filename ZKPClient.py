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


# TODO TODO TODO:
# if incorrect password provided, hangs
# doing it multiple times doesn't quite work yet
def authenticate(username, password):
    # verify authentication works 10 times to beat chance
    # for i in range(0, 10):
    r = generateR()
    t = doexp(g, r)
    s.sendall(str(t))
    s.sendall(username)
    # 8192 here is large enough for the int
    c = int(s.recv(8192))
    x = hash(password) % 1024
    numS = r + c * x
    s.sendall(str(numS))
    resp = s.recv(1024)
    if resp != "authenticated":
        print "sorry - wrong information"
    else:
        print "authenticated!"
            # break

# Server sends generator
g = int(s.recv(1024))

while True:

    while raw_input("Would you like to register? ").startswith('y'):
        s.sendall('register')
        input_user = raw_input("Enter your username: ")
        s.sendall(input_user)
        input_pass = raw_input("Enter your password: ")
        # TODO: arbitrarily modding this to make calculations go faster
        y = doexp(g, hash(input_pass) % 1024)
        s.sendall(str(y))

    s.sendall('authenticate')

    input_user = raw_input("Enter your username: ")
    input_pass = raw_input("Enter your password: ")
    authenticate(input_user, input_pass)
