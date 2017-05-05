# Echo client program
import socket

HOST = '130.229.144.135' #use your own ip address
PORT = 50055
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#-----------------------------------------------------------------------------------------


#Before registration we need to receive these from the clients
n = 13
g = 5

while true:

	while raw_input("Would you like to register? ") == 'yes':
		s.sendall('register')
		input_user = raw_input("Enter your username: ")
		s.sendall(input_user)
		input_pass = raw_input("Enter your password: ")
		s.sendall(hash(input_pass))

	s.sendall('authenticate')

	input_user = raw_input("Enter your username: ")
	input_pass = raw_input("Enter your password: ")

	#All authentication code lies within the Authentication method

	# authenticate(input_user, input_pass)



# #-------------------------------------------------------------------------------------
# #Boilerplate input output code
# s.sendall('Hello, world')
# data = s.recv(1024)
# s.close()
# print 'Received', repr(data)
# #-------------------------------------------------------------------------------------


# #-------------------------------------------------------------------------------------------
# #All other defined Methods


# def sendUsernameAndY():
#         return 1

def computeY(x):
	return g**x

def generateR():
	return rnd.random(1,n-1)

def authenticate(username, password):
	#Right before all of this we need to tell the server we are trying to authenticate and it will send us A
	A = s.recv(1024) #not sure if this is correct but placeholder
	s.sendall(username)

	#put in username and password
	x = hash(password)
	y = computeY(x)
	r = generateR()

	# We dont know if Mod is necessary or not TODO
	t = (g ** r) % n # add our own exponentiation if we want faster code

	c = hash(str(y) + str(t) + str(A))
	z = r - (c * x)


	s.sendall(str(c))
	s.sendall(str(z))
	response = s.recv(1024)
	print(response)
