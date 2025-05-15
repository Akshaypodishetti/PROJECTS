#Calculator

"""
step 1 = define a function
step 2 = user input
step 3 = call a function
step 4 = use conditional statements
"""

#functions
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

def average(num1,num2):
    return (num1 + num2)/2

print("The functions are:\n" \
      "1.addition\n"\
      "2.subraction\n"\
      "3. multiplication\n"\
      "4.division\n"\
      "5.average\n"\
        )

#user input
user_input = int(input("Which function you want to call 1,2,3,4,5 : "))
select1 = int(input("enter a value to calculate : "))
select2 = int(input("enter a value to calculate : "))

#user call
if user_input == 1:
    print(f"{select1} + {select2} = {add(select1,select2)}")
elif user_input == 2:
    print(f"{select1} - {select2} = {sub(select1,select2)}")
elif user_input == 3:
    print(f"{select1} * {select2} = {multiply(select1,select2)}")
elif user_input == 4:
    print(f"{select1} / {select2} = {division(select1,select2)}")
elif user_input == 5:
    print(f"{select1} + {select2} / 2 = {round(average(select1,select2))}")
else:
    print("invalid operation!!")

