# if else, elif statements
student_name = input("Input your name:")
student_average_mark = float(input("Please input your average mark:"))
if 0 <= student_average_mark <= 30:
    print("You scored an E")
elif 30 < student_average_mark <= 40:
    print("You scored a D")
elif 40 < student_average_mark <= 50:
    print("You scored a C")
elif 50 < student_average_mark <= 60:
    print("You scored a B")
elif 60 < student_average_mark <= 90:
    print("You scored a A")
elif 90 < student_average_mark <= 100:
    print("You scored a A+")
else:
    print("Input valid average marks")
