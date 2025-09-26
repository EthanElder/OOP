def area_rectangle():
    l = float(input("Enter the length of rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    print(l * w)

def volume_cube():
    cube = float(input("Enter the length of one side of the cube: "))
    print(cube*cube*cube)

def area_circle():
    rad = float(input("Enter the radius of the circle: "))
    print(rad*rad*3.14)

def perimeter_circle():
    radi = float(input("Enter the radius of the circle: "))
    print(2*3.14*radi)

def volume_sphere():
    radius = float(input("Enter the radius of the sphere: "))
    print((4/3)*3.14*radius*radius*radius)

while 1:
    print("1. Find area of a rectangle")
    print("2. Find the volume of a cube")
    print("3. Find the area of a circle")
    print("4. Find the perimeter of a circle")
    print("5. Find the volume of a sphere")
    print("6. Quit")
    x = int(input("Enter your choice: "))

    if x == 1:
        area_rectangle()

    elif x == 2:
        volume_cube()

    elif x == 3:
        area_circle()

    elif x == 4:
        perimeter_circle()

    elif x == 5:
        volume_sphere()

    elif x == 6:
        break