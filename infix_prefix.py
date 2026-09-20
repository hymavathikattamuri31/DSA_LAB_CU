def infix_to_prefix(expression):
    # Reversing the expression and swapping ths parentheses
    expression = expression[::-1]

    swapped = ""
    for x in expression:
        if x == '(':
            swapped += ')'
        elif x == ')':
            swapped += '('
        else:
            swapped += x

    # Converting the reversed expression to postfix
    stack = []
    output = []

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    for x in swapped:

        # for operand :
        if x.isalnum():
            output.append(x)

        # for opening parenthesis
        elif x == '(':
            stack.append(x)

        # for closing parenthesis
        elif x == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())

            if stack:
                stack.pop()

        # for operator:
        else:
            while (stack and stack[-1] != '(' and
                   precedence[x] < precedence[stack[-1]]):
                output.append(stack.pop())

            stack.append(x)

    # for empty the stack
    while stack:
        output.append(stack.pop())

    # Reversing the postfix to get prefix
    prefix = output[::-1]

    return ''.join(prefix)


# Taking the input from user :)
expression = input("Enter an infix expression: ")

print("Infix :", expression)
print("Prefix:", infix_to_prefix(expression))
