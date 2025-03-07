import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return np.tanh(x)

def d_tanh(x):
    return 1 - np.tanh(x)**2

def plot_tanh():
    x = np.linspace(-5, 5, 400)
    y = tanh(x)
    dy = d_tanh(x)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label='Tanh')
    plt.plot(x, dy, label='Derivada de Tanh', linestyle='dashed')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='dotted')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='dotted')
    plt.title('Tanh y su Derivada')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
