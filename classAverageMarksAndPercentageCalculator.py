

print("This script will take input from user to put student profile and it will you an awesome result")


class profile:

    def __init__(self,firstname,lastname,age):             #Object intances
        self.firstname=firstname                            #Object intances
        self.lastname=lastname                                #Object intances
        self.age=age


    def fullname(self):
        return "{} {}".format(self.firstname,self.lastname)


        
student1 = profile(input("First Name: "), input("Last Name: "), input("Age: "))     #student1 object
student2 = profile(input("First Name: "), input("Last Name: "), input("Age: "))     #student2 object
student3 = profile(input("First Name: "), input("Last Name: "), input("Age: "))     #student3 object
student4 = profile(input("First Name: "), input("Last Name: "), input("Age: "))     #student4 object
student5 = profile(input("First Name: "), input("Last Name: "), input("Age: "))     #student5 object
student6 = profile(input("First Name: "), input("Last Name: "), input("Age: "))     #student6 object
student7 = profile(input("First Name: "), input("Last Name: "), input("Age: "))     #student7 object
student8 = profile(input("First Name: "), input("Last Name: "), input("Age: "))     #student8 object
student9 = profile(input("First Name: "), input("Last Name: "), input("Age: "))     #student9 object
student10 = profile(input("First Name: "), input("Last Name: "), input("Age: "))    #student10 object

print("RECORDS")

ob_list = []


def totalaverage(n):
    a = n/10
    return a


try:                                                #Try-except is using now

    tm = int(input("Total Marks: "))

except Exception as e:                              #Try-exception is using now

    print("Error here. Please write a integer")
    tm = int(input("Total Marks: "))

print("Now, enter obtained marks for 10 students")



for i in range(10):                              # loops are using now




    try:
        ob_marks = int(input("Obtained Marks: "))       #Try-except is using again
    except Exception as e:
        print("Error here. Please write a integer")     #Try-except is using
        ob_marks = int(input("Obtained Marks: "))


    if ob_marks<=tm:
        ob_list.append(ob_marks)

    else:
        print("Please enter marks below than",tm)
        ob_marks = int(input("Obtained Marks: "))
        if ob_marks<=tm:
            ob_list.append(ob_marks)
    

obtained_marks_list = [x for x in ob_list]         #list comprehension method 


dic = {x:x for x in ob_list}                       #dictionary comprehension method

totalmarks = 0

for i in obtained_marks_list:                    #loops
    totalmarks+=i
#percentage
st1 = ob_list[0]/tm*100
st2 = ob_list[1]/tm*100
st3 = ob_list[2]/tm*100
st4 = ob_list[3]/tm*100
st5 = ob_list[4]/tm*100
st6 = ob_list[5]/tm*100
st7 = ob_list[6]/tm*100
st8 = ob_list[7]/tm*100
st9 = ob_list[8]/tm*100
st10 = ob_list[9]/tm*100





st1_record = "Name of student:",student1.fullname(), "Age:", student1.age,"Obtained marks:",ob_list[0],"Percentage:",st1 
st2_record= "Name of student:",student2.fullname(), "Age:", student2.age,"Obtained marks:",ob_list[1],"Percentage:",st2
st3_record= "Name of student:",student3.fullname(), "Age:", student3.age,"Obtained marks:",ob_list[2],"Percentage:",st3
st4_record= "Name of student:",student4.fullname(), "Age:", student4.age,"Obtained marks:",ob_list[3],"Percentage:",st4
st5_record= "Name of student:",student5.fullname(), "Age:", student5.age,"Obtained marks:",ob_list[4],"Percentage:",st5
st6_record= "Name of student:",student6.fullname(), "Age:", student6.age,"Obtained marks:",ob_list[5],"Percentage:",st6
st7_record= "Name of student:",student7.fullname(), "Age:", student7.age,"Obtained marks:",ob_list[6],"Percentage:",st7
st8_record= "Name of student:",student8.fullname(), "Age:", student8.age,"Obtained marks:",ob_list[7],"Percentage:",st8
st9_record= "Name of student:",student9.fullname(), "Age:", student9.age,"Obtained marks:",ob_list[8],"Percentage:",st9 
st10_record= "Name of student:",student10.fullname(), "Age:", student10.age,"Obtained marks:",ob_list[9],"Percentage:",st10 

print("Results")

print(st1_record)
print(st2_record)
print(st3_record)
print(st4_record)
print(st5_record)
print(st6_record)
print(st7_record)
print(st8_record)
print(st9_record)
print(st10_record)


print("POSITION")

perlist = [st1,st2,st3,st4,st5,st6,st7,st8,st9,st10]
maxmarks = 0



for i in perlist:
    if i>=maxmarks:
        maxmarks=i

index1 = perlist.index(max(perlist))

