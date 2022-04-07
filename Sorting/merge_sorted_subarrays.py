from enterarray import enter_array
from swap import swap_num

def merge(arr, l, y, r):

    t1 = l
    t2 = y
    ans = []
    while (t1 < y and t2 < r+1):
        if arr[t1] <= arr[t2]:
            ans.append(arr[t1])
            t1 += 1
        else:
            ans.append(arr[t2])
            t2 += 1
    
    while (t1 < y):
        ans.append(arr[t1])
        t1 += 1
    
    while (t2 < r+1):
        ans.append(arr[t2])
        t2 += 1
    
    arr[l:r+1] = ans

    return arr

if __name__ == '__main__':
    arr = enter_array()
    l = int(input('Enter l: '))
    y = int(input('Enter y: '))
    r = int(input('Enter r: '))
    print(merge(arr, l, y, r))
