        # average program for dynamic no of students

marks=[];
print ("average program for dynamic no of student");
num= int(input("enter the no of student: "));
for i in range(0,num):
    a= int(input("enter the marks: "));
    marks.append(a);
avg= sum(marks)/num;
print ("avarage: ",avg);