import matplotlib.pyplot as plt

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

plotsoma(2-1j,1+1j)
plotsoma(2-1j,-1-1j)