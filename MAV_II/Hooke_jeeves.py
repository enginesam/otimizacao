import numpy as np

# Ponto de partida  
x1 = np.array([0,0])

def hooke_jeeves(x1):
    n = 2  # numero de direções coordenadas 
    p = 1.0 # passo 
    eps = 0.1 # criterio de parada 
    alpha = 1.0 # fator de aceleração

    d1 = np.array([1,0])
    d2 = np.array([0,1])
    y = x1
    x = x1
    d = [d1,d2]
    itt= 0 


    def f(x1):
        x = x1[0]
        y = x1[1]  
        return 3*x**2 + 2*y**2 - 4*x*y - 3*x - 7*y + 10

    while p > eps:
        for i in range(n):
            if f(y + p*d[i]) < f(y): 
                y = y + p*d[i]
            elif f(y - p*d[i]) < f(y):
                y = y - p*d[i]

            else: 
                y = y 
        
        if f(y) < f(x):
            x_ant = x
            x = y 
            y = x + alpha*(x - x_ant)

        else: 
            p *= 1/2
            y = x

        itt +=1

    return x[0],x[1],f(x),itt

x,y,min,itt = hooke_jeeves(x1)

print(f'x:{x}')
print(f'y:{y}')
print(f'Mínimo:{min}')
