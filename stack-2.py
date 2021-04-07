userinput = input('Please Enter the String   --  ')

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

operators = ['+', '-', '*', '/']
stack = []


def mathOperation(input):
    for i in range(len(input)):

        if input[i] in operators:
            stack.append(input[i])

        if input[i] in numbers:
            if len(stack) == 0:
                stack.append(input[i])

            elif stack[-1] in operators:
                operator = stack.pop()

                try:
                    pre_number = float(stack.pop())
                except:
                    print('Error')
                if operator == '+':
                    pre_number
                    sum = pre_number + float(input[i])
                    stack.append(sum)
                if operator == '-':
                    diffrence = pre_number - float(input[i])
                    stack.append(diffrence)
                if operator == '*':
                    product = pre_number * float(input[i])
                    stack.append(product)
                if operator == '/':
                    div = pre_number / float(input[i])
                    stack.append(div)
    return stack


print(mathOperation(userinput))
