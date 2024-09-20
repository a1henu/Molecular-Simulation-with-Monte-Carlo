from module.argon import ArgonSystem
from module.mc import MonteCarlo
from visualize import plot
from argparse import ArgumentParser

import time
import numpy as np
import matplotlib.pyplot as plt

arg_parser = ArgumentParser()
arg_parser.add_argument('-o', '--output', type=str, default=None)
arg_parser.add_argument('-N', '--num_particles', type=int, default=200)
arg_parser.add_argument('-L', '--box_length', type=float, default=1.0)
arg_parser.add_argument('-e', '--epsilon', type=float, default=1.0)
arg_parser.add_argument('-s', '--sigma', type=float, default=0.1)
arg_parser.add_argument('-b', '--beta', type=float, default=0.01)
arg_parser.add_argument('-n', '--num_steps', type=int, default=2000)

def main():
    args = arg_parser.parse_args()
    output = args.output
    
    N = args.num_particles
    L = args.box_length
    epsilon = args.epsilon
    sigma = args.sigma
    beta = args.beta # 1 / kT
    num_steps = args.num_steps

    system = ArgonSystem(N, L, beta, epsilon, sigma)
    mc = MonteCarlo(system, num_steps)
    
    print(f'\n********** Monte Carlo Simulation for Argon System with LJ Potential **********')
    print(f'Number of particles: {N}'
          f'\nBox length: {L}'
          f'\nBeta: {beta}'
          f'\nEpsilon: {epsilon}'
          f'\nSigma: {sigma}'
          f'\nNumber of steps: {num_steps}'
          f'\nInitial energy: {system.E_cur}')
    print(f'*******************************************************************************')
    
    time.sleep(1)
    print('Running simulation...')
    time.sleep(0.5)
    
    if output is not None:
        print(f'Output file: ./output/{output}')
    
    np.random.seed(time.time_ns() % (1 << 32 - 1))
    mc.run(output)
    print(f'*******************************************************************************')
    print(f'Average energy: {mc.average_energy()}')
    print(f'Average pressure: {mc.average_pressure()}')
    print(f'Acceptance ratio: {mc.acceptance_ratio()}')
    
    if output is not None:
        print(f'You can run the command below to visualize the simulation:')
        print(f'python visualize.py --data ./output/{output}\n')
    
    if output is None:
        plt.show(block=True)

if __name__ == "__main__":
    main()
