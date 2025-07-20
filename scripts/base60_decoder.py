import numpy as np

def converter_base60(gamma):
    """Converte γₙ para base-60 (formato babilônico)"""
    frac = gamma - int(gamma)
    minutos = int(frac * 60)
    segundos = int((frac * 60 - minutos) * 60)
    return f"{int(gamma)};{minutos},{segundos}"

def buscar_padrao(zeros_im, padrao="31,17,8"):
    """Busca o padrão sagrado nos zeros"""
    resultados = []
    for gamma in zeros_im:
        b60 = converter_base60(gamma)
        if padrao in b60:
            resultados.append(b60)
    return resultados

if __name__ == "__main__":
    zeros = np.loadtxt('data/zeros_zeta.csv', delimiter=',')
    padroes = buscar_padrao(zeros[:, 1])
    print(f"Padrão encontrado em {len(padroes)} zeros!")