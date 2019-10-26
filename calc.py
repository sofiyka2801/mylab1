x = float(input('перше число:'))
y = float(input('друге число:'))
operation = input('операція:')

result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result =x - y
elif operation == '/':
    result = x / y
elif operation == '*':
    result = x * y
else:
    print('Unsupported operation')

if result is not None:7
    print('результат:', result)
