import matplotlib.pyplot as plt
import cmath


def plotexp (z):
    plt.figure()
    plt.grid()
    for n in range(1,11):
        plt.plot([0,(z**n).real], [0,(z**n).imag], label=f'z**{n}')
    for n in range (1,11):
        plt.scatter([(z**n).real], [(z**n).imag])
    plt.legend()
    plt.show()

z=complex(input("Insira z: "))

plotexp(z)