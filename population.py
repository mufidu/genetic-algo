import random, math

# Inisialisasi populasi / generasi pertama
def generate_population(size, x_boundaries, y_boundaries):
    lower_x_boundary, upper_x_boundary = x_boundaries
    lower_y_boundary, upper_y_boundary = y_boundaries

    population = []
    # Populasi akan berisi list yang berisi dictionary yang berisi nilai x, y, fitness, dan hasil function
    for _ in range(size):
        x = random.uniform(lower_x_boundary, upper_x_boundary)
        y = random.uniform(lower_y_boundary, upper_y_boundary)
        individual = {
            "x": x,
            "y": y,
            "fitness": 1/((math.pow((math.cos(x)+math.sin(y)),2)/(x**2+y**2))+0.01),
            "h":(math.cos(x)+math.sin(y))**2/(x**2+y**2)
        }
        population.append(individual)

    return population

# Mengurutkan populasi berdasarkan fitness dari yang terkecil ke terbesar
def sort_population_by_fitness(population):
    return sorted(population, key=lambda individual: individual["fitness"])