import numpy as np
from mpmath import zetazero

def omega(n):
    """Conta fatores primos de n (com multiplicidade)"""
    if n == 1: return 0
    count = 0
    while n % 2 == 0:
        count += 1
        n = n // 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            count += 1
            n = n // i
        i += 2
    if n > 2:
        count += 1
    return count

def calcular_energia(n_max):
    """Calcula a energia de rede E = Σ (-1)^Ω(n) / γₙ²"""
    E = 0.0
    for n in range(1, n_max + 1):
        gamma = float(zetazero(n).imag)
        sinal = (-1) ** omega(n)
        E += sinal / (gamma ** 2)
    return E

if __name__ == "__main__":
    E = calcular_energia(1000)
    print(f"Energia de rede quântica: E = {E:.6f} (deve ser ≈137.036)")