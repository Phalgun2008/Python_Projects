     # Marks Store
a = int(input("Enter Marks of Maths = "))
b = int(input("Enter Marks of Science = "))
c = int(input("Enter Marks of Social Science = "))

     # Calculate-Marks
def Total_Marks(a,b,c):
     sum = a+b+c
     print(sum)
     return sum

     # print Total Marks
print("Total Marks",end=(" = "))
Total_Marks(a,b,c)

     #Calculate-Percentage
def Percentage(a,b,c):
     sum = float(((a+b+c)/300)*100)
     print(sum)
     return sum

Value_assign = Percentage(a,b,c)

     # print Total Percentage
print("Percentage",end=(" = "))
Percentage(a,b,c)

     # Conditions for Marks-Grade
if (Value_assign >= 95 or (Value_assign >= 100)):
     print("Exelent")
     
elif(Value_assign >= 80 or (Value_assign >= 90)):
     print("Grade - A")
     
elif(Value_assign >= 70 or (Value_assign >= 80)):
     print("Grade - B")
     
elif(Value_assign >= 60 or (Value_assign >= 70)):
     print("Grade - C")
     
elif(Value_assign >= 50 or (Value_assign >= 60)):
     print("Grade - D")
     
elif(Value_assign >= 33 or (Value_assign >= 45)):
     print("Grade - E")
     
else:
     Value_assign >= 32
     print("Fail")
     
     # Condition for Supplementary Subject
if a <= 32 and b <= 32 and c <= 32:
     print("Supplementary in Maths,Science,Social-Science")
     
elif a <= 32 and b <= 32 and c >= 32:
     print("Supplementary in Maths,Science")
     
elif a >= 32 and b <= 32 and c <=32:
     print("Supplementary in Science,Social-Science")
     
elif a <= 32 and b >= 32 and c <= 32:
     print("Supplementary in Maths,Social-Science")
     
elif a <= 32:
     print("Supplementary in Maths")
     
elif b <= 32:
     print("Supplementary in Science")
     
elif c <= 32:
     print("Supplementary in Social-Science ")
     
else:
     print("For any Help = +91 97837xxxxx")
     
     pass