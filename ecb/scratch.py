import random
import math


def is_prime(number):
    if number<2 or number/2==0 :
        return False
    max_num=math.floor(math.sqrt(number))
    for i in range(2,max_num):
        if number % i==0:
            return False

    return True

def generate_prime(min_value,max_value):
    prime=random.randint(min_value,max_value)
    while not is_prime(prime):
        prime=random.randint(min_value,max_value)
    return prime

def mod_inverse(e,phi):
    for d in range(3,phi):
        if (d*e)% phi == 1:
            return d
    raise ValueError("mod_inverse doesn't exist")

p,q = generate_prime(1000,100000),generate_prime(1000,100000)

while p==q:
    q=generate_prime(1000,100000)

n=p*q
phi_n=(p-1)*(q-1)

e=random.randint(3,phi_n-1)
while math.gcd(e,phi_n)!=1:
    e= random.randint(3,phi_n)

d=mod_inverse(e,phi_n)

print("Public Key:",e)
print("private Key:",d)
print("n:",n)
print("Phi of n",phi_n)
print("p:",p)
print("q:",q)

message=input("message")

message_encoded =[ord(ch) for ch in message]
cipertext = [pow(ch,e,n) for ch in message_encoded]

print(cipertext)
message_encoded=[pow(ch,d,n) for ch in cipertext]
message="".join(chr(ch) for ch in message_encoded)

print(message)



