c1=complex(input("Digite o primeiro complexo: "))
c2=complex(input("Digite o segundo complexo: "))


print(f"conj(c1) + conj(c2) = {c1.conjugate()+c2.conjugate()} ; conj(c1+c2) = {(c1+c2).conjugate()}")
print(f"conj(c1) * conj(c2) = {c1.conjugate()*c2.conjugate()} ; conj(c1*c2) = {(c1*c2).conjugate()}")
