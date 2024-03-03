import math

def gcd(a, h):
  temp = 0
  while(1):
    temp = a % h
    if (temp == 0):
      return h
    a = h
    h = temp

p = 21
q = 23
n = p * q
e = 7
phi = (p - 1) * (q - 1)

while(e < phi):
  if (gcd(e, phi) == 1):
    break
  else:
    e = e + 1

k = 3
d = (1 + (k * phi)) / e
print("Modular multiplicative inverse of (e mod phi): ", d)

msg = 20.0
print("Message data = ", msg)
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)