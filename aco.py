
import simple_colors
import numpy as np
import random
import matplotlib.pyplot as plt

# Graph a line plot of the min. distance at each iteration
def plot_iterations_over_distance(x, y):
    plt.plot(x, y, color = "green")
    plt.title("\nBest Solution Distance Over Course of Search")
    plt.xlabel("Epoch(s)") # X axis
    plt.ylabel("Total distance (km) for TSP") # Y axis
    plt.show()

# Graph a scattered line plot of the best tour
def plot_optimal_path_through_cities(x, y):
    plt.title("\nOptimal Path Through Cities Found")
    plt.xlabel("X-Coordinate of City")
    plt.ylabel("Y-Coordinate of City")
    plt.plot(x, y, marker = "*", mec = "red", mfc = 'red', ms = 8, color = "green")
    plt.show()

# Class to represent cities with a name and x, y coordinates for positioning
class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    # Compute the distance between the current city and a given city
    def distance(self, city):
        return ((self.x - city.x)**2 + (self.y - city.y)**2)**0.5

    # Provides a string representation for the City object, which is its name
    def __repr__(self):
        return self.name

# Class for a tour made up of multiple cities
class Tour:
    def __init__(self, cities):
        # The tour starts and ends at the same city
        self.cities = cities + [cities[0]]

     # Compute the total distance of the tour
    def total_distance(self):
        return sum(self.cities[i].distance(self.cities[i + 1]) for i in range(len(self.cities) - 1))

    def __repr__(self):
        return ' -> '.join(city.name for city in self.cities)

# class to implement the aco
class AntColonyOptimization:
    def __init__(self, cities, n_ants, n_iterations, decay=0.99):
        self.cities = cities
        self.distances = self.calculate_distances()
        self.pheromone = np.ones(self.distances.shape) / len(cities)  # Initial pheromone concentration
        self.all_indxs = range(len(cities))  # Indexes of all the cities
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay  # Pheromone decay factor

    # Function calculates the distance between each pair of cities and stores it in a 2D numpy array
    def calculate_distances(self):
        n_cities = len(self.cities)
        distances = np.zeros((n_cities, n_cities))  # Initialize the 2D array with zeros
        for i in range(n_cities):
            for j in range(i+1, n_cities):
                distances[i, j] = self.cities[i].distance(self.cities[j])
                distances[j, i] = distances[i, j]  # distance must be symmetric
        return distances

    #Function runs the ACO algorithm for a given number of iterations
    def run(self):
        # Initial shortest path is infinitely long
        shortest_path = ("placeholder", np.inf)
        # Epoch counter
        epoch = 1
        x_arr_line_plot = []
        y_arr_line_plot = []
        # Iterate for a given number of times
        for i in range(self.n_iterations):
            # Generate all paths for the current iteration
            all_paths = self.gen_all_paths()
            # Spread pheromone along the paths
            self.spread_pheronome(all_paths)
            # Find the shortest path in the current iteration
            min_path = min(all_paths, key=lambda x: x[1])

            print(simple_colors.green("Epoch " + str(epoch)) + " | " + "Minimum Total Distance: " + str(shortest_path[1]))
            epoch += 1
            x_arr_line_plot.append(epoch)
            y_arr_line_plot.append(shortest_path[1])
            if min_path[1] < shortest_path[1]: # If shorter than current shortest do your thing and update and decay
                shortest_path = min_path
            self.pheromone *= self.decay

        # Graph the min. distance at each iteration
        plot_iterations_over_distance(x_arr_line_plot, y_arr_line_plot)

        return shortest_path

    # Function spreads the pheromone on the shortest path found in the current iteration
    def spread_pheronome(self, all_paths):
        min_path = min(all_paths, key=lambda x: x[1])  # Shortest path in the current iteration
        # For each move in the shortest path, increase the amount of pheromone
        for move in min_path[0]:
            self.pheromone[move] += 1.0 / self.distances[move]

    # Function generates all paths for all ants in the current iteration
    def gen_all_paths(self):
        all_paths = []  # List to store all paths
        for i in range(self.n_ants):
            path = self.gen_path(random.randint(0,24))
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    # Function generates a single path for one ant, starting from a given city
    def gen_path(self, start):
        path = []
        visited = set()  # Set to store visited cities
        visited.add(start)  # Add the start city to the visited set
        prev = start  # The previous city is the start city

        for i in range(len(self.distances) - 1):
            # Choose the next city to visit
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            # Add the move to the path
            path.append((prev, move))
            prev = move  # previous city becomes the city just visited
            visited.add(move)  # Add the visited city to the set
        #  path ends with a move to the start city
        path.append((prev, start))

        return path

    # Function chooses the next city to move to
    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)  # Copy of the pheromone list
        # Set the pheromone value to 0 for the cities that have already been visited
        pheromone[list(visited)] = 0
        dist[dist == 0] = 1e-10  # avoid division by zero
        # Probability of moving to each city
        row = pheromone / dist
        norm_row = row / row.sum()
        # Choosing city to move to based on the made up probability I created
        move = np.random.choice(self.all_indxs, 1, p=norm_row)[0]
        return move

    # This function calculates the total distance of a given path
    def gen_path_dist(self, path):
        return sum([self.distances[i, j] for i, j in path])

# List of city names
city_names = ["Wintefell", "King's Landing", "Braavos", "Pentos", "Riverrun", "Dorne", "Highgarden",
    "Lannisport", "The Vale", "The Eyrie", "Mareen", "Volantis", "Qarth", "Ashaai", "Pyke",
    "Oldtown", "Storm's End", "Gulltown", "White Harbor", "Qohor", "Lys", "Lorath",
    "Stormlands", "Essos", "Tyrosh"]

# Generate list of city objects with random coordinates
city_list = [City(name, random.uniform(-200.0, 200.0), random.uniform(-200.0, 200.0)) for name in city_names]

print("---------------------------------------------------------------------")
print(simple_colors.green("Parameters for Ant Colony Optimization", "bold"))
print("---------------------------------------------------------------------")

# Print the names of the cities in the best tour and its total distance
print(simple_colors.green("Number of cities in the tour:"), len(city_names))

# Prompt for number of iterations
#n_iterations = int(input("Enter the number of iterations (default = 500): "))
print("\n")

# Initialize instance of the AntColonyOptimization class
aco = AntColonyOptimization(city_list, n_ants=25, n_iterations=500)

# Run ACO algorithm and store the shortest path found
shortest_path = aco.run()

# Print best tour found out of all the paths and total distance
print(simple_colors.green("\nBest Tour:", "bold"))
i = 1
x_arr_for_scatter = []
y_arr_for_scatter = []
for move in shortest_path[0]:
    print(f"{i}. {simple_colors.green(city_list[move[0]].name)} | Coodinates = ({city_list[move[0]].x}, {city_list[move[0]].y})")
    i += 1
    x_arr_for_scatter.append(city_list[move[0]].x)
    y_arr_for_scatter.append(city_list[move[0]].y)
print(simple_colors.green("\nTotal distance:", "bold"), shortest_path[1])
plot_optimal_path_through_cities(x_arr_for_scatter, y_arr_for_scatter)