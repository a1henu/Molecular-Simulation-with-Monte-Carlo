# Monte Carlo Simulation for Argon System with Lennard-Jones Potential
This is the final project for the course "Fundamentals and Applications of Molecular Simulations"(00333736) at College of Engineering, Peking University. It contains an implementation of Monte Carlo simulation for Argon system with Lennard-Jones potential, using Python and Numpy.

## Requirements
- Python 3.7 or later.
- NumPy.

## Project Structure
- `main.py`: The main script that runs the simulation.
- `module/system.py`: Contains the `BaseSystem` class which defines the base problem.
- `module/argon.py`: Contains the Derived class `ArgonSystem` which defines the Argon system.
- `module/mc.py`: Contains the `MonteCarlo` class which performs the Monte Carlo simulation.
- `module/utils.py`: Contains utility functions for the simulation.

## Generic Monte Carlo Algorithm
This project presents a generic Monte Carlo algorithm for simulating any system. It is organized into three main classes:
- **BaseSystem**: An abstract base class that defines the basic interfaces required for Monte Carlo simulations.
- **ArgonSystem**: Inherits from `BaseSystem` and implements specific methods for energy calculation and particle movement. This class mainly handles the Lennard-Jones potential and periodic boundary conditions.
- **MonteCarlo**: Implements the general logic for Monte Carlo simulations, including trial moves, energy calculations, and the Metropolis criterion.

The `MonteCarlo` class has an attribute `system` which is an instance of a class that inherits from `BaseSystem` which defines the system to be simulated. Using this structure, we can easily extend the simulation to other systems by creating a new class that inherits from `BaseSystem` and implements the required methods.

To implement a new system, you need to create a new class that inherits from `BaseSystem` and implement the following methods:
- `calc_energy(self) -> float`: Calculate the total energy of the system.
- `trial_move(self) -> Tuple[float, float]`: Perform a trial move and determine the change in energy.
- `accept_move(self) -> None`: Accept the trial move and do the necessary updates.
- `reject_move(self) -> None`: Reject the trial move and revert the changes.

Then, you can use the `MonteCarlo` class to run the simulation for the new system.

**Note**: The current implementation is for a simple Argon system. My `MonteCarlo` class will calculate the pressure of the system, but other systems may not have this feature. In that case, you can modify the `MonteCarlo` class to remove the pressure calculation.

## Usage
To run the simulation, you can use the command line interface provided. The script accepts the following arguments:
- `-N` or `--num_particles`: The number of particles in the system.
    - Default: 50
- `-L` or `--box_length`: The length of the square box.
    - Default: 1.0
- `-e` or `--epsilon`: The argument \epsilon in the Lennard-Jones potential.
    - Default: 1.0
- `-s` or `--sigma`: The argument \sigma in the Lennard-Jones potential.
    - Default: 0.1
- `-b` or `--beta`: The inverse temperature. (\beta = \frac{1}{kT}, where k is the Boltzmann constant and T is the temperature.)
    - Default: 0.01
- `-n` or `--num_steps`: The number of Monte Carlo steps to run.
    - Default: 2000

If you choose the `-o` or `--output` option, the results will be saved to the specified file. Then, you can use the command line to view the results.

```bash
python3 visualize.py --data {output_file}
```

## Example
```bash
python3 main.py -N 50 -L 1.0 -e 1.0 -s 0.1 -b 0.01 -n 2000
```
This command will run the simulation and print the results to the console.

```bash
python3 main.py --output output.txt -N 50 -L 1.0 -e 1.0 -s 0.1 -b 0.01 -n 2000
```
This command will run the simulation and save the results to `output.txt`.

```bash
python3 visualize.py --data output.txt
```
This command will visualize the results saved in `output.txt`.

## Output
The output of the simulation includes the following information:
- The initial conditions of the particles.
- The energy and pressure of the system at each step.
- The average energy and pressure of the system.
