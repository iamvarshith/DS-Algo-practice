# pairsum problem in python with dicts and without sorting

arr = [i for i in range(200)]

target_element = 26
might_be_dict = {}

for i in range(len(arr) - 1):

    if arr[i] in might_be_dict.keys():
        print(f'This pair {arr[i]},{target_element - arr[i]} are the two elements at the index of the '
              f'{might_be_dict[arr[i]]} and {i}')
    else:
        might_be_dict[(target_element - arr[i])] = i
