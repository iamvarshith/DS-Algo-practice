# given an array of n elements and give 'i' is an integer.
# Find the total number of trios which can be summed up to the value 'i'

arr = [12, 3, 4, 1, 6, 9]
sorted_array = sorted(arr)
print(sorted_array)
target_element = 24

for k in range(len(arr) - 2):
    i = k + 1
    j = len(sorted_array) - 1

    while i < j:

        if sorted_array[i] + sorted_array[j] == target_element - sorted_array[k]:
            print(sorted_array[i], sorted_array[j], sorted_array[k])
            i += 1
            j -= 1
        if sorted_array[i] + sorted_array[j] > target_element - sorted_array[k]:
            j -= 1

        if sorted_array[i] + sorted_array[j] < target_element - sorted_array[k]:
            i += 1
