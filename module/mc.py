from .utils import accept, prob
from .system import BaseSystem
from typing import Union
import matplotlib.pyplot as plt

class MonteCarlo:
    def __init__(self, 
                 system: BaseSystem, 
                 num_steps: int
                ) -> None:
        self.system = system
        self.num_steps = num_steps
        
        self.N_success = 0
        self.E_sum = 0
        self.P_sum = 0

    def run(self, output: Union[str, None] = None) -> None:
        if output is not None:
            output_file = open('./output/' + output, 'w')
            output_file.write(f'E, P\n')
        else:
            # plt.ion()
            fig, ax = plt.subplots()
            scat = ax.scatter(self.system.positions[:, 0], self.system.positions[:, 1])
            ax.set_xlim(0, self.system.L)
            ax.set_ylim(0, self.system.L)
            
        for step in range(self.num_steps):
            E_old, E_new = self.system.trial_move()
            
            # print(f'prob = {prob(E_new - E_old, self.system.beta)}')
            
            if accept(E_new - E_old, self.system.beta):
                self.system.accept_move()
                self.N_success += 1
            else:
                self.system.reject_move()
                
            E, P = self.system.calc_energy(), self.system.calc_pressure()
            self.E_sum += E
            self.P_sum += P
            
            if output is not None:
                output_file.write(f'{E}, {P}\n')
            else:
                print(f'step {step + 1:^7}: E = {E:.8f}\tP = {P:.8f}')
                
                scat.set_offsets(self.system.positions)
                plt.draw()
                plt.pause(0.01)
                
    def average_energy(self) -> float:
        return self.E_sum / self.num_steps
    
    def average_pressure(self) -> float:
        return self.P_sum / self.num_steps
    
    def acceptance_ratio(self) -> float:
        return self.N_success / self.num_steps
