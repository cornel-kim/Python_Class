#control statements examples are the if else statements, elif, and nested if else

studentName = str(input("Please input your name:"))
studentMarks = float(input("Please input your marks:"))
#if else statement
# if studentMarks < 250:
#     print("Below average marks")
#
# else:
#     print("You excelled")
#elif statement
# if studentMarks < 250:
#     print("Below average marks")
#
# elif 250 <= studentMarks < 350:
#     print("You are an average student")
#
# elif 350 <= studentMarks < 500:
#     print("You are an excellent student")
#
#
# else:
#     print("Input valid marks")

#nested else if statement
if studentMarks < 250:
    gender = input("Input your gender")
    if gender == "Male":
        print("A boy should perform better")
    elif gender == "Female":
        print("A girl should work better")
    else:
        print("Input valid gender")
else:
    print("you excelled")























