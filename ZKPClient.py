# Echo client program
import socket
import random as rnd

HOST = '130.229.131.64' #use your own ip address
PORT = 50050
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#-----------------------------------------------------------------------------------------



# #-------------------------------------------------------------------------------------
# #Boilerplate input output code
# s.sendall('Hello,world')
# data = s.recv(1024)
# s.close()
# print 'Received', repr(data)
# #-------------------------------------------------------------------------------------


# #-------------------------------------------------------------------------------------------
# #All other defined Methods


# def sendUsernameAndY():
#         return 1

def domodexp (base, exp, mod):
    workingB = base
    workingE = exp
    total = 1
    while(workingE > 0):
        if workingE % 2 == 0:
            # square for every position in the binary rep
            workingB = (workingB * workingB) % mod
            workingE = workingE / 2
        else:
            # if reach a 1 in the binary rep, add 1 more of total
            total = (total * workingB) % mod
            workingE = workingE - 1
    return total

def computeY(x):
	return domodexp(g, x, x)

def generateR():
	return rnd.randint(1, n - 1)

def authenticate(username, password):
	#Right before all of this we need to tell the server we are trying to authenticate and it will send us A
	A = s.recv(1024) #not sure if this is correct but placeholder
	print(A)
	s.send(username)
	print("d")
	#put in username and password
	x = hash(password)
	print x
	y = computeY(x)
	print("computed")
	r = generateR()
	print('ss')

	# We dont know if Mod is necessary or not TODO
	t = (g ** r) % n # add our own exponentiation if we want faster code
	print 'b'
	c = hash(str(y) + str(t) + str(A))
	z = r - (c * x)
	print 'd'
	print c
	s.sendall(str(c))
	print c
	s.sendall(str(z))
	print z
	response = s.recv(1024)
	print(response)

#Before registration we need to receive these from the clients
n = 13
g = 5

while True:

	while raw_input("Would you like to register? ") == 'yes':
		s.sendall('register')
		input_user = raw_input("Enter your username: ")
		s.sendall(input_user)
		input_pass = raw_input("Enter your password: ")
		s.sendall(str(hash(input_pass)))

	s.sendall('authenticate')

	input_user = raw_input("Enter your username: ")
	input_pass = raw_input("Enter your password: ")
	print input_user
	print input_pass

	#All authentication code lies within the Authentication method

	authenticate(input_user, input_pass)
