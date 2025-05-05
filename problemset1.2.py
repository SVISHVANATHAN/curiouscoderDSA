#Write a program to check whether a triangle can be formed with the given values for the angles
angle1=int(input("enter a first side angle of an triangle:"))
angle2=int(input("enter a second side angle of an triangle:"))
angle3=int(input("enter a third side angle of an triangle:"))
if (angle1+angle2+angle3)==180:
    print("triangle can be formed")
else:
    print("Triangle cannot be formed")