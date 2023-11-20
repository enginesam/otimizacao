# intervalo [a,b]
a = 1 
b = 10

n=1
eps = 0.1 # intervalo de incerteza
phi = ((5**(1/2)+1)/2)

def f(x):
    return x**4-2*x**2-4*x+3

c = b + (a-b)/phi
d = a + (b-a)/phi

while b-a >= eps: 
    if f(c)<f(d): 
        b = d
        d = c
        c = b + (a-b)/phi 
    
    else: 
        a = c
        c = d 
        d = a + (b-a)/phi

x_min  = (a+b)/2
y_min = f(x_min)

print(f'Valor mínimo: {round(y_min,3)}')

