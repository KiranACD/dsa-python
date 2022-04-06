import operator
operator_precedence_mapping = {'+':1, '-':1, '*':2, '/':3, '(':0, ')':0}

operator_function = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

def check_precedence(operator1, operator2):

    return operator_precedence_mapping[operator1] > operator_precedence_mapping[operator2]
    
def infix_to_postfix(string):

    operator_stack = []
    top = -1
    new_string = ''
    
    for s in string:
        if s in operator_precedence_mapping:
            if top == -1:
                operator_stack.append(s)
                top += 1
            else:
                if s == '(':
                    operator_stack.append(s)
                    top += 1
                elif s == ')':
                    while True:
                        x = operator_stack.pop(top)
                        if x == '(':
                            top -= 1
                            break
                        new_string += x
                        top -= 1

                elif check_precedence(s, operator_stack[top]):
                    operator_stack.append(s)
                    top += 1
                else:
                    while (top != -1) and (check_precedence(s, operator_stack[top]) == 0):
                        x = operator_stack.pop(top)
                        top -= 1
                        new_string += x
                    operator_stack.append(s)
                    top += 1
        else:
            new_string += s
        
    while (top != -1):
        new_string += operator_stack.pop(top)
        top -= 1
    
    return new_string

def solve_postfix_expression(string):

    sol_stack = []
    top = -1
    ans = 0
    for s in string:
        if s not in operator_precedence_mapping:
            sol_stack.append(int(s))
            top += 1
        else:
            x1 = sol_stack.pop(top)
            top -= 1
            x2 = sol_stack.pop(top)
            top -= 1
            x = operator_function[s](x2, x1)
            sol_stack.append(x)
            top += 1
    return x
            

def evaluate_expression():

    string = input('Enter the expression you want to evaluate: ')
    string = string.replace(' ', '')
    print(string)

    string = infix_to_postfix(string)
    print(string)
    ans = solve_postfix_expression(string)
    return ans

if __name__ == '__main__':

    print(evaluate_expression())
