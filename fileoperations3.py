# program to remove lines starting with prefix 
file = open('codingal.txt','r')
file2= open('CodingalUpdated.txt','w')

# reading each line from original file
for line in file.readlines():

# reading all lines that do not start with coding
     
        if not(line.startswith("coding")):
          print(line)

