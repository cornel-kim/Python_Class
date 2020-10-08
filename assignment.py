# 1. Create a Python Program to find Body Mass Index.  (Formula. weight/height squared)
# 2. Create a Python Program to find the Simple Interest.   (Formula. PRT/100).

#question 1
weight = float(input("Please Input your weight:"))
height = float(input("Please input your height:"))
BMI = weight/(height * height)
print("You BMI is", BMI)

#question 2
P = int(input("Please add the principle amount:"))
R = 0.12
T = float(input("Add time"))
simple_interest = (P*R*T)/100
print("The simple interest is:", simple_interest)
