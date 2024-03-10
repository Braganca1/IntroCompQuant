import matplotlib.pyplot as plt

def multipreal(z,z0):
    plt.figure()
    plt.plot([0,z.real],[0,z.imag],label = 'z')
    plt.plot([0,(z*(z0.real)).real],[0,(z*(z0.real)).imag],label = 'z*(z0.real)')
    plt.scatter([z.real,(z*(z0.real)).real],[z.imag,(z*(z0.real)).imag])
    plt.grid()
    plt.legend()
    plt.show()

def multipimag(z,z0):
    plt.figure()
    plt.plot([0,z.real],[0,z.imag],label = 'z')
    plt.plot([0,(z*(z0.imag)).real],[0,(z*(z0.imag)).imag],label = 'z*(z0.imag)')
    plt.scatter([z.real,(z*(z0.imag)).real],[z.imag,(z*(z0.imag)).imag])
    plt.grid()
    plt.legend()
    plt.show()

z=complex(input("Insira z: "))
z0=complex(input("Insira z0: "))

multipreal(z,z0)
multipimag(z,z0)