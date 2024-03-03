import math

#Taking input

p = int(input("Enter a prime number for 'p': "))
q = int(input("Enter a prime number for 'q': "))

#Checking the input is valid for prime

def prime_check(a):
    if(a == 2):
        return True
    elif((a < 2) or ((a % 2) == 0)):
        return False
    elif(a > 2):
        for i in range(2, a):
            if not(a % i):
                return False
    return True

check_p = prime_check(p)
check_q = prime_check(q)
 
while(check_p == False):
    p = int(input("Enter a prime number for 'p': "))
    check_p = prime_check(p)

while(check_q == False):
    q = int(input("Enter a prime number for 'q': "))
    check_q = prime_check(q)

'''CALCULATION OF RSA MOPDULUS 'n'.'''
n = p * q

print("RSA Modulus(n) is: ", n)

'''CALCULATION OF EULERS TOITENT 'r'.'''
r = (p - 1) * (q - 1)
print("Eulers Toitent(r) is:", r)

'''CALCULATION OF GCD FOR 'e' CALCULATION.'''
def egcd(e,r):
    while(r != 0):
        e,r = r, e % r
    return e

def eugcd(e,r):
    for i in range(1, r):
        while(e != 0):
            a, b = r // e, r % e
            r = e
            e = b

def eea(a, b):
    if(a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s - ((a // b) * t)
        return (gcd, t, s)

def mult_inv(e, r):
    gcd, s, _ = eea(e, r)
    if(gcd != 1):
        return None
    else:
        return s % r

for i in range(1, 1000):
    if(egcd(i, r) == 1):
        e = i

print("The value of e is: ", e)

eugcd(e, r)

d = mult_inv(e, r)
public = (e, n)
private = (d, n)
print("Private key is: ", private)
print("Public key is: ", public)

'''ENCRYPTION ALGORITHM.'''
def encrypt(pub_key, n_text):
    e, n = pub_key
    x = []
    m = 0
    for i in n_text:
        if(i.isupper()):
            m = ord(i) - 65
            c = (m ** e) % n
            x.append(c)
        elif(i.islower()):
            m = ord(i) - 97
            c = (m ** e) % n
            x.append(c)
        elif(i.isspace()):
            spc = 400
            x.append(400)
    return x

'''DECRYPTION ALGORITHM.'''
def decrypt(priv_key, c_text):
    d, n = priv_key
    txt = c_text.split(',')
    x =''
    m = 0
    for i in txt:
        if(i == '400'):
            x += ' '
        else:
            m = (int(i) ** d) % n
            m += 65
            c = chr(m)
            x += c
    return x

message = input("What would you like encrypted or decrypted?(Seperate numbers with ','): ")
print("Your message is: ", message)

choose = input("Type '1' for encryption or '2' for decryption. ")
if(choose == '1'):
    enc_msg = encrypt(public, message)
    print("Your encrypted message is: ", enc_msg)
elif(choose == '2'):
    print("Your decrypted message is: ", decrypt(private, message))
else:
    print("You Entered the wrong option.")