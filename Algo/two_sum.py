# given an array of n elements and give 'i' is an integer.
# Find the total number of pairs which can be summed up to the value 'i'

arr = [0, 1, 4, 5, 6, 3]
sorted_array = sorted(arr)
print(sorted_array)
taget_element = 9

i = 0
j = len(sorted_array) - 1

while i != j:
    if sorted_array[i] + sorted_array[j] == taget_element:
        print(sorted_array[i], sorted_array[j])
        i += 1
        j += 1
    if sorted_array[i] + sorted_array[j] < taget_element:
        print('No element found')
        break
    if sorted_array[i] + sorted_array[j] > taget_element:
        j -= 1
        pass
