import matplotlib.pyplot as plt
import cmath

def polar (z):
    return abs(z)*cmath.exp(1j*cmath.phase(z))

def plotsoma (z1,z2):
    plt.figure()
    plt.grid()
    plt.plot([0, z1.real], [0, z1.imag], label='z1')
    plt.plot([0, z2.real], [0, z2.imag], label='z2')
    plt.plot([0, (z1+z2).real], [0, (z1+z2).imag], label='Soma', linestyle='--')
    plt.scatter([z1.real, z2.real,(z1+z2).real], [z1.imag, z2.imag, (z1+z2).imag])
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.legend()
    plt.show()

a=2-1j
b=1+1j
c=2-1j
d=-1-1j

plotsoma(polar(a),polar(b))
plotsoma(polar(c),polar(d))