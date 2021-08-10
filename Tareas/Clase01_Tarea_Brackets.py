# Brackets: Class 01 - Edgar Alexis González Amador - A01746540

def bracketsValidation(brackets):
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == '(' or brackets[i] == '[':
            stack.append(brackets[i])
            print('Stack with new element: ', stack)
        elif brackets[i] == ')':
            if not (stack.pop() == '('):
                print('Invalid closure')
                break
            else:
                print('closed () in stack: ', stack)
        elif brackets[i] == ']':
            if not (stack.pop() == '['):
                print('Invalid closure')
                break
            else:
                print('closed [] in stack: ', stack)
    if len(stack) != 0:
        print('Invalid brackets')
    else:
        print('Correct brackets!!!')

bracketsValid = "([])()()()()"
bracketsInvalid = "(((()(((((("

bracketsValidation(bracketsValid)
print('-----------------------------------------------------')
bracketsValidation(bracketsInvalid)