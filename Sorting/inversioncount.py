# Given an array, count the number of inversion pairs, such that i < j and A[i] > A[j]
from enterarray import enter_array
from count_pairs import getpaircount

def inversion_count(arr, l, r):

    count = 0
    if l >= r:
        return count
    
    mid = l + (r - l + 1)//2

    count1 = inversion_count(arr, l, mid-1)
    count2 = inversion_count(arr, mid, r)

    return count1 + count2 + getpaircount(arr[l:mid], arr[mid:r+1])

if __name__ == '__main__':

    arr = enter_array()
    n = len(arr)
    print(inversion_count(arr, 0, n-1)) 