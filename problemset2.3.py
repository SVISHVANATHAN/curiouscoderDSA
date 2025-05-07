#Write a program to get firstName and lastName and n as input and print fullName that is firstName+lastName for n times.
firstname=str(input("enter your first name:"))
lastname=str(input("enter your last name:"))
loop=int(input("how many times you can print:"))
for i in range(loop):
    print(firstname+lastname)