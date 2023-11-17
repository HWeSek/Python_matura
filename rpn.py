#odwrotna notacja polska 2 4 +

def calculateRPN(expression):
    stack=[]
    operators = {'+','-','*','/'}
    tokens = expression.split()

    for token in tokens:
        if token not in operators:
            stack.append(float(token))
        else:
            if len(stack) < 2:
                raise ValueError('Niewystarczająco operdandów dla operatora')
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a+b
            elif token == '-':
                result = a-b
            elif token == '*':
                result = a*b
            elif token == '/':
                if b==0:
                    raise ValueError('Dzielenie przez zero')
                result = a/b
            stack.append(result)
    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError('Zła ilość operatorów')

expression1 = '3 4 + 2 *'
print(calculateRPN(expression1))
