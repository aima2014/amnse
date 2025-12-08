file_read = open("C:/Users/shyle/Downloads/Codingal.txt", "r")

print("File in read mode -")

f = file_read.read()

print(f)

file_read.close()

# Writing to file

file_write = open("Codingal.txt", "w")

file_write.write("File in write mode ....\n")

file_write.write("Hi! I am Penguin. I am 1 yr. old.\n")

file_write.close()

# Appending to file

file_append = open("Codingal.txt", "a")

file_append.write("In file in append mode ....\n")

file_append.write("Hi! I am penguin. I am 1 yr. old.\n")

file_append.close()