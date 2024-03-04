print ("i**2 = -1")
print ("i**3 = -1*i = -i")
print ("i**4 = -i*i = 1")
print ("i**5 = 1*i = i")

a=int(input("Digite a potência de i: "))

if (a%4==0):
    print(f"i**{a} = 1")

    
if (a%4==1):
    print(f"i**{a} = i")
    
if (a%4==2):
    print(f"i**{a} = -1")
    
if (a%4==3):
    print(f"i**{a} = -i")