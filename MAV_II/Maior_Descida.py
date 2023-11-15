import sympy as sp

x,y = sp.symbols('x y')

z  = x**2 + 4*y**2 + 2*x*y


f_x = sp.diff(z,x)
f_y = sp.diff(z,y)

