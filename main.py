import population as p
import generation as g

# Total generasi yang akan dibuat
generations = 100

print("Mencari fungsi minimum dengan metode genetika\n")

for generation in range(generations):
    print(f"Generasi ke-{generation+1}:\n")
    
    if generation == 0:
        # Inisialisasi populasi / generasi pertama
        population = p.generate_population(size=10, x_boundaries=(-5, 5), y_boundaries=(-5, 5))     
    else:
        # Buat generasi baru
        population = g.make_next_generation(population)
    
    # Menampilkan populasi yang individunya sudah diurutkan berdasarkan fitness
    sorted_population = p.sort_population_by_fitness(population)
    for individual in sorted_population:
        print("\tX: {:f}, Y: {:f}, Fitness: {:.3f}, Hasil function: {:.10f}".format(individual["x"], individual["y"], individual["fitness"], individual["h"]))
    print("\n")

# Menampilkan individu dengan fitness terbaik di generasi terakhir
sorted_last_gen = p.sort_population_by_fitness(population)
best_individual = sorted_last_gen[-1]
print("\n Fungsi minimum yang ditemukan adalah dengan:")
print("\tX: {:f}, Y: {:f}, Fitness: {:.3f}, Hasil function: {:.10f}".format(best_individual["x"], best_individual["y"], best_individual["fitness"], best_individual["h"]))