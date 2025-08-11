print("Takshashila university")
print("ongur,tindivanam")
print("-------------------")
print("Student mark list")
print("-------------------")
pymark=int(input("Enter the python mark:"))
dbmsmark=int(input("Enter the dbms mark:"))
indmark=int(input("Enter  the industry mark:"))
total=pymark+dbmsmark+indmark
print("Total mark:",total)
avg=total/3
print("Average mark:",avg)
if pymark>=40 and dbmsmark>=40 and indmark>=40:
    print("Result:pass")
if total>=250:
    print("Grade:O Grade*")
elif total>=200:
    print("Grade: A+ Grade*")
elif total>=150:
    print("Grade: A Grade*")
else:
    print("Grade: B Grade*")
    print("Result:Fail")
    print("Grade no Grade (Failed)")
