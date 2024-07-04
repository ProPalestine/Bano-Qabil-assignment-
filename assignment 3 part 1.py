print('Enter your subject marks to find grade......')


subject1_marks = float(input("Enter  marks of math: 100 out of "))

subject2_marks = float(input("Enter marks of English: 100 out of "))

subject3_marks = float(input("Enter marks of urdu: 100 out of "))

subject4_marks = float(input("Enter marks of physics: 75 out of "))

subject5_marks = float(input("Enter marks of computer: 85 out of "))


total_marks = (subject1_marks + subject2_marks + subject3_marks + subject4_marks +subject5_marks)

print("total marks is 460 and you get ", total_marks)

x = (total_marks/460)*100

print("your percentage is ", x)

if x >= 90:
    grade = "A"
elif x >= 80:
    grade = "B"
elif x >= 70:
    grade = "C"
elif x >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)


