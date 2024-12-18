import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_sorting_time(sort_func, array_size, num_iterations=5):

    total_time = 0
    for _ in range(num_iterations):
        arr = [random.randint(0, array_size) for _ in range(array_size)]
        start_time = time.time()
        sort_func(arr)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / num_iterations



start_s = 100
end_s = 1500
step_s = 50
num_iterations = 5
sizes = range(start_s, end_s+ 1, step_s)


bubble_sort_time = []
selection_sort_time = []
insertion_sort_time = []

# Измерение времени сортировки для каждого размера массива
for size in sizes:
    bubble_time = measure_sorting_time(bubble_sort, size, num_iterations)
    selection_time = measure_sorting_time(selection_sort, size, num_iterations)
    insertion_time = measure_sorting_time(insertion_sort, size, num_iterations)

    bubble_sort_time.append(bubble_time)
    selection_sort_time.append(selection_time)
    insertion_sort_time.append(insertion_time)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_sort_time, label='Bubble Sort')
plt.plot(sizes, selection_sort_time, label='Selection Sort')
plt.plot(sizes, insertion_sort_time, label='Insertion Sort')
plt.xlabel('Размер массива')
plt.ylabel('Время сортировки ')
plt.title('Зависимость времени сортировки от размера массива')
plt.legend()
plt.grid(True)
plt.show()
