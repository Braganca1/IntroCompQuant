from sympy import symbols, Eq, solve

x= symbols ('x')

print(solve(Eq(x**2+2*x+2,0),x))