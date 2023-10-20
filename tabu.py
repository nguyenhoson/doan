import random

def tabu_search(initial_solution, tabu_list_size, max_iterations):
    current_solution = initial_solution
    best_solution = initial_solution
    tabu_list = []

    for _ in range(max_iterations):
        random_i, random_j, same_route = select_random_customers(current_solution)
        neighbor_solutions = generate_neighbors(current_solution, random_i, random_j, same_route)

        # Lưu trạng thái tốt nhất trong tất cả các lân cận
        best_neighbor = None
        best_neighbor_cost = float('inf')

        for neighbor_solution in neighbor_solutions:
            neighbor_cost = evaluate_solution(neighbor_solution)

            if neighbor_solution not in tabu_list and neighbor_cost < best_neighbor_cost:
                best_neighbor = neighbor_solution
                best_neighbor_cost = neighbor_cost

        if best_neighbor:
            current_solution = best_neighbor
            if best_neighbor_cost < evaluate_solution(best_solution):
                best_solution = best_neighbor

            tabu_list.append(best_neighbor)
            if len(tabu_list) > tabu_list_size:
                tabu_list.pop(0)  # Loại bỏ giải pháp cấm lâu nhất

    return best_solution

def select_random_customers(solution):
    while True:
        i, j = random.sample(range(1, len(solution)), 2)
        if solution[i] == solution[j]:
            same_route = True
        else:
            same_route = False
        if same_route or i < j:
            return i, j, same_route

def generate_neighbors(solution, i, j, same_route):
    neighbors = []

    # Vertex exchange (cả 2 trường hợp)
    neighbor = solution[:]
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    neighbors.append(neighbor)

    if not same_route:
        # Vertex forward insertion (chỉ khi khác chuyến)
        if i + 1 < j:
            neighbor = solution[:i] + [solution[j]] + solution[i:j] + solution[j + 1:]
            neighbors.append(neighbor)

        # Vertex backward insertion (chỉ khi khác chuyến)
        if i > 0 and i < j - 1:
            neighbor = solution[:i] + solution[i + 1:j + 1] + [solution[i]] + solution[j + 1:]
            neighbors.append(neighbor)

    # Vertex inversion (cả 2 trường hợp)
    neighbor = solution[:i] + list(reversed(solution[i:j + 1])) + solution[j + 1:]
    neighbors.append(neighbor)

    if not same_route:
        # Tails exchange (chỉ khi khác chuyến)
        if j < len(solution) - 1:
            neighbor = solution[:i] + solution[j:] + solution[i:j]
            neighbors.append(neighbor)

    return neighbors

def evaluate_solution(solution):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += travel_time[solution[i]][solution[i + 1]]

    return total_cost

# Tham số cho giải thuật Tabu Search
tabu_list_size = 10
max_iterations = 100

best_solution = tabu_search(initial_solution, tabu_list_size, max_iterations)
print("Best Solution:")
for route in best_solution:
    print(route)
