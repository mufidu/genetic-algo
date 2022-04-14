import random

def choice_by_roulette(sorted_population, fitness_sum):
    # Memilih individu menggunakan metode roulette
    pick = random.uniform(0, fitness_sum)
    current = 0
    for individual in sorted_population:
        current += individual["fitness"]
        if current > pick:
            return individual