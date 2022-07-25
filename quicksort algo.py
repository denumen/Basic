import numpy


arr = [1, 3, 5, 90, 35, 80, 54, 75]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    arr = numpy.array(arr)
    p = arr[len(arr) // 2]
    array_left = [x for x in arr if x < p]
    array_right =[x for x in arr if x > p]
    array_middle =[x for x in arr if x == p]
    return quick_sort(array_left) + array_middle + quick_sort(array_right)
print(quick_sort(arr))
