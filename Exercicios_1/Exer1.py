from sympy import symbols, Eq, solve

x = symbols('x')

e = Eq(x**4 + 2*x**2 +1 , 0)

print(solve(e, x))

#As raízes são i e -i e são raízes duplas