import matplotlib.pyplot as plt
import cmath


def plotsomaimag (z):
    plt.figure()
    plt.grid()
    for n in range(1,11):
        plt.plot([0,(z+1j*n).real], [0,(z+n*1j).imag], label=f'z**{n}')
    for n in range (1,11):
        plt.scatter([(z+n*1j).real], [(z+n*1j).imag])
    plt.legend()
    plt.show()

z=complex(input("Insira z: "))

plotsomaimag(z)