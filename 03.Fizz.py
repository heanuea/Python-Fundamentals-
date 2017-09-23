#  Write a program that prints the numbers from 1 to 100, except for the following conditions.
#  For multiples of three print “Fizz” instead of the number, and for the multiples of five print “Buzz”.
#  For numbers which are multiples of both three and five print “FizzBuzz”.


for A in range (1, 101):            #loops threw the numbers 
    if A % 3 == 0 and A % 5 == 0:       #Divisble by 3 and 5 
        print ("FizzBuzz")

    elif A % 3 == 0:                #Divisble by 3
        print ("Fizz")

    elif A % 5 == 0:                #Divisble by 5
        print ("Buzz")

    else:
        print (A)                   #print outcome