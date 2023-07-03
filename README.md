# Ant Colony Optimization for Travelling Salesman Problem

This repository contains a Python implementation of the Ant Colony Optimization (ACO) algorithm for solving the Travelling Salesman Problem (TSP). The TSP is a classic optimization problem that seeks to find the shortest possible route for a salesperson who needs to visit a list of cities once and return to the origin city.

## Code Structure and Functions

The code is organized into several components: the `City` class, the `Tour` class, the `AntColonyOptimization` class, and the main execution code.

### City Class

The `City` class represents a city in the TSP. It has a name and coordinates (x, y).

- `__init__(self, name, x, y)`: Initializes the city object with a name and its coordinates.
- `distance(self, city)`: Computes and returns the Euclidean distance between the current city and another given city.
- `__repr__(self)`: Provides a string representation of the city object when printed.

### Tour Class

The `Tour` class represents a possible solution to the TSP. It consists of a sequence of cities representing a specific route.

- `__init__(self, cities)`: Initializes the tour object with a list of cities. The tour starts and ends at the same city.
- `total_distance(self)`: Calculates and returns the total distance of the tour.
- `__repr__(self)`: Provides a string representation of the tour object when printed.

### AntColonyOptimization Class

The `AntColonyOptimization` class implements the Ant Colony Optimization algorithm to solve the TSP.

- `__init__(self, cities, n_ants, n_iterations, decay=0.1)`: Initializes the ACO algorithm with the given parameters.
- `calculate_distances(self)`: Calculates the distances between each pair of cities and stores them in a 2D numpy array.
- `run(self)`: Executes the ACO algorithm for the specified number of iterations.
- `spread_pheromone(self, all_paths)`: Spreads pheromone along the shortest path found in each iteration.
- `gen_all_paths(self)`: Generates all paths for all ants in the current iteration.
- `gen_path(self, start)`: Generates a single path for one ant, starting from a given city.
- `pick_move(self, pheromone, dist, visited)`: Chooses the next city to move to based on pheromone levels and distances.
- `gen_path_dist(self, path)`: Calculates the total distance of a given path.

## Usage

To run the ACO solver for the TSP, execute the Python script:

```bash
python version3.py
```

In `version3.py`, the ACO algorithm is initialized with the following parameters:

- `cities`: A list of `City` objects representing the cities in the TSP.
- `n_ants`: The number of ants to use in the ACO algorithm.
- `n_iterations`: The number of iterations to run the ACO algorithm.
- `decay`: The pheromone decay factor.

The script will output the best tour found by the ACO algorithm and the total distance of that tour.

## Dependencies

The script requires the following Python libraries:

- `numpy`
- `random`

## What I Learned

- **Ant Colony Optimization**: I gained a deep understanding of the Ant Colony Optimization algorithm and how it can be applied to solve the Travelling Salesman Problem. We learned about the concept of pheromones, ant movement, and the convergence of the algorithm towards the optimal solution. This algorithm, inspired by the behavior of ants, demonstrates the power of swarm intelligence in solving complex optimization problems.

- **Swarm Intelligence**: Implementing the Ant Colony Optimization algorithm provided us with insights into the concept of swarm intelligence. I learned how individual agents (ants) in a collective system can interact locally and share information (pheromone trails) to collectively make decisions that lead to global optimization. This collective intelligence mimics the behavior of natural swarms and offers an effective approach for solving complex problems.

- **Python Programming**: This project allowed us to strengthen our Python programming skills. I improved our knowledge of classes, data structures, and algorithm implementation in Python. I gained experience in working with numpy arrays, random number generation, and leveraging Python's object-oriented programming capabilities.

- **Problem Solving and Optimization**: The project challenged me to think critically and develop creative solutions to the Travelling Salesman Problem. I gained experience in analyzing complex problems, designing algorithms, and evaluating their efficiency and effectiveness. The use of swarm intelligence, specifically the Ant Colony Optimization algorithm, provided me with a different perspective on optimization and problem-solving techniques.

- **Collaboration and Teamwork**: Working as a team on this project enhanced our collaboration and teamwork skills. We learned how to effectively communicate, distribute tasks, and integrate individual contributions into a cohesive solution. Collaborating with teammates allowed us to leverage different perspectives and collectively develop a stronger understanding of swarm intelligence and its application to optimization problems.
