userinput = '1+2(9+2+1)'

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

operators = ['+', '-', '*', '/', '(', ')']

stack = []


def mathOperation(userinput):
    i = 0

    while (i < (len(userinput))):

        if userinput[i] in numbers:
            stack.append(userinput[i])
        if userinput[i] in operators:
            if userinput[i] == '+':
                try:
                    if userinput[i + 2] != '(':
                        pre_number = stack.pop()

                        sum = float(pre_number) + float(userinput[i + 1])
                        stack.append(sum)
                        i += 1

                    if userinput[i + 2] == '(':
                        stack.append(userinput[i])
                        stack.append(userinput[i + 1])
                        i += 2
                except:
                    print('no values more')
            if userinput[i] == '-':
                try:
                    if userinput[i + 2] != '(':
                        pre_number = stack.pop()
                        diffrence = float(pre_number) - float(userinput[i + 1])
                        stack.append(diffrence)
                        i += 1

                    if userinput[i + 2] == '(':
                        stack.append(userinput[i])
                        stack.append(userinput[i + 1])
                        i += 2
                except:
                    print('no val')
            if userinput[i] == '*':
                try:
                    if userinput[i + 2] != '(':
                        pre_number = stack.pop()
                        product = float(pre_number) * float(userinput[i + 1])
                        stack.append(product)
                        i += 1

                    if userinput[i + 2] == '(':
                        stack.append(userinput[i])
                        stack.append(userinput[i + 1])
                        i += 2
                except:
                    print('no vals')
            if userinput[i] == '/':
                try:
                    if userinput[i + 2] != '(':
                        pre_number = stack.pop()
                        div = float(pre_number) / float(userinput[i + 1])
                        stack.append(div)
                        i += 1

                    if userinput[i + 2] == '(':
                        stack.append(userinput[i])
                        stack.append(userinput[i + 1])
                        i += 2
                except:
                    print('no vals')

            if userinput[i] == '(':
                stack.append(userinput[i])

            if userinput[i] == ')':
                in_bracket = stack.pop()
                stack.pop()
                if stack[-1] in numbers:
                    out_bracket = stack.pop()

                new_product = int(out_bracket) * int(in_bracket)

                if stack[-1] in operators:
                    if stack[-1] == '+':
                        stack.pop()
                        before_out_bracket = int(stack.pop())
                        final = before_out_bracket + new_product
                        stack.append(final)
                    if stack[-1] == '-':
                        stack.pop()
                        before_out_bracket = stack.pop()
                        final = before_out_bracket - new_product
                        stack.append(final)
                    if stack[-1] == '*':
                        stack.pop()
                        before_out_bracket = stack.pop()
                        final = before_out_bracket * new_product
                        stack.append(final)
                    if stack[-1] == '/':
                        stack.pop()
                        before_out_bracket = stack.pop()
                        final = before_out_bracket / new_product
                        stack.append(final)

        i += 1
    return stack


print(mathOperation(userinput))
