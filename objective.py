from doan import *
from hoandoi import *
import random
t =1200
S_feasible = []
S_now = initial_solution
tabu_list = []
S_best = S_now
N = len(S_now)
iteration_limit = 4000 + 40 * N
iteration_without_change_limit = 2000 + 10 * N
list_j1j2 =[]
def chonj1_j2(solution):
    non_zero_positions = [i for i, val in enumerate(solution) if val != 0]
    # Nếu không còn vị trí không phải là 0 hoặc chỉ còn một vị trí thì không thể lựa chọn j1 và j2
    if len(non_zero_positions) < 2:
        print("Không thể lựa chọn j1 và j2.")
    else:
        # Chọn ngẫu nhiên vị trí của j1 và j2
        vtj1, vtj2 = random.sample(non_zero_positions, 2)
        # Đảm bảo j1 nằm trước j2
        vtj1, vtj2 = min(vtj1, vtj2), max(vtj1, vtj2)
        j1 = solution[vtj1]
        j2 = solution[vtj2]
        while (j1, j2) in tabu_list:
            vtj1, vtj2 = random.sample(non_zero_positions, 2)
            vtj1, vtj2 = min(vtj1, vtj2), max(vtj1, vtj2)
            j1 = solution[vtj1]
            j2 = solution[vtj2]
        list_j1j2 = [j1,j2]
    return list_j1j2
def hoandoi(solution,j1,j2):
    S_feasible_1 = Vertex_exchange(solution, j1, j2)
    S_feasible_2=Vertex_forward_insertion(solution, j1, j2)
    S_feasible_3=Vertex_backward_insertion(solution, j1, j2)
    S_feasible_4=Vertex_inversion(solution, j1, j2)
    S = [S_feasible_1,S_feasible_2,S_feasible_3,S_feasible_4]
    return S
def evaluate_solution(solution):
    total_load1 = 0
    total_time1 = 0
    current_load1 = 0
    current_time1 = 0
    f = 1
    h = 0
    z = 0
    number_vehicle = solution.count(0)
    for i in range(1, len(solution)):
        customer = solution[i]
        demand_customer = demand[customer]
        time_window_constraint_customer = time_window_constraint[customer]
        total_load1 = current_load1 + demand_customer[0]
        travel_time_to_customer = travel_time[solution[i-1]][customer]
        total_time1 = current_time1 + travel_time_to_customer + demand_customer[1]
        if customer != 0:
            current_load1 = total_load1
            current_time1 = total_time1
            #if time_window_constraint_customer[0] - total_time1 > 0:
            #    z = z + time_window_constraint_customer[0] - total_time1
            #    f = 0
            if total_time1 - time_window_constraint_customer[1]  > 0:
                z = z + 5*(time_window_constraint_customer[1] - total_time1)
                f = 0
            if i == len(solution)-1:
                if current_load1 > capacity_constraint[0]:
                    h = h +1
                    f = 0
        else:
            if current_load1 > capacity_constraint[0]:
                h = h +1
                f = 0
        # Gặp số 0, cập nhật lại trạng thái
            current_load1 = 0
            current_time1 = 0
            total_load1 = 0
            total_time1 = 0
    G = 1000000*number_vehicle + 10*(z+h*t)
    # list G f của 1 solution
    list_gf = [G,f,h,solution]
    return list_gf
iteration = 0
while iteration < iteration_limit:
    list12 = chonj1_j2(S_now)
    j1 = list12[0]
    j2 = list12[1]
    S = hoandoi(S_now,j1,j2)
    best = evaluate_solution(S_best)
    # Tạo ra các giải pháp khả thi
    for i in S:
        S_feasible += evaluate_solution(i)
# Kết quả có hàm mục tiêu của S best
    check = [1, 5, 9, 13]
    positions = [pos for pos in check if S_feasible[pos] == 1]
    if not positions:
        position = [pos for pos in check if S_feasible[pos] == 0]
        mins = [S_feasible[pos - 1] for pos in position if pos >= 1]
        if mins:
            if len(mins) > 1:
                min = min(mins)
            else:
                min = mins[0]
        min_position = positions[mins.index(min)]
        S_now = S_feasible[min_position+2]
    else:
    # cái này là tìm 1 list giá trị hàm mục tiêu khi tại vị trí đó có f=1 nghĩa là giải pháp không vi phạm ràng buộc
        min_values = [S_feasible[pos - 1] for pos in positions if pos >= 1 and S_feasible[pos - 1] != 0]
        if min_values:
            if len(min_values) > 1:
                min_value = min(min_values)
            else:
                min_value = min_values[0]
            #print(min_value)
            min_position = positions[min_values.index(min_value)]
            #print(S_feasible[min_position])
            now = min_position + 2
            #print(S_feasible[now])
            if min_value <= best[0]:
                S_best = S_feasible[now]
                S_now = S_best
                if len(tabu_list) > 10:
                    tabu_list.pop(0)
                tabu_list+= (j1,j2)
            else: S_now = S_feasible[now]
    iteration += 1
print(S_best)

    # # Tìm solution hàng xóm tốt nhất
    # for neighbor in neighbors:
    #     neighbor_value = evaluate_solution(neighbor)[0]
    #     if neighbor_value < best_neighbor_value and neighbor not in tabu_list:
    #         best_neighbor = neighbor
    #         best_neighbor_value = neighbor_value
    # if best_neighbor is not None:
    #     S_now = best_neighbor
    #     S_now_value = best_neighbor_value
    #     tabu_list.append(S_now)
    #     if len(tabu_list) > 10:
    #         tabu_list.pop(0)

    # if S_now_value < best_value:
    #     S_best = S_now
    #     best_value = S_now_value
    #     iteration_without_change = 0
    # else:
    #     iteration_without_change += 1

    # iteration += 1
