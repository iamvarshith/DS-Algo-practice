# check the parenthesis in the given string

input = input('Enter the string to with the given brackets')

stack = []


# types of brackets () [] {}
def checkIndentOfBrackets(input):
    for i in range(len(input)):
        if input[i] == '[':
            stack.append('[')

        if input[i] == ']':
            if len(stack) !=0 and stack[len(stack)-1] == '[':
                stack.pop()
            else:
                stack.append(']')

        if input[i] == '(':
            stack.append('(')

        if input[i] == ')':
            if len(stack) !=0 and stack[len(stack)-1] == '(':
                stack.pop()
            else:
                stack.append(')')

        if input[i] == '{':
            stack.append('{')

        if input[i] == '}':
            print(len(stack))
            if len(stack) !=0 and stack[len(stack)-1] == '{':
                stack.pop()
            else:
                stack.append('}')

    return stack


if len(checkIndentOfBrackets(input)) == 0:
    print('yay')
else:
    print('there is a mistake')

