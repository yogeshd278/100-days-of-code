    # factor program
   
x = int(input('enter the no to find factor '))
print("The factors of",x,"are:")
for i in range(1, x + 1):
    if x % i == 0:
        print(i)
