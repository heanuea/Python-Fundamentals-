
#Write a function that returns the largest and smallest Number in a list.

lst = []        #Array list 

num = int(input('How many numbers: '))      #Input number

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

#print outs numbers 
print("Maximum Number in the list is : %d" % max(lst))
print("Minimum Number in the list is : %d" % min(lst))