# Given 2 sorted arrays of size n and m, merge and return a new sorted array
from enterarray import enter_array

def merge(arr1, arr2):

    n1 = len(arr1)
    n2 = len(arr2)
    t1 = 0
    t2 = 0
    ans = []

    while (t1<n1 and t2<n2):

        if arr1[t1]<arr2[t2]:
            ans.append(arr1[t1])
            t1 += 1
        else:
            ans.append(arr2[t2])
            t2 += 1
    
    while (t1<n1):
        ans.append(arr1[t1])
        t1 += 1
    
    while (t2<n2):
        ans.append(arr2[t2])
        t2 += 1
    
    return ans

if __name__ == '__main__':
    arr1 = enter_array()
    arr2 = enter_array()
    print(merge(arr1, arr2))