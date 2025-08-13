print("Bhvui computer")
print("Nehru street, marakanam")
print("------------------------")
print("Bill recipt")
print("------------------------")
No=input("Enter the item No:")
Name=input("Enter the particular:")
Rate=int(input("Enter the Rate:"))
Quty=int(input("Enter the Quantity:"))
Total=Rate*Quty
print("Total amount in RS:")
if(Total>=100000):
   GST=Total*10/100
elif(Total>=50000):
    GST=Total*5/100
elif(Total>20000):
    GST=Total*3/100
elif(Total>=10000):
    GST=Total*2/100
else:
    GST=Total*1/100
print("GST(Good&service tax):",GST)
Amt=Total+GST
print("Amount to be paid:",Amt)
