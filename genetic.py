import random
import matplotlib.pyplot as plt
import time
from problems import SmallestCircle
from problems import demand_points


def search(problem, fitness, population, generations):
    plot_data = {"gen": [], "fitness": []}

    fig, ax = plt.subplots()

    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness")

    #plt.yscale('log')

    for gen in range(generations):
        plot_data["gen"].append(gen)
        plot_data["fitness"].append(max([fitness(individual) for individual in population]))

        new_population = []

        for i in range(len(population)):
            x, y = selection(population.copy(), fitness)

            child = problem.reproduce(x, y)

            if random.random() < 0.1:
                child = problem.mutate(child)

            new_population.append(child)

        population += new_population
        population = sorted(population, key=fitness, reverse=True)
        population = population[:len(population) // 2]

    ax.plot(plot_data["gen"], plot_data["fitness"], label=str(problem))

    ax.legend()

    t = time.time()
    fig.savefig(f'{t}.png')

    fitnesses = []

    for individual in population:
        fitnesses.append(fitness(individual))

    if str(problem) == "<class 'problems.SmallestCircle'>":
        fig1, ax1 = plt.subplots()

        ax1.plot([point[0] for point in demand_points], [point[1] for point in demand_points], 'ro', label="Demand points")
        ax1.plot(population[fitnesses.index(max(fitnesses))][0], population[fitnesses.index(max(fitnesses))][1], 'bo', label="Best individual")

        ax1.legend()

        fig1.savefig(f'{t}g.png')

    return population[fitnesses.index(max(fitnesses))]


def selection(population, fitness):
    x = random.choice(population)
    y = random.choice(population)

    return x, y

