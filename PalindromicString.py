'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
# Write your code here
 
def isPalindrome(a): 
    return a == a[::-1] 
 
a = str(input())
result = isPalindrome(a) 
  
if result: 
    print("YES") 
else: 
    print("NO")
