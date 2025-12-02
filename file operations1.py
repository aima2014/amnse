#open file and read its contents
file = open('codingal.txt2', 'r')
print(file.read())
file.close()

#open file and read its beginning 8 characters
file = open('codingal.txt2', 'r')
print("\n Read in parts \n")
print(file.read(8))

#append your name and age in the file
file = open('codingal.txt2', 'a')
file.write("Hi! I am Aima and i am 11 years old")
file.close()