from argparse import ArgumentParser
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import numpy as np

def plot(data, header):
    x = data[:, 0]
    y = data[:, 1]
    n = np.arange(1, len(x) + 1)

    n_smooth = np.linspace(n.min(), n.max(), 300)
    x_smooth = make_interp_spline(n, x)(n_smooth)
    y_smooth = make_interp_spline(n, y)(n_smooth)

    fig, axs = plt.subplots(1, 2, figsize=(20, 6))

    axs[0].plot(n_smooth, x_smooth, label=f'{header[0]}')
    mean_x = np.mean(x)
    axs[0].axhline(mean_x, color='red', linestyle='--', label='Mean')
    axs[0].text(n_smooth[-1], mean_x, f'{mean_x:.2f}', color='red', va='center', ha='left', backgroundcolor='white')
    axs[0].set_ylabel(header[0])
    axs[0].set_title(f'{header[0]}')
    axs[0].legend()
    axs[0].grid(True)

    axs[1].plot(n_smooth, y_smooth, label=f'{header[1]}')
    mean_y = np.mean(y)
    axs[1].axhline(mean_y, color='red', linestyle='--', label='Mean')
    axs[1].text(n_smooth[-1], mean_y, f'{mean_y:.2f}', color='red', va='center', ha='left', backgroundcolor='white')
    axs[1].set_ylabel(header[1])
    axs[1].set_title(f'{header[1]}')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument('--data', type=str, required=True)

    args = argparser.parse_args()
    filename = args.data

    with open(filename, 'r') as file:
        header = file.readline().strip().split(',')
        data = np.array([list(map(float, line.split(','))) for line in file])
        
    plot(data, header)
