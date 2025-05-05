import numpy as np

n = 10
ants = 100
iters = 1000
alpha, beta, rho = 1, 2, 0.1

dist = np.random.randint(1, 100, size=(n, n))
dist = (dist + dist.T) // 2
np.fill_diagonal(dist, 0)
pheromone = np.ones((n, n))

best_tour, best_len = None, np.inf

for _ in range(iters):
    all_tours = []

    for _ in range(ants):
        tour = [np.random.randint(n)]
        visited = set(tour)

        for _ in range(n - 1):
            curr = tour[-1]
            probs = np.array([
                (pheromone[curr][j] ** alpha) * (1 / dist[curr][j] ** beta) if j not in visited else 0
                for j in range(n)
            ])
            probs /= probs.sum()
            next_city = np.random.choice(n, p=probs)
            tour.append(next_city)
            visited.add(next_city)

        length = sum(dist[tour[i]][tour[i+1]] for i in range(n - 1))
        all_tours.append((tour, length))

        if length < best_len:
            best_tour, best_len = tour, length

    pheromone *= (1 - rho)
    for tour, length in all_tours:
        for i in range(n - 1):
            a, b = tour[i], tour[i+1]
            pheromone[a][b] += 1 / length
            pheromone[b][a] += 1 / length

print("Best tour length:", best_len)
print("Best tour:", best_tour)
