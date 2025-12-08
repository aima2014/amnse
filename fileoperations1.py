# write in file using()function
with open('codingal.txt','w') as file:
    file.write("Hi this is Codingal.")
    file.close()

    #split file into words
    with open('codingal.txt','r') as file:
        data = file.readlines()
        print("words in this file are....")
        for line in data:
            word = line.split()
            print (word)
file.close()