perlist = [st1,st2,st3,st4,st5,st6,st7,st8,st9,st10]
perlist.remove(max(perlist))
sec_highest = max(perlist)
index2 = perlist.index(max(perlist))


perlist.remove(max(perlist))
third_highest = max(perlist)
index3 = perlist.index(max(perlist))


indexfin = [index1,index2,index3]
students = ["student1","student2","student3","student4","student5","student6","student7","student8","student9","student10"]

first_topper = students[indexfin[0]]
second_topper = students[indexfin[1]]
third_topper = students[indexfin[2]]


if first_topper=="student1":
    a = student1.fullname()
    print("Student Name:",a,"Percentage",maxmarks,"First Position in class")
elif first_topper=="student2":
    a = student2.fullname()
    print("Student Name:",a,"Percentage",maxmarks,"First Position in class")
elif first_topper=="student3":
    a = student3.fullname()
    print("Student Name:",a,"Percentage",maxmarks,"First Position in class")
elif first_topper=="student4":
    a = student4.fullname()
    print("Student Name:",a,"Percentage",maxmarks,"First Position in class")
elif first_topper=="student5":
    a = student5.fullname()
    print("Student Name:",a,"Percentage",maxmarks,"First Position in class")
elif first_topper=="student6":
    a = student6.fullname()
    print("Student Name:",a,"Percentage",maxmarks,"First Position in class")
elif first_topper=="student7":
    a = student7.fullname()
    print("Student Name:",a,"Percentage",maxmarks,"First Position in class")
elif first_topper=="student8":
    a = student8.fullname()
    print("Student Name:",a,"Percentage",maxmarks,"First Position in class")
elif first_topper=="student9":
    a = student9.fullname()
    print("Student Name:",a,"Percentage",maxmarks,"First Position in class")
if first_topper=="student10":
    a = student10.fullname()
    print("Student Name:",a,"Percentage",maxmarks,"First Position in class")



if second_topper=="student1":
    a = student1.fullname()
    print("Student Name:",a,"Percentage",sec_highest,"second Position in class")
elif second_topper=="student2":
    a = student2.fullname()
    print("Student Name:",a,"Percentage",sec_highest,"second Position in class")
elif second_topper=="student3":
    a = student3.fullname()
    print("Student Name:",a,"Percentage",sec_highest,"second Position in class")
elif second_topper=="student4":
    a = student4.fullname()
    print("Student Name:",a,"Percentage",sec_highest,"second Position in class")
elif second_topper=="student5":
    a = student5.fullname()
    print("Student Name:",a,"Percentage",sec_highest,"second Position in class")
elif second_topper=="student6":
    a = student6.fullname()
    print("Student Name:",a,"Percentage",sec_highest,"second Position in class")
elif second_topper=="student7":
    a = student7.fullname()
    print("Student Name:",a,"Percentage",sec_highest,"second Position in class")
elif second_topper=="student8":
    a = student8.fullname()
    print("Student Name:",a,"Percentage",sec_highest,"second Position in class")
elif second_topper=="student9":
    a = student9.fullname()
    print("Student Name:",a,"Percentage",sec_highest,"second Position in class")
if second_topper=="student10":
    a = student10.fullname()
    print("Student Name:",a,"Percentage",sec_hishest,"second Position in class")

if third_topper=="student1":
    a = student1.fullname()
    print("Student Name:",a,"Percentage",third_highest,"third Position in class")
elif third_topper=="student2":
    a = student2.fullname()
    print("Student Name:",a,"Percentage",third_highest,"third Position in class")
elif third_topper=="student3":
    a = student3.fullname()
    print("Student Name:",a,"Percentage",third_highest,"third Position in class")
elif third_topper=="student4":
    a = student4.fullname()
    print("Student Name:",a,"Percentage",third_highest,"third Position in class")
elif third_topper=="student5":
    a = student5.fullname()
    print("Student Name:",a,"Percentage",third_highest,"third Position in class")
elif third_topper=="student6":
    a = student6.fullname()
    print("Student Name:",a,"Percentage",third_highest,"third Position in class")
elif third_topper=="student7":
    a = student7.fullname()
    print("Student Name:",a,"Percentage",third_highest,"third Position in class")
elif third_topper=="student8":
    a = student8.fullname()
    print("Student Name:",a,"Percentage",third_highest,"third Position in class")
elif third_topper=="student9":
    a = student9.fullname()
    print("Student Name:",a,"Percentage",third_highest,"third Position in class")
if third_topper=="student10":
    a = student10.fullname()
    print("Student Name:",a,"Percentage",third_highest,"third Position in class")



average = totalaverage(totalmarks)

print("Your class average is: ",average)

if average>=80:
    print("This class performance is very good")

elif average<=40:
    print("This class performance is very poor")

if average>=60 and average<=80:
    print("This class performance is medium")
