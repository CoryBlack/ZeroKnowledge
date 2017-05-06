import random as rnd
n = 13
g = 5
username = "n"
password = "a"

def exp(x,e):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X)
            E = E/2
        else:
            Y = (X * Y)
            E = E - 1
    return Y

# essentially pretend between client and server
# code blocks the client sends the necessary info
# to the server and vice versa

# client
# CONCERN: have to mod hash to make calculations
# efficient - only 1024 different passwords then
x = hash(password) % 1024
y = exp(g, x)
# CONCERN: r should be able to be larger i think
r = rnd.randint(1, n - 1)
t = exp(g, r)


# server
# same concern for c as for r
c = rnd.randint(1, n - 1)

#client
s = r + c * x

#server
t1 = exp(g, s)
t2 = t * exp(y, c)
if (t1 == t2):
    print "authenticated B)"
