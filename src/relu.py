import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

def d_relu(x):
    return np.where(x > 0, 1, 0)

def plot_relu():
    x = np.linspace(-5, 5, 400)
    y = relu(x)
    dy = d_relu(x)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label='ReLU')
    plt.plot(x, dy, label='Derivada de ReLU', linestyle='dashed')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='dotted')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='dotted')
    plt.title('ReLU y su Derivada')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
