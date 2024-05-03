'''i=1
while i<=50:
     if(i%2==0):
        print(i)
     i +=1
     
     
     
     num=int(input("Enter a number: "))
     i=1
     while i<=num:
         if(num%i==0):
             print(i)'''
             
             
             
def sum_of_digits(number):
    
    number_str = str(number)
    
    
    digit_sum = 0
    for digit in number_str:
        digit_sum += int(digit)
    
    
    print("Sum of digits:", digit_sum)


input_number = int(input("Enter a number: "))
sum_of_digits(input_number)
