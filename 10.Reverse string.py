
# function to reverse a string. I have used this slice sentax before in part 7 of the problem sheet.

def str_reverse(str1):
    return str1[::-1] #reverses the string

str1 = input("Please enter a word? ").lower()

print(str_reverse(str1)) #prints string 