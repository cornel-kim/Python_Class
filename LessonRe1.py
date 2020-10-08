#python loops
#while loop


# x = 0
# while x < 10:
#     print(x)
#     x += 1
#     # if x > 4:
#     #     continue
#     # else:
#     #     break
from pythonfunctionsre import my_shop

for x in range(1, 10, 2):
    print(x)


fruits = ('apples', 'mangoes', 'Mango', 'Passion')
for fruit in fruits:
    print(fruit)
    if fruit == 'mangoes':
        print("We found mangoes")
        break
    else:
        continue


marks = [25, 40, 45, 67, 87]
names = ['john', 'Peter', 'Mark', 'Halima']
#slicing
print(marks[2])
print(marks[0:2])
print(marks[-1])
print(marks[3:])
#add two lists together
print(marks + names)
#add an item to an existing list
names.append('Anita')
names.append('Paul')
print(names)


my_shop(tax=2.5, name='john', money=5000, balance=300 )
