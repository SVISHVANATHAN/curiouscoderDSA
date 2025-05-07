#Write a program to take x and print multiples of x till 1000
x = int(input("Enter a number: "))
for i in range(x, 1001, x):#start,stop,step
    print(i)


