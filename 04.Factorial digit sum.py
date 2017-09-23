# Write a function that calculates the sum of the digits of the factorial of a number. 
# n! means n x (n − 1) ... x 3 x 2 x 1. For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
#  and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. 
# Find the sum of the digits in the number 100!

def factorial(n):
    x = n
    for i in range(1, n):
        x = x*(n-i)
    return x


sumOfDigits = sum(int(digit) for digit in str(factorial(100))) # gets the number of digits in string 


print("The sum of digits for factorial 100 is " +str(sumOfDigits))   # Prints answer 

# this should be printed out 
#The sum of digits for factorial 100 is 648
