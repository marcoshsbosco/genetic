"""
Authors: Bosco - RA117873; Mafe - RA118597
"""


import genetic
from problems import Queens, SmallestCircle
import time


print("###### 8 Queens ######")
# ----- 8 queens config 1 -----
print("--- Configuration 1 ---")

for i in range(3):
    t0 = time.time()
    best_individual = genetic.search(
        problem=Queens,
        fitness=Queens.fitness,
        population=Queens.random_population(15),
        generations=500
        )
    t1 = time.time()

    print("*** RESULT ***")
    print(f"Best individual: {best_individual}")
    print(f"Fitness: {Queens.fitness(best_individual)}")
    print(f"Time taken: {t1 - t0} s\n")


# ----- 8 queens config 2 -----
print("--- Configuration 2 ---")

for i in range(3):
    t0 = time.time()
    best_individual = genetic.search(
        problem=Queens,
        fitness=Queens.fitness,
        population=Queens.random_population(30),
        generations=125
        )
    t1 = time.time()

    print("*** RESULT ***")
    print(f"Best individual: {best_individual}")
    print(f"Fitness: {Queens.fitness(best_individual)}")
    print(f"Time taken: {t1 - t0} s\n")

print("###### SmallestCircle ######")

# ----- SmallestCircle config 1 -----
print("--- Configuration 1 ---")

for i in range(3):
    t0 = time.time()
    best_individual = genetic.search(
        problem=SmallestCircle,
        fitness=SmallestCircle.fitness,
        population=SmallestCircle.random_population(80),
        generations=20
        )
    t1 = time.time()

    print("*** RESULT ***")
    print(f"Best individual: {best_individual}")
    print(f"Fitness: {SmallestCircle.fitness(best_individual)}")
    print(f"Time taken: {t1 - t0} s\n")


# ----- SmallestCircle config 2 -----
print("--- Configuration 2 ---")

for i in range(3):
    t0 = time.time()
    best_individual = genetic.search(
        problem=SmallestCircle,
        fitness=SmallestCircle.fitness,
        population=SmallestCircle.random_population(4),
        generations=400
        )
    t1 = time.time()

    print("*** RESULT ***")
    print(f"Best individual: {best_individual}")
    print(f"Fitness: {SmallestCircle.fitness(best_individual)}")
    print(f"Time taken: {t1 - t0} s\n")
