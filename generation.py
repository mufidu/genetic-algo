import random, parents, math
import population as p

def crossover(individual_a, individual_b):
    xa = individual_a["x"]
    ya = individual_a["y"]

    xb = individual_b["x"]
    yb = individual_b["y"]

    # Crossover menggunakan rata-rata dari dua nilai
    return {"x": (xa + xb) / 2, "y": (ya + yb) / 2}

def mutate(individual):
    # Mutasi menggunakan nilai random antara -0.05 sampai 0.05
    next_x = individual["x"] + random.uniform(-0.05, 0.05)
    next_y = individual["y"] + random.uniform(-0.05, 0.05)

    lower_boundary, upper_boundary = (-5, 5)

    # Untuk memastikan hasil mutasi tidak keluar dari range
    next_x = min(max(next_x, lower_boundary), upper_boundary)
    next_y = min(max(next_y, lower_boundary), upper_boundary)

    return {"x": next_x, "y": next_y}

def make_next_generation(previous_population):
    next_generation = []
    sorted_by_fitness_population = p.sort_population_by_fitness(previous_population)
    population_size = len(previous_population)
    fitness_sum = sum([individual["fitness"] for individual in sorted_by_fitness_population])

    for _ in range(population_size):
        first_parent = parents.choice_by_roulette(sorted_by_fitness_population, fitness_sum)
        second_parent = parents.choice_by_roulette(sorted_by_fitness_population, fitness_sum)

        individual = crossover(first_parent, second_parent)
        individual = mutate(individual)

        individual["fitness"] = 1/((math.pow((math.cos(individual["x"])+math.sin(individual["y"])),2)/(individual["x"]**2+individual["y"]**2))+0.01)
        individual["h"] = math.pow((math.cos(individual["x"])+math.sin(individual["y"])),2)/(individual["x"]**2+individual["y"]**2)
        next_generation.append(individual)  

    return next_generation
