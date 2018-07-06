    # factorial program without recursion
i, num, fact = 0, 0, 1
print ("factorial program\n")
num = int(input('enter the no\t'))
for i in range(1,num+1):
    fact = fact * i
print (fact)
