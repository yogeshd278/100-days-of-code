    #factorial program with recursion
def rec_fact(n):
   "recursion function"
   if n == 1:
       return n
   else:
       return n*rec_fact(n-1)

num = int(input('enter the no '))
if num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"=",rec_fact(num))