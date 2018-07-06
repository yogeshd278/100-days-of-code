	# reverse string program
print("for exit enter 0")
string = input("Enter the string to reverse it: ")
if string == '0':
    exit()
else:
    revstring = string[::-1]
    print("\nstring =",string)
    print("reverse string =",revstring)