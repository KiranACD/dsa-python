from enterarray import enter_array

def check_consecutive_using_min(arr):

    n = len(arr)

    min_val = arr[0]

    for _ in range(1, n):
        if arr[_] < min_val:
            min_val = arr[_]
    
    s = 0
    for _ in range(n):
        s += arr[_] - min_val
    
    if s == n*(n-1)/2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    arr = enter_array()
    print(check_consecutive_using_min(arr))