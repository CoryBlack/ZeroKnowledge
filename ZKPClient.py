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


input_register = raw_input("Would you like to register? ")

if input_register == 'yes':
	s.sendall('true')
	input_user = raw_input("Enter your username: ")
	s.sendall(input_user)
	input_pass = raw_input("Enter your password: ")
	s.sendall(input_pass)


# hashedP = hash(input_pass)

# #All authentication code lies within the Authentication method

# authenticate("placeholder", hashedP)



# #-------------------------------------------------------------------------------------
# #Boilerplate input output code
# s.sendall('Hello, world')
# data = s.recv(1024)
# s.close()
# print 'Received', repr(data)
# #-------------------------------------------------------------------------------------


# #-------------------------------------------------------------------------------------------
# #All other defined Methods

def hash():
	return 5


# def sendUsernameAndY():
#         return 1

# def computeY(x):
# 	return g**x

# def generateR():
# 	return rnd.random(1,n-1)

# def authenticate(username, password):
# 	#Right before all of this we need to tell the server we are trying to authenticate and it will send us A
# 	A = s.recv(1024) #not sure if this is correct but placeholder

# 	#put in username and password
# 	x = hash(password)
# 	y = computeY(x)
# 	r = generateR()

# 	# We dont know if Mod is necessary or not TODO
# 	t = (g ** r) % n # add our own exponentiation if we want faster code

# 	c = hash(str(y) + str(t) + str(A))
# 	z = r - (c * x)

# 	username = "jerry"
# 	s.sendall(username + "c = " + str(c) + "z = " + str(z))

