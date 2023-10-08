#  This is a program to automatically generate passwords for users. The program should interactively ask users:

#    - how many letters they would like to have in their passwords (and restrict them between 5 and 10 letters)?
#    - how many number they would like to have in their passwords (and restrict them between 5 and 10 numbers)?
#   - how many symbols they would like to have in their passwords (and restrict them between 5 and 10 symbols)?

#   If the user enters a number which is out of range, they should get a warning message and the question should repeat until
#   the user enters a number between 5 and 10.

#   The program should generate a password with the aforementioned combination of letters, symbols and numbers.
  
#   The password must be generated in a completed random order, meaning the letters doesn't necessarily have to come together and
#   don't necessarily have to come before the symbols or numbers. The password should be a random mix of numbers, letters, symbols.


#   letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
#             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#   numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#   symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



#  SOLUTION
# ================================================



import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_count = int(input("how many letters would you like to have in your passwords? (Minimum 5, maximum 10):\n"))
while letters_count not in [5, 6, 7, 8, 9, 10]:
    if 5 <= letters_count <= 10:
        pass
    else:
        print("Please enter a valid number between 5 and 10")
    letters_count = int(input("how many letters would you like to have in your passwords? (Minimum 5, maximum 10):\n"))

numbers_count = int(input("how many numbers would you like to have in your passwords? (Minimum 5, maximum 10):\n"))
while numbers_count not in [5, 6, 7, 8, 9, 10]:
    if 5 <= numbers_count <= 10:
        pass
    else:
        print("Please enter a valid number between 5 and 10")
    numbers_count = int(input("how many symbols would you like to have in your passwords? (Minimum 5, maximum 10):\n"))

symbols_count = int(input("how many symbols would you like to have in your passwords? (Minimum 5, maximum 10):\n"))
while symbols_count not in [5, 6, 7, 8, 9, 10]:
    if 5 <= symbols_count <= 10:
        pass
    else:
        print("Please enter a valid number between 5 and 10")
    symbols_count = int(input("how many symbols would you like to have in your passwords? (Minimum 5, maximum 10):\n"))

chosen_letters = random.sample(letters, k=letters_count)
chosen_numbers = random.sample(numbers, k=numbers_count)
chosen_symbols = random.sample(symbols, k=symbols_count)


password_content = chosen_letters + chosen_numbers + chosen_symbols

random.shuffle(password_content)

print(''.join(password_content))
