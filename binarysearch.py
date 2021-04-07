array = sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
search_element = int(input('enter the number'))


def binarysort(start_index: int, end_index: int):
    print(array)
    print(start_index, end_index)
    mid = int((start_index + end_index) / 2)
    print(mid)

    if search_element == array[mid]:
        return mid

    if search_element > array[mid]:
        return binarysort(start_index=mid + 1, end_index=end_index)

    if search_element < array[mid]:
        return binarysort(start_index=start_index, end_index=mid - 1)


print('the result is  {}'.format(binarysort(0, len(array) - 1)))
