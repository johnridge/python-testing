import secrets
seen=set()
count = 0
seq=[1, 2, 3, 4, 5, 6, 7, 8, 9]
seed = int(str(secrets.choice(seq)) + str(secrets.choice(seq)) + str(secrets.choice(seq)) + str(secrets.choice(seq)))
number = seed
while number not in seen:
    seen.add(number)
    count += 1
    number = int(str(number * number).zfill(8)[2:6])
    print(f"#{count}: {number}")
else:
    print(f"Our initial seed was {seed} and we have repeated ourselves after {count} steps, with {number}")

