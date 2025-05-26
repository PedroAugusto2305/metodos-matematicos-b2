import numpy as np
import matplotlib.pyplot as plt

def diferencas_divididas(x, y):
    n = len(x)
    coef = y.copy()
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

def polinomio_newton(x, coef, valor):
    n = len(coef)
    resultado = coef[-1]
    for i in range(n - 2, -1, -1):
        resultado = resultado * (valor - x[i] + coef[i])
    return resultado

x = [600, 800, 1000, 1300, 1400]
y = [1.43, 2.55, 2.71, 2.61, 2.51]

coef = diferencas_divididas(x, y)

x_plot = np.linspace(min(x) - 1, max(x) + 1, 400)
y_plot = [polinomio_newton(x, coef, xi) for xi in x_plot]

plt.figure(figsize=(8,5))
plt.plot(x_plot, y_plot, label='Polinômio de Newton', linewidth=2)
plt.scatter(x, y, color='red', zorder=5, label='Pontos dados')
plt.title('Interpolação Polinomial de Newton')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("grafico_newton.png")  # Salva a imagem no mesmo diretório
print("Gráfico salvo como 'grafico_newton.png'")