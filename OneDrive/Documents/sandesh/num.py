'''num=int(input("Enter a number: "))
num1=num 
cnt=0
while num > 0:
   num= num//10
   cnt +=1
print(num, "is", cnt, "digit number")'''





def reverse_number(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
    return reversed_number


try:
    user_input = int(input("Enter a number: "))
    reversed_result = reverse_number(user_input)
    print("Reversed number:", reversed_result)
except ValueError:
    print("Please enter a valid integer.")
