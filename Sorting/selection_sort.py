# Get a stable implementation of selection sort using <= instead of <
from enterarray import enter_array
from swap import swap_num

def selection_sort(arr):

    n = len(arr)

    for i in range(n):
        min_num = arr[i]
        ind = i
        for j in range(i, n):

            if arr[j] < min_num:
                min_num = arr[j]
                ind = j

        arr[i], arr[ind] = swap_num(arr[i], arr[ind])        
    
    return arr

if __name__ == '__main__':
    
    arr = enter_array()
    print(selection_sort(arr))