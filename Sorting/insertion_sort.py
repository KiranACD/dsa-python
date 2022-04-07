from http.client import ImproperConnectionState
from swap import swap_num
from enterarray import enter_array

def insertion_sort_fn(arr):

    n = len(arr)

    for i in range(1, n):
        j = i-1
        while (arr[j+1] < arr[j]) and (j >= 0):
            arr[j+1], arr[j] = swap_num(arr[j+1], arr[j])
            j -= 1
    
    return arr

if __name__ == '__main__':

    arr = enter_array()
    print(insertion_sort_fn(arr))