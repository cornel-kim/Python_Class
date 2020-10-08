# def marks():
#     marks = 45
#     if marks < 50:
#         print("You failed")
#     else:
#         print("You passed")
#
# marks()

# def simpleInterest():
#     Basic_amount = 3000
#     number_years = 3
#     total_interest = (Basic_amount * number_years) * 0.15
#     print("Total interest accrued is equals to", total_interest)
#
#
# simpleInterest()

def my_shop(tax, name, money, balance):#assign parameters
    total = money - balance
    print("You available balance is :", total)
    print("Money given is:", money)
    print("The tax is:", tax)
    print("Shoopkeeper name is:", name)
    print("The balace is:", balance)


#assign arguments
my_shop(tax=2.5, name='Ann', money=4000, balance=200 )
my_shop(tax=2.5, name='Tom', money=6000, balance=600 )