import math
a = int(input("Input initial condition:"))
s = int(input("Input quantity of terms:"))
n = 1
print(f"{n, a}")
while n <= s:
    n += 1
    a = a + math.gcd(n, a)
    print(f"{n, a}")
else:
    print("Generation completes")