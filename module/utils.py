import numpy as np

def dist(x: np.array, y: np.array, L: float) -> float:
    dx = abs(x[0] - y[0])
    dy = abs(x[1] - y[1])
    if dx > L / 2:
        dx -= L
    if dy > L / 2:
        dy -= L
    return np.sqrt(dx ** 2 + dy ** 2)

def LJ_potential(r: float, epsilon: float, sigma: float) -> float:
    val6 = (sigma / r) ** 6
    return 4 * epsilon * (val6 * val6 - val6)

def distribute_points(L: float, N: int) -> np.ndarray:
    size = int(np.floor(np.sqrt(N)))
    if size ** 2 < N:
        size += 1
    
    # Calculate number of points per grid
    num_points_per_grid = N // (size * size)  
    extra_points = N % (size * size)  
      
    x_coords = []  
    y_coords = []  
      
    for i in range(size):  
        for j in range(size):  
            num_points_this_grid = num_points_per_grid  
            if extra_points > 0:  
                num_points_this_grid += 1  
                extra_points -= 1  
              
            step_x = L / size  
            step_y = L / size  
            for _ in range(num_points_this_grid):  
                x = (i + 0.5) * step_x  
                y = (j + 0.5) * step_y  
                x_coords.append(x)  
                y_coords.append(y)  
      
    points = np.array([x_coords, y_coords]).T
    return points 

def prob(dE: float, beta: float) -> float:
    if dE < 0:
        return 1
    return np.exp(-beta * dE)

def accept(dE: float, beta: float) -> float:
    return np.random.rand() < prob(dE, beta)