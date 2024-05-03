m1=int(input("Enter marks of subject1:"))
m2=int(input("Enter marks of subject2:"))
m3=int(input("Enter marks of subject3:"))
m4=int(input("Enter marks of subject4:"))
m5=int(input("Enter marks of subject5:"))
sum = m1+m2+m3+m4+m5
percentage = (sum/500)*100
print("Total marks: ",sum )
if(percentage>=90):
     print("Grade A")
elif percentage>=80:
     print("Grade B")
elif percentage>=70:
     print("Grade C")
elif percentage>=60:
     print("Grade D")
elif percentage>=50:
     print("Grade E")
     
else:
    print("fail")
    