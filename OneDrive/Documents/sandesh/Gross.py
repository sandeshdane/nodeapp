bsal=int(input("Enter your salary: "))

if(bsal<=10000):
    hra= (bsal*20)//100
    da= (bsal*80)//100
elif (bsal>=20000):
    hra= (bsal*25)//100
    da=(bsal*90)//100
else:
    hra= (bsal*30)//100
    da= (bsal*95)//100
gross_sal= bsal+hra+da
print("Gross Salary: ", gross_sal)