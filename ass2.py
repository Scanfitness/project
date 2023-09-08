# Print all the letters of the alphabet in uppercase except J and T
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if letter != 'J' and letter != 'T':
        print(letter, end= " ")
print()

# Print 1 - 99 separeted by comma and space
for n in range(1, 100):
    print(int(n), end= ", ")
print()

