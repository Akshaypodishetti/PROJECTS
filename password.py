import random
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l',
           'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','&','*','(','+',"-"]
print("Welcome to password generator!")
num_letters = int(input("How many letters would you want in your password:\n"))
num_numbers = int(input("How many numbers would you want in your password:\n"))
num_symbols = int(input("How many symbols would you want in your password:\n"))
password_list = []
for i in range(1,num_letters+1):
    char = random.choice(letters)
    password_list +=char

for i in range(1,num_numbers+1):
    char = random.choice(numbers)
    password_list +=char

for i in range(1,num_symbols+1):
    char = random.choice(symbols)
    password_list +=char
    
print(password_list)
random.shuffle(password_list)
print(password_list)
password = " "
for char in password_list:
    password += char
print(password)

