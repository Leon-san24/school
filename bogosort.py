from random import randint,shuffle

numbers = []
c = 0
while c != 4:
    c += 1
    numbers.append(randint(0, 100))

print(numbers)

check = sorted(numbers)

print(check)

while numbers != check:
    shuffle(numbers)
    print(numbers)