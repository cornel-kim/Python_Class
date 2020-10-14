#we have parameters and arguments
def addition():
    x = 7
    y = 6
    answer = x + y
    if answer > 5:
        return "The number is greater than 5"
    else:
        return "The answer is less than 5"


returned_answer = addition()
print('The answer is', returned_answer)

print(returned_answer)


def addition2(x, y):#x and y are parameters
    answer = x + y
    print('addition2 answer is', answer)


addition2(x=7, y=6)#arguments
addition2(x=10, y=12)


def payroll(basic, allowances):
    print("Basic salary is", basic)
    print("Allowance is", allowances)
    gross_Salary = basic + allowances
    return gross_Salary


x = payroll(basic=30000, allowances=2000)
print("Your Gross salary is", x, 'KSH')

#create a function with parameters and arguments that calculates student average marks for subject eng, kisw and math