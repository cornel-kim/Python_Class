def studentsMarks():
    studentName = str(input("Input your name:"))
    SubEng = int(input("Input Your English marks:"))
    SubMath = int(input("Input Your Math marks:"))
    SubKisw = int(input("Input Your Kiswahili marks"))
    totalMarks = SubKisw + SubEng + SubMath
    aveMark = totalMarks/3
    if aveMark<40:
        print("You have scored a D")
    elif 40 <= aveMark < 60:
        print("You scored a C")
    elif 60 <= aveMark < 80:
        print("You scored a B")
    elif 80 <= aveMark < 100:
        print("You scored a B")
    else:
        print("Invalid marks")


studentsMarks()


def studentFee():
    ttlFee = input("Input the total fee")
    print("Your total fee is", ttlFee)


studentFee()
