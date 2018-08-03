        # leap year program

print ("Leap Year Program");
num=  input("enter  the number: ");
if num == 0:
    exit();
try:
    year = int(num);
except valueError:
    print ("Please enter correct form of year\n");
else:
    if ((year%4 == 0) and (year%100 != 0)):
        print (year," is a leap year.");
    elif ((year%100 == 0) and (year%400 == 0)):
        print (year," is a leap year.");
    elif (year%400 == 0):
        print (year," is a leap year.");
    else:
        print (year," is not leap year");


        