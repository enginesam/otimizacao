
# interavalo [a,b]
a = 1 
b = 10

n=1
eps = 0.2 # intervalo de incerteza

def f(x):
    return x**4-2*x**2-4*x+3

def fib(n):
    val1 = 1
    val2 = 1
    val3 = 1

    for i in range (n-1):
        val3 = val1 + val2
        val1 = val2
        val2 =val3

    return val3

while (b-a)/fib(n) > eps: 
    n +=1

c = a + (fib(n-2)/fib(n))*(b-a)
d = a + (fib(n-1)/fib(n))*(b-a)

while n !=2: 
    n -=1
    if f(c) < f(d):
        b = d 
        d = c
        c = a + (fib(n-2)/fib(n))*(b-a)
    
    else:
        a = c
        c = d 
        d = a + (fib(n-1)/fib(n))*(b-a)


x_min  = (a+b)/2
y_min = f(x_min)

print(f'Valor mínimo: {round(y_min,3)}')