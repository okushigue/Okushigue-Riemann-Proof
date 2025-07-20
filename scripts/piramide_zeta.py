import numpy as np
import matplotlib.pyplot as plt
from mpmath import zetazero
from mpl_toolkits.mplot3d import Axes3D

def calcular_zeros(n_start, n_end):
    """Calcula zeros da Zeta e retorna Re(s), Im(s), |ζ(s)|"""
    zeros = []
    for n in range(n_start, n_end + 1):
        z = zetazero(n)
        s = complex(z)
        zeros.append([s.real, s.imag, abs(z)])
    return np.array(zeros)

def plot_piramide(zeros):
    """Plota a pirâmide 3D dos zeros"""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    x, y, z = zeros[:, 0], zeros[:, 1], zeros[:, 2]
    ax.scatter(x, y, z, c=z, cmap='viridis', s=10)
    
    ax.set_xlabel('Re(s)')
    ax.set_ylabel('Im(s)')
    ax.set_zlabel('|ζ(s)|')
    plt.title("Pirâmide dos Zeros da Função Zeta")
    plt.savefig('results/piramide_3d.png')
    plt.show()

if __name__ == "__main__":
    zeros = calcular_zeros(1, 1000)  # Altere o intervalo conforme necessário
    np.savetxt('data/zeros_zeta.csv', zeros, delimiter=',')
    plot_piramide(zeros)