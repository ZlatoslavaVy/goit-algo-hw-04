import timeit
import random


# 1. Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 2. Сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Основна частина ---

def measure_time(sort_func, data):
    start = timeit.default_timer()
    sort_func(data[:])
    return timeit.default_timer() - start

# Різні набори даних
sizes = [100, 1000, 2000] 

print(f"{'Size':<10} | {'Insertion':<10} | {'Merge':<10} | {'Timsort':<10}")
print("-" * 50)

for size in sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    
    t_ins = measure_time(insertion_sort, data)
    t_mer = measure_time(merge_sort, data)
    t_tim = measure_time(sorted, data)
    
    print(f"{size:<10} | {t_ins:.5f}    | {t_mer:.5f}    | {t_tim:.5f}")

# Висновки
print("\n--- Висновки ---")
print("1. Timsort найшвидший, бо це вбудований алгоритм на C.")
print("2. Insertion sort дуже повільний на великих даних (O(n^2)).")
print("3. Merge sort ефективний, але повільніший за Timsort.")