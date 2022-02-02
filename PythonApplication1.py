def plus():
    return a + b

def min():
    return a - b

def umn():
    return a * b

def dele():
    return a / b
while True:
    c = input()
    a = int(input())
    b = int(input())

    if c == '+':
        print(plus())
    elif c == '-':
        print(min())
    elif c == '*':
        print(umn())
    elif c == '/':
        try:
            print(dele())
        except ZeroDivisionError:
            print('на ноль делить нельзя')
    elif c == '0':
        break
    else:
        print('нет такой операции')
    

