def calculator(num1, num2):
    add = num1 + num2
    subtract = num1 - num2
    divide = num1 / num2
    multiply = num1 * num2
    if op1 == '+':
        return add
    elif op1 == '-':
        return subtract
    elif op1 == '/':
        return divide
    elif op1 == '*':
        return multiply
    else:
        print('Invalid input. ')


active = True
while active:
    num_1 = float(input('Please enter a number: '))
    op1 = input('Please enter an operator (+*/-):')
    num_2 = float(input('Please enter a second number: '))

    result = calculator(num_1, num_2)
    print(result)

    repeat = input('Would you like to enter another calculation? (yes/no): ')
    if repeat == 'no':
        active = False
        print('Thanks for using my calculator. ')




