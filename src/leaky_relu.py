import numpy as np
import matplotlib.pyplot as plt

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def d_leaky_relu(x, alpha=0.01):
    return np.where(x > 0, 1, alpha)

def plot_leaky_relu():
    x = np.linspace(-5, 5, 400)
    y = leaky_relu(x)
    dy = d_leaky_relu(x)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label='Leaky ReLU')
    plt.plot(x, dy, label='Derivada de Leaky ReLU', linestyle='dashed')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='dotted')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='dotted')
    plt.title('Leaky ReLU y su Derivada')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
