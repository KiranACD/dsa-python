# Given 2 arrays of N and M. Count pairs such that A[i] > B[j]
from enterarray import enter_array
from merge_sort import merge_sort_fn
def getpaircount(arr1, arr2):

    n = len(arr1)
    m = len(arr2)

    arr1 = merge_sort_fn(arr1, 0, n-1)
    arr2 = merge_sort_fn(arr2, 0, m-1)

    t1 = 0
    t2 = 0

    ans = []
    count = 0
    while(t1<n and t2<m):
        if arr1[t1] > arr2[t2]:
            count += n - t1
            t2 += 1
        else:
            t1 += 1
    
    return count

if __name__ == '__main__':

    arr1 = enter_array()
    arr2 = enter_array()
    print(getpaircount(arr1, arr2))
