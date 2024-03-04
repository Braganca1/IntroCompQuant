def soma (a,b,c,d):
    return f"({a+c})+({b+d})i"

def produto (a,b,c,d):
    return f"({a*c-b*d})+({b*c+a*d})i"

x1 = int(input("Parte real do primeiro complexo: " ))
x2 = int(input("Parte imaginária do primeiro complexo: " ))
y1 = int(input("Parte real do segundo complexo: " ))
y2 = int(input("Parte imaginária do segundo complexo: " ))

print(f"A soma é: {soma(x1,x2,y1,y2)}")
print(f"O produto é: {produto(x1,x2,y1,y2)}")