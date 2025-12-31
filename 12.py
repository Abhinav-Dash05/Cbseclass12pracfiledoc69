def fibo():
    n = int(input('Enter the number: '))
    a = 0
    b = 1
    t = 0
    for i in range(0,n):
        t = a + b
        b = a
        a = t
        print(a, end = ' ')
    print()    
fibo()