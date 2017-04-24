# Echo server program
import socket

HOST = ''
PORT = 50008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

#-------------------------------------------------------------------
#Our code below, rest is just boilerplate connections

n = 13
g = 5

#REGISTRATION
#If connected for registration, wait for the username and Y and store it
#usernames.add(username)
#Ys.add(Y)






#Begin Authentication
#Generate integer a
A = generateA()
conn.sendall(A)

#Receives c and z as a result of the client calculations
#username = ...
#c = ...
#z = ...
t = generateT()

zPrime = hash(str(y) + str(t) + str(A))

if c == cPrime:
	#user has correctly authenticated
	conn.sendall("You're in!")


#-------------------------------------------------------------------------------------
#Boilerplate input output code
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
#-------------------------------------------------------------------------------------


def hash(val):


def generateA():
	return 5 #just a placeholder


#look up the y corresponding to the username
def generateT(username, c, z):
	#find y
	# We dont know if Mod is necessary or not TODO
	return ((y ** c) * (g ** z)) % n
