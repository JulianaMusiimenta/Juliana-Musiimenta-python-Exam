#3(i)
name =int( input("Enter your name:. "))
age = int(input("Enter your age:. "))


if age>=18:
    print("you are eligible")
else:
    print("you are not eligible")



#3(ii)
def grade_students(mark):

    #capture student mark
    mark = int(input('Enter mark scored:.'))

    #testing student mark
    if mark>=90 and mark<=100:
        print("Grade is A")

    elif mark>=80 and mark<=89:
        print("Grade is B")

    elif mark>=70 and mark<=79:
        print("Grade is C")

    elif mark>=60 and mark<=69:
        print("Grade is D")

    else:
        print("F")
grade_students()

#3(iii) Testing the function with a mark of 85
mark = 85
grade_students(mark)
print(f"For a mark of {mark} is.")


#3(iv)


#3(V)
def grade_students (mark):
    if mark >=90 and mark<= 100:
        grade = "A"
        message = "Excellent"
    elif mark >=80 and mark<= 89:
        grade = "B"
        message = "Excellent"
    elif mark >= 70 and mark<= 79:
        grade = "C"
        message = "Good"
    elif mark >= 60 and mark<= 69:
        grade = "D"
        message = "Satisfactory"
    else:
        grade = "F"
        message = "Needs Improvement"
    return grade, message

#3(iv)
# Testing the function with a mark of 78
mark = 78
grade, message = grade_students(mark)
print(f"For a mark of {mark}, the grade is {grade} and the message is '{message}'.")