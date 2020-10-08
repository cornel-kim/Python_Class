#nested if else statement

Age = int(input("Input your age:"))
if Age > 17:
    print("Can donate blood")
    weight = float(input("Please input your weight:"))
    if weight < 55:
        print("Your age is more than 17 years hence can donate but you weight is less hence not eligible")
    else:
        print("Both you age and weight meet the required criteria for blood donations hence proceed to donate")
else:
    print("You are not eligible")