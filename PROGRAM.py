from itertools import permutations

INF = float('inf')


def tsp_brute_force(cost, n):
    """Find the optimal TSP tour using brute force."""
    cities = list(range(1, n))
    best_cost = INF
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]

        total_cost = 0
        for i in range(n):
            total_cost += cost[path[i]][path[i + 1]]

        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path

    return best_path, best_cost


# 5-City Cost Matrix
cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

cities = ['A', 'B', 'C', 'D', 'E']
n = len(cost)

# Find optimal tour
best_path, best_cost = tsp_brute_force(cost, n)

# Print Cost Matrix
print("5-City TSP - Cost Matrix:\n")

print(f'{"":>4}', end="")
for city in cities:
    print(f'{city:>6}', end="")
print()

for i in range(n):
    print(f'{cities[i]:>4}', end="")
    for value in cost[i]:
        if value == INF:
            print(f'{"INF":>6}', end="")
        else:
            print(f'{value:>6}', end="")
    print()

# Print Optimal Tour
print("\nOptimal Tour:", " -> ".join(cities[i] for i in best_path))
print("Minimum Cost:", best_cost)

# Path Verification
print("\nPath verification:\n")

total = 0
for i in range(len(best_path) - 1):
    u = best_path[i]
    v = best_path[i + 1]
    w = cost[u][v]
    total += w
    print(f"  {cities[u]} -> {cities[v]}: cost = {w}")

print(f"\nVerified Total Cost = {total}")
