with open('my_file.txt', mode='r') as file:
    print(file.read())

with open('my_file.txt', mode='w') as file:
    file.write('Hello World!')

with open('my_file.txt', mode='r') as file:
    print(file.read())

    #############

names = []
with open('names.txt', mode='r') as file:
    for line in file:
        names.append(line.strip())

with open('letter.txt', mode='r') as file:
    letter = file.read()
    for name in names:
        with open(f'invites/letter_for_{name}.txt', mode='w') as file:
            file.write(letter.replace('[name]', name))
