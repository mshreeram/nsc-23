import random
p = int(input("Enter p(prime number): "))
g = int(input("Enter g(primitive root of p): "))
a = random.randint(1, 100)
b = random.randint(1, 100)
print("Generated random nos a and b are", a , b)
A = int(pow(g,a,p))
B = int(pow(g,b,p))
Ka = int(pow(B,a,p))
Kb = int(pow(A,b,p))
print("Secret key at A(ka) = ", str(Ka))
print("Secret key at B(kb) = ", str(Kb))