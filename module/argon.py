from .system import BaseSystem
from .utils import LJ_potential, distribute_points, dist, accept
from typing import Tuple
import numpy as np

class ArgonSystem(BaseSystem):
    def __init__(self, 
                 N: int, 
                 L: float, 
                 beta: float, 
                 epsilon: float, 
                 sigma:float
                ) -> None:
        self.N = N
        self.L = L
        self.V = L ** 2
        
        self.beta = beta
        self.epsilon = epsilon
        self.sigma = sigma
        self.max_displacement = 0.02 * L
        self.positions = distribute_points(L, N)
        
        self.E_cur = self.calc_energy()
        self.changed_index = []
        self.changed_position = []
        
    def calc_energy(self) -> float:
        energy = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                r = dist(self.positions[i], self.positions[j], self.L)
                energy += LJ_potential(r, self.epsilon, self.sigma)
        return energy
    
    def displacement(self, *indices: int) -> None:
        for index in indices:
            self.changed_index.append(index)
            self.changed_position.append(self.positions[index].copy())
            
            dx = np.random.uniform(-self.max_displacement, self.max_displacement)
            dy = np.random.uniform(-self.max_displacement, self.max_displacement)
            
            self.positions[index] = (self.positions[index] + np.array([dx, dy])) % self.L
        
    def trial_move(self) -> Tuple[float, float]:
        k = 5 # number of particles to displace
        indices = np.random.randint(0, self.N, k)
        self.displacement(indices)
        
        E_o = self.E_cur
        E_n = self.calc_energy()
        
        return E_o, E_n
    
    def __clear(self) -> None:
        self.changed_index = []
        self.changed_position = []
        
    def accept_move(self) -> None:
        self.__clear()
        self.E_cur = self.calc_energy()
        
    def reject_move(self) -> None:
        for index, position in zip(self.changed_index, self.changed_position):
            self.positions[index] = position
        self.__clear()
        
    def calc_pressure(self) -> float:
        '''
        P = rho kT + P^{\star} / V
        where rho = N / V
              P^{\star} = (1/6) \sum_{i} \sum_{j \neq i} \vec{r}_{ij} \cdot \vec{f}_{ij}
        '''
        rho = self.N / self.V
        P_star = 0
        for i in range(self.N):
            for j in range(self.N):
                if j != i:
                    r = self.positions[i] - self.positions[j]
                    f = 48 * self.epsilon / self.sigma * ((self.sigma / np.linalg.norm(r)) ** 13 - 0.5 * (self.sigma / np.linalg.norm(r)) ** 7) * r / np.linalg.norm(r)
                    P_star += np.dot(r, f)
        P_star /= 6
        return rho / self.beta + P_star / self.V
        