# Optimised Palindrome.py
n = int(input())
if(n<=1000):
    # convert integer to string
    s = str(n) 
    # reverse the string using string slicing 
    # and compare the two strings
    if(s == s[::-1]):
        print("yes")
    else:
        print("no")
else:
    print("invalid")
