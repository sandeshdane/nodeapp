days= int(input("Enter no of days: "))
year= days//365
print("years: ", year)
rem1_days= days%365
month= rem1_days//30
print("Month: ", month)
rem2_days= rem1_days%30
week= rem2_days//7
print("weeks: ", week)
rem3_days= rem2_days%7
print("Days: ",days)