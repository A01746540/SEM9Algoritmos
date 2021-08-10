# Brackets: Class 01 - Edgar Alexis González Amador - A01746540

# Recibes una string conteniendo solo () y []
# Crea un algoritmos para validar que la sintaxis de los corchetes es correcta:
# Ejemplos validos:
# '()'
# '()()()()()()()()()'
# '([])[]()'
# Ejemplos no validos:
# ')'
# '()['
# '(([))]'
# '(((((((((((((((((((((((((((((((((('

def bracketsSimpleValidation(brackets):
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == '(' or brackets[i] == '[':
            stack.append(brackets[i])
        elif brackets[i] == ')':
            try:
                if not (stack.pop() == '('):
                    break
            except:
                stack.append(brackets[i])
                break
        elif brackets[i] == ']':
            try:
                if not (stack.pop() == '['):
                    break
            except:
                stack.append(brackets[i])
                break
    if len(stack) != 0:
        print('Invalid brackets :', brackets)
    else:
        print('Correct brackets!:', brackets)

print('Examples with simple validation')
bracketsSimpleValidation('()')
bracketsSimpleValidation('()()()()()()()()()')
bracketsSimpleValidation('([])[]()')
bracketsSimpleValidation(')')
bracketsSimpleValidation('()[')
bracketsSimpleValidation('()[')
bracketsSimpleValidation('(([))]')
bracketsSimpleValidation('((((((((((((((((((((((((((((((((((')

print('\n/////////////////////////////////////////////////////\n')

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

print('Examples step-by-step')

bracketsValid = "([])()()()()"
bracketsInvalid = "(((()(((((("

bracketsValidation(bracketsValid)
print('-----------------------------------------------------')
bracketsValidation(bracketsInvalid)