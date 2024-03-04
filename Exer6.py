str1 = input("Digite o primeiro complexo no formato a+bj: ")
str2 = input("Digite o segundo complexo no formato a+bj: ")

c1 = complex(str1)
c2 = complex(str2)

print("teste a:")
print("|c1|*|c2| = |c1*c2|", (abs(c1)*abs(c2) == abs(c1*c2)))

print("teste b:")
print("|c1+c2| <= |c1|+|c2|", (abs(c1+c2) <= abs(c1)+abs(c2)))