# Print all the letters of the alphabet in uppercase except J and T
for value in range(ord("A"), ord("Z") + 1):
    letter = chr(value)
    if letter not in ['J', 'T']:
        print(letter, end= " ")
print()

# Print 1 - 99 separeted by comma and space
for n in range(1, 100):
    print(int(n), end= ", ")
print()

