from doan import *
import random
#1
def Vertex_exchange(solution, j1, j2):
    new_solution1 = solution.copy()
    for i in range(len(new_solution1)):
        if new_solution1[i] == j1:
            new_solution1[i] = j2
        elif new_solution1[i] == j2:
            new_solution1[i] = j1
    so_chuyen = 0
    for item in solution:
        if item == 0:
            so_chuyen += 1
    #print(so_chuyen)
    if so_chuyen < Kmin:
        new_solution1 = []
    return new_solution1
#2
def  Vertex_forward_insertion(solution, j1, j2):    
    new_solution2 = solution.copy()
    # Tìm vị trí của j1 và j2 trong danh sách đỉnh
    index_j1 = solution.index(j1)
    index_j2 = solution.index(j2)    
    # Loại bỏ j1 khỏi danh sách
    new_solution2.pop(index_j1)   
    # Nếu j1 đứng trước j2, chỉ cần chèn j1 vào trước j2
    if index_j1 < index_j2:
        new_solution2.insert(index_j2-1, j1)
    # Ngược lại, nếu j1 đứng sau j2, chèn j1 vào trước j2 - 1 (do j1 bị loại bỏ khỏi danh sách trước đó)
    else:
        new_solution2.insert(index_j2 , j1)
    so_chuyen = 0
    for item in solution:
        if item == 0:
            so_chuyen += 1
    #print(so_chuyen)
    if so_chuyen < Kmin:
        new_solution2 = []
    return new_solution2
#3
def  Vertex_backward_insertion(solution, j1, j2):    
    new_solution3 = solution.copy()
    # Tìm vị trí của j1 và j2 trong danh sách đỉnh
    index_j1 = solution.index(j1)
    index_j2 = solution.index(j2)    
    # Loại bỏ j1 khỏi danh sách
    new_solution3.pop(index_j1)   
    # Nếu j1 đứng trước j2, chỉ cần chèn j1 vào trước j2
    if index_j1 < index_j2:
        new_solution3.insert(index_j2, j1)
    # Ngược lại, nếu j1 đứng sau j2, chèn j1 vào trước j2 - 1 (do j1 bị loại bỏ khỏi danh sách trước đó)
    else:
        new_solution3.insert(index_j2 +1 , j1)
    so_chuyen = 0
    for item in solution:
        if item == 0:
            so_chuyen += 1
    #print(so_chuyen)
    if so_chuyen < Kmin:
        new_solution3 = []
    return new_solution3
#4 nèee
def Vertex_inversion(solution, j1, j2):
    def find_nearest_zero_right(arr, start_index):
        for i in range(start_index, len(arr)):
            if arr[i] == 0:
                return arr[start_index:i]
        return []

    def find_nearest_zero_left(arr, start_index):
        for i in range(start_index, -1, -1):
            if arr[i] == 0:
                return arr[i:start_index+1]
        return []

    # Tạo bản sao của solution thành new_solution
    new_solution = solution.copy()

    # Tìm vị trí của j1 và j2 trong new_solution
    index_j1 = new_solution.index(j1)
    index_j2 = new_solution.index(j2)
    # Tìm tập giá trị a1 từ j1 đến số 0 tiếp theo, không bao gồm số 0
    a1 = find_nearest_zero_right(new_solution, index_j1)
    if a1 and j2 not in a1:
    # Tạo a11 bằng cách nghịch đảo a1
        a11 = list(reversed(a1))
    # Tìm tập giá trị a2 từ j2 đến số 0 tiếp theo phía bên trái
        a2 = find_nearest_zero_left(new_solution, index_j2)
    # Tạo a22 bằng cách nghịch đảo a2
        a22 = list(reversed(a2))
    # Loại bỏ các dấu ngoặc và xóa chuỗi con giống a1 và a2
        new_solution = [x for x in new_solution if x not in a1]
    # Thêm a11 sau j2 và a22 trước j1 trong new_solution
        new_solution[index_j2-1:index_j2-1] = a11
        new_solution[index_j1:index_j1] = a22
        position_of_8 = new_solution.index(a11[0])
# Xóa số trước số 8 và số 0 (nếu có) cho đến khi số trước 8 là 0
        while position_of_8 > 0 and new_solution[position_of_8 - 1] != 0:
            del new_solution[position_of_8 - 1]
            position_of_8 -= 1
# Xóa số 0 nếu có
        if new_solution[position_of_8 - 1] == 0:
            del new_solution[position_of_8 - 1]
        i = 0
        while i < len(new_solution) - 1:
            if new_solution[i] == 0 and new_solution[i + 1] == 0:
                del new_solution[i]
            else:
                i += 1
    so_chuyen = 0
    for item in solution:
        if item == 0:
            so_chuyen += 1
    #print(so_chuyen)
    if so_chuyen < Kmin:
        new_solution = []
    return new_solution

#print(S)
   