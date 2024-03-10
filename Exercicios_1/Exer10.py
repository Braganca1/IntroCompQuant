import matplotlib.pyplot as plt
import cmath

def pol(z):
    return (f"{abs(z)} cis {cmath.phase(z)}")

z=2+2j

print(pol(z))