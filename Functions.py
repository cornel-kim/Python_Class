#functions is a set of codes that a user creates to do a specific ativity i.e to calculate marks aor average and allows code reusability
def studentsMarks():
    studentName = str(input("Input your name:"))
    SubEng = int(input("Input Your English marks"))
    SubMath = int(input("Input Your Math marks"))
    SubKisw = int(input("Input Your Kiswahili marks"))
    totalMarks = SubKisw + SubEng + SubMath
    print("Your total marks", totalMarks)


studentsMarks()