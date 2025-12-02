#open in read mode
file = open('codingal.txt', 'r')
print(file.read())
file.close()

# open in read mode and read multiple lines
file = open('codingal.txt', 'r')
print("\n read first 1 line")
print(file.readline())
print(file.readline())
file.close()

# open in read mode and read  3 lines
file = open('codingal.txt', 'r')
print("\n read first 3 lines ")
print(file.readline())
print(file.readline())
file.close()

# open in read mode and loop through the lines of the file
file = open('codingal.txt','r')
print("\n read all lines using loop")
for line in file:
    print(line)
file.close()
