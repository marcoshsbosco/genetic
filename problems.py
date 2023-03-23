import random


class Queens:
    def random_population(n):
        population = []

        for j in range(n):
            s = ""

            for i in range(8):
                s += str(random.randint(0, 7))

            population.append(s)

        return population


    def fitness(individual):
        score = 0  # pairs of non-attacking queens

        for i_atk, j_atk in enumerate(individual):
            for i, j_def in enumerate(individual[i_atk + 1:]):
                i_def = i + i_atk + 1

                j_atk = int(j_atk)
                j_def = int(j_def)

                if j_atk == j_def:  # attacking and defending queens on same row
                    pass
                elif i_atk - j_atk == i_def - j_def:  # same diagonal up-right
                    pass
                elif i_atk + j_atk == i_def + j_def:  # same diagonal down-right
                    pass
                else:  # attacking and defending queen don't conflict
                    score += 1

        return score


    def reproduce(x, y):
        return x[:4] + y[4:]


    def mutate(individual):
        col = random.randint(0, 7)  # chooses column to mutate row position

        individual = individual[:col] + str(random.randint(0, 7)) + individual[col + 1:]

        return individual


demand_points = []
for i in range(10):
            demand_points.append((random.random()*100, random.random()*100))

class SmallestCircle:
    def random_population(n):
        population = []

        for j in range(n):
            population.append((random.random()*100, random.random()*100))

        return population


    def fitness(individual):  # distance is the cost
        distances = []

        for point in demand_points:
            distances.append(((individual[0] - point[0]) ** 2 + (individual[1] - point[1]) ** 2) ** 0.5)

        return 1 / max(distances)  # return score (inverse because we need to minimize)


    def reproduce(x, y):  # places child between x and y points
        return ((x[0] + y[0]) / 2, (x[1] + y[1]) / 2)


    def mutate(individual):  # adds 10 to coordinates
        return (individual[0] + 10 if random.random() < 0.5 else individual[0] - 10, individual[1] + 10 if random.random() < 0.5 else individual[1] - 10)
