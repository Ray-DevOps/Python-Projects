# In this project, we create a simple calculator that can do additions, subtractions, multiplications, and divisions.
# The calculator should be able to work with both round numbers and numbers with decimals
# The user should be able to do a calculation, and then use the answer to do another calculation
# Therefore the calculator should ask the user after each calculation whether they want to continue calculating
# If user says 'yes', then the answer of the previous calculation becomes input value for their new calculation
# If user says 'no', then the calculator resets and user is prompted to enter new values from start.

def calculator():
    num1 = float(input("Please enter the first number: "))
    op = input("Please enter an operator: ")
    num2 = float(input("Please enter the second number: "))

    continue_calcution = True

    if op == '+':
        answer = num1 + num2
    elif op == '-':
        answer = num1 - num2
    elif op == '*':
        answer = num1 * num2
    else:
        answer = num1 / num2

    print(f"{num1} {op} {num2} = {answer}")

    while continue_calcution == True:
        proceed = (input("Will you like to continue calculations? 'yes' or 'no': ")).lower()
        if proceed == 'yes':
            new_op = input("Pick an operator. '+', '-', '*', '/': ")
            new_num2 = float(input("enter number: "))
            if new_op == '+':
                new_answer = answer + new_num2
            elif new_op == '-':
                new_answer = answer - new_num2
            elif new_op == '*':
                new_answer = answer * new_num2
            else:
                new_answer = answer / new_num2
            print(f"{answer} {new_op} {new_num2} = {new_answer}")
        else:
            continue_calcution = False
            print("Operation exited")
            calculator()
        answer = new_answer

calculator()
