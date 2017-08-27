powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)

print(powers)

num = int(input('Enter a number to convert it into binary: '))

printing = False

for power in powers:
    digit = num // power
    if digit != 0:
        printing = True
    if printing:
        print(digit)
        x = x % power
