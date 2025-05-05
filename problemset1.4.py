#Write a program using switch case which takes a value and prints the respective Size.If size is 29 then its small
size=int(input("enter a size of the pants:"))
sizes = {29: "Small", 30: "Medium", 38: "Large", 42: "XLarge"}
print(sizes.get(size),"Invalid")

