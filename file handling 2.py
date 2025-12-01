file_read=open('codingal.txt' , 'r')
print("file in Read Mode-")
print(file_read.read())
file_read.close()

# Open file in write mode
file_write= open('codingal.txt' , 'w')
file_write.write("File in write mode........")
file_write.write("Hi I am Aimaaaaaaaaaaaaaaaaa")
file_write.close()

# Open file in append mode
file_append= open('codingal.txt', 'a')
file_append.write("\n File in append mode......" )
file_append.write("\n Hello, I am learning to code.")
file_append.close