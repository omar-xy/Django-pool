
file = open("numbers.txt", "r")
numbers = file.read()
numbers = numbers.split(',')
numbers = list(map(int, numbers))

for i in numbers:
    print(i)

