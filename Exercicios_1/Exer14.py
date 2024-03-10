def moebius (x):
    return (a*x+b)/(c*x+d)

a=0
d=0
b=1
c=1

z=complex(input("digite z: "))
print(moebius(z))