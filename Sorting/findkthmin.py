# Given array, find kth minimum. k < log N. N = Size of aarray

from swap import swap_num

def find_kth_min(arr, k):

    n = len(arr)

    for i in range(k):
        for j in range(i, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = swap_num(arr[i], arr[j])
    
    return arr[k-1]

def enter_array():

    arr = input('Enter the array as a string with "," seperating the elements: ')
    arr = arr.split(',')
    arr = list(map(lambda x: int(x), arr))

    k = int(input('Enter k: '))

    return find_kth_min(arr, k)

if __name__ ==  '__main__':
    
    print(enter_array())
