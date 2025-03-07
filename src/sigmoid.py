import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def d_sigmoid(x):
    s = sigmoid(x)
    return s * (1 - s)

def plot_sigmoid():
    x = np.linspace(-5, 5, 400)
    y = sigmoid(x)
    dy = d_sigmoid(x)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label='Sigmoid')
    plt.plot(x, dy, label='Derivada de Sigmoid', linestyle='dashed')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='dotted')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='dotted')
    plt.title('Sigmoid y su Derivada')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
