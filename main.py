import numpy as np
import matplotlib.pyplot as plt

from src.relu import plot_relu
from src.sigmoid import plot_sigmoid
from src.tanh import plot_tanh
from src.leaky_relu import plot_leaky_relu

def main():
    
    plot_relu()
    plot_sigmoid()
    plot_tanh()
    plot_leaky_relu()

if __name__ == "__main__":
   main()
