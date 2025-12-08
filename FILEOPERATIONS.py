file_read=open('new_file.txt', 'x')
new_file.close()

import os
print("checking if new_file.txt exists or not..... ")
if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")
else:
    print("the file does not exists")

    my_file = open("new_file.txt", "w")
    my_file.write("Hello this is Codingal")
    my_file.close()

    os.remove('codingal.txt')
    os.rmdir('aimaaa')
    
