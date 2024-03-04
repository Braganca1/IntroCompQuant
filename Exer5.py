def soma (a,b,c,d):
    return f"({a+c})+({b+d})i"

def produto (a,b,c,d):
    return f"({a*c-b*d})+({b*c+a*d})i"

x1 = int(input("Parte real do primeiro complexo: " ))
x2 = int(input("Parte imaginária do primeiro complexo: " ))
y1 = int(input("Parte real do segundo complexo: " ))
y2 = int(input("Parte imaginária do segundo complexo: " ))
z1 = int(input("Parte real do terceiro complexo: " ))
z2 = int(input("Parte imaginária do terceiro complexo: " ))


print(f"c1 + c2 = {soma(x1,x2,y1,y2)} ; c2 + c1 = {soma(y1,y2,x1,x2)}")
print(f"c1 x c2 = {produto(x1,x2,y1,y2)} ; c2 x c1 = {produto(y1,y2,x1,x2)}\n")

print(f"(c1 + c2) + c3 = {soma(int (soma(x1,x2,y1,y2)[1]),int (soma(x1,x2,y1,y2)[5]),z1,z2)} ; c1 + (c2 + c3)  = { soma(x1,x2,int (soma(y1,y2,z1,z2)[1]),int (soma(y1,y2,z1,z2)[5]))}")
print(f"(c1 x c2) x c3 = {produto(x1,x2,y1,y2)} ; c1 x (c2 x c3) = {produto(y1,y2,x1,x2)}\n")

print (f"c1 x (c2 + c3) = {produto(x1,x2,int(soma(y1,y2,z1,z2)[1]),int(soma(y1,y2,z1,z2)[5]))} ; (c1 x c2) + (c1 x c3) = {soma(int(produto(x1,x2,y1,y2)[1]),int(produto(x1,x2,y1,y2)[5]),int(produto(x1,x2,z1,z2)[1]),int(produto(x1,x2,z1,z2)[5]))}")
