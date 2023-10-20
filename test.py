# import random
# from objective import S_feasible,S_best,best
# neighbors = []  # Danh sách các solution hàng xóm
# check = [1, 5, 9, 13]
# positions = [pos for pos in check if S_feasible[pos] == 1]

# if not positions:
#     position = [pos for pos in check if S_feasible[pos] == 0]
#     mins = [S_feasible[pos - 1] for pos in position if pos >= 1]
#     if mins:
#         if len(mins) > 1:
#             min = min(mins)
#         else:
#             min = mins[0]
#     min_position = positions[mins.index(min)]
#     S_now = S_feasible[min_position+2]
# else:
#     # cái này là tìm 1 list giá trị hàm mục tiêu khi tại vị trí đó có f=1 nghĩa là giải pháp không vi phạm ràng buộc
#     min_values = [S_feasible[pos - 1] for pos in positions if pos >= 1 and S_feasible[pos - 1] != 0]
#     if min_values:
#         if len(min_values) > 1:
#             min_value = min(min_values)
#             #min_value = random.choice(min_value)
#         else:
#             min_value = min_values[0]
#         print(min_value)
#         min_position = positions[min_values.index(min_value)] # chỗ này còn test lại xem đúng không
#         print(S_feasible[min_position])
#         now = min_position + 2
#         print(S_feasible[now])
#         if min_value <= best[0]:
#             S_best = S_feasible[now]

# print(S_feasible)
solution = [1,2,5,3]
demand = {1: (5, 2), 6: (10, 5), 2: (20, 5), 3: (30, 5), 5: (40, 5)}
current_load1 = 0
time_window_constraint = {1: (5, 2), 1: (10, 5), 2: (20, 5), 3: (30, 5), 5: (40, 5)}
travel_time = {3: {1: 17, 2: 10, 3: 20,  5: 29},1: {0: 17, 2: 48, 3: 50, 5: 44},
2: {2: 10, 1: 48, 3: 11, 4: 48, 5:23},5: {2: 10, 1: 48, 3: 11, 5:23}}
current_time1 = 0
for i in range(1, len(solution)):
    customer = solution[i]
    demand_customer = demand[customer]
    time_window_constraint_customer = time_window_constraint[customer]
    total_load1 = current_load1 + demand_customer[0]
    travel_time_to_customer = travel_time[solution[i - 1]][customer]
    total_time1 = current_time1 + travel_time_to_customer + demand_customer[1]
    
    print(travel_time_to_customer)
