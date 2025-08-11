print("Government of tamilnadu")
print("Electricity board")
print("--------------------")
print("Bill recipt")
print("--------------------")
EB=int(input("Enter the eb no:"))
CN=input("Enter the current name:")
PU=int(input("Enter the previous unit:"))
CU=int(input("Enter the current unit:"))
unit=PU+CU
print("Unit consumed:",unit)
if(unit>=1000):
    amt=unit*10
    print("Amount to be paid:",amt)
elif(unit>=500):
    amt=unit*5
    print("Amount to be paid:",amt)
elif(unit>=100):
    amt=unit*2
    print("Amount to be paid:",amt)
else:
    print("Amount to be paid:",nill)
