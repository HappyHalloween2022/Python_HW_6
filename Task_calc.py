# # 41. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции
# # +, -, /, *. Приоритет операций стандартный.


# def add(a, b):
#     return a + b


# def diff(a, b):
#     return a - b


# def mult(a, b):
#     return a * b


# def delim(a, b):
#     return a / b


# def app(txt):
#     sign = ''
#     for s in '+-*/':
#         if s in txt:
#             sign = s
#         break
#         if sign == '':
#          int(txt)
#         else:
#             a, b = txt.split(sign)
#     if sign == '*': return mult(app(a), app(b))
#     elif sign == '/': return delim(app(a), app(b))
#     elif sign == '+': return add(app(a), app(b))
#     elif sign == '-': return diff(app(a), app(b))


    # Very-very simple calc

expr = input()

def calc(expr):
    operator_function = {
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    nums = list()
    opers = list()

    tokens = list('(' + expr + ')')

    while tokens:
        token = tokens.pop(0)

        if token.isdecimal():
            nums.append(float(token))
        else:
            if token == ')':
                oper = opers.pop()
                while opers and oper != '(':
                    b, a = nums.pop(), nums.pop()
                    f = operator_function[oper]
                    nums.append(f(a, b))

                    oper = opers.pop()

            else:
                opers.append(token)

    return nums[0]


# if __name__ == '__main__':
    # print(calc("((1+(2*3))*2)+4"))  # 18.0
    # print(calc("(1*(3/2))+4"))  # 5.5
    # print(calc("(2*(3/2))+4"))  # 7.0

print(int(calc(expr)))