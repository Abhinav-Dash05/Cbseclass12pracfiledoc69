def add(k,y):
    print('Sum: ', k+y)
def subtract(k,y):
    print('Difference: ', k-y)
def multiply(k,y):
    print('Product: ', k*y)
def divide(k,y):
    print('Quotient: ', k//y, 'Remainder: ', k%y)
print('''Press:
+ for addition
- for subtraction
* for multiplication
/ for division''')
op = input()
k = int(input("Enter Number a: "))
y = int(input("Enter Number b: "))
if op == '+':
    add(k,y)
elif op == '-':
    subtract(k,y)
elif op == '*':
    multiply(k,y)
elif op == '/':
    divide(k,y)
else:
    print("Invalid Operation.")