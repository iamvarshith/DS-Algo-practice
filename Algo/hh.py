arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,12,18]
k = 4

counter =0
for j in range(k):
    counter += arr[j]


sub_arr = [counter]
for i in range(len(arr)-1):
    counter