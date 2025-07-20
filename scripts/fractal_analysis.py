import numpy as np
from scipy.stats import linregress

def dimensao_fractal(zeros, escalas=[10, 20, 50, 100]):
    """Calcula dimensão fractal via box-counting"""
    counts = []
    for scale in escalas:
        hist, _ = np.histogram(zeros, bins=scale)
        counts.append(np.sum(hist > 0))
    slope, _, _, _, _ = linregress(np.log(escalas), np.log(counts))
    return slope

if __name__ == "__main__":
    zeros = np.loadtxt('data/zeros_zeta.csv', delimiter=',')[:, 1]  # Pega Im(s)
    D = dimensao_fractal(zeros)
    print(f"Dimensão fractal estimada: D = {D:.3f} (deve ser ≈1.0)")