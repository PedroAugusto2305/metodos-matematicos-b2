import numpy as np
import matplotlib.pyplot as plt


def interpolador_lagrange(x_vals, y_vals, x):
    num_pontos = len(x_vals)
    val = 0.0
    for i in range(num_pontos):
        termo_lagr = 1.0
        for j in range(num_pontos):
            if j != i:
                termo_lagr *= (x - x_vals[j] / (x_vals[i] - x_vals[j]))
        val += termo_lagr * y_vals[i]
    return val

def plotar_lagrange(x_vals, y_vals, titulo="Polinômio de Lagrange", salvar_imagem=True):
    x_intervalo = np.linspace(min(x_vals) - 1, max(x_vals) + 1, 400)
    y_interp = [interpolador_lagrange(x_vals, y_vals, x) for x in x_intervalo]

    plt.figure(figsize=(8, 5))
    plt.plot(x_intervalo, y_interp, label="Polinômio Interpolador", linewidth=2)
    plt.scatter(x_vals, y_vals, color='red', label="Pontos originais", zorder=5)
    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    if salvar_imagem:
        plt.savefig("grafico_lagrange.png")
        print("Gráfico salvo como 'grafico_lagrange.png'")
    else:
        plt.show()


x_dados = [600, 800, 1000, 1300]
y_dados = [1.43, 2.55, 2.71, 2.61]
x_avaliar = 1200

resultado = interpolador_lagrange(x_dados, y_dados, x_avaliar)
print(f"Valor estimado do polinômio em x = {x_avaliar} é {resultado:.6f}")

plotar_lagrange(x_dados, y_dados)