import time
import random
import matplotlib.pyplot as plt


def merge(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)


def insertion(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and (j > 0):
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1


elements = []
merge_timer = []
insertion_timer = []

for i in range(5):
    array = random.sample(range(1, 100000000), 10 ** i)

    merge_time_start = time.process_time()
    merge_sort(array)
    merge_time_end = time.process_time()

    insertion_timer_start = time.process_time()
    insertion(array)
    insertion_timer_end = time.process_time()

    elements.append(10000 * i)
    merge_timer.append(merge_time_end - merge_time_start)
    insertion_timer.append(insertion_timer_end - insertion_timer_start)

plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.plot(elements, merge_timer, color='r', label='merge Sort')
plt.plot(elements, insertion_timer, color='g', label='Insertion Sort')

plt.grid()
plt.legend()
plt.show()
