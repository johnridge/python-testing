import math
b = int(input("Enter upper bound:"))
n = 0
phi = (1 + 5 ** 0.5) / 2
psi = -phi ** -1
print("Beginning generation")
while n < b:
    f = ((phi ** n) - (psi ** n)) / (phi - psi)
    print(math.floor(f))
    n += 1
else:
    print("Generation complete")