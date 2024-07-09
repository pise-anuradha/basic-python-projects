print('''
+ ADD
- SUB
* MUL
/ DIV
''')

num1 = int(input('Enter the Value1:'))
num2 = int(input('Enter the Value2:'))
opr = input('Enter the Operator:')

if opr == '+':
  print(num1+num2)
elif opr == '-':
  print(num1-num2)
elif opr == '*':
  print(num1*num2)
elif opr == '/':
  print(num1/num2)
else:
  print('Invalid Operator')
