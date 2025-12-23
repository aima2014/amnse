choice = input("Welcome to area calculator \nPlease Enter your choice \n1 area of a rectangle \n2 area of a triangle \n3 area of a circle\n4 area of a parallelogram: ")

if choice == '1':
    length = float(input('Enter the Length: '))
    breadth = float(input('Enter the breadth: '))
    result = length * breadth
    print("The Area is " + str(result))

if choice == '2':
    height = float(input('Enter the height: '))
    breadth = float(input('Enter the breadth: '))
    result = height * breadth
    print("The area is " + str(result))

if choice == '3':
    radius = float(input('Enter the radius: '))
    result = 3.14 * radius * radius
    print("The area is " + str(result))

if choice == '4':
    height = float(input('Enter the Height: '))
    base = float(input('Enter the corresponding base: '))
    result = height * base
    print("The area is " + str(result))