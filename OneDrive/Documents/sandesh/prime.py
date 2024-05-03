'''def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

user_input = int(input("Enter a number: "))

if is_prime(user_input):
    print(f"{user_input} is a Prime Number.")
else:
    print(f"{user_input} is not a Prime Number.")'''
    
    
'''def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

display_primes(1, 100)'''

'''for i in range(0,5):
    for j in range(0,5):
        if(j==i):
           print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''
    
    
for i in range(0,5):
    for j in range(0,5):
        if(i+j>=4):
           print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
    

