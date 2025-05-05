'''
Given mark of student, Print the Grade

Grade A if mark is greater than or equal to 90

Grade B if mark is greater than or equal to 80

Grade C if mark if greater than or equal to 60

Grade D if mark if greaer than or equal to 35

Fail if mark is lesser than 35
'''
mark=int(input("enter a mark of student:"))
if mark>=90:
    print("Grade A")
elif (mark<90 and mark>=80):
    print("Grade B")
elif (mark<80 and mark>=60):
    print("Grade C")
elif (mark<60 and mark>=35):
    print("Grade D")
else:
    print("Fail")

