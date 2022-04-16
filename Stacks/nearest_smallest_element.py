# Nearest smaller element
# For every i, find the nearest element on the left side of i which is smaller than A[i]
# Implement to return the index
# Implement to get the distance from the nearest smaller element.
# Max rectangle area of a histogram
import sys
sys.path.append('/home/kiran/dsa-python/Sorting')
from enterarray import enter_array

def smaller_element(arr):

    n = len(arr)
    stack = []
    top = -1
    ans = []
    for _ in range(n):

        if top == -1:
            stack.append(arr[_])
            top += 1
            ans.append(-1)
            continue

        while(top != -1):
            if arr[_] > stack[top]:
                ans.append(stack[top])
                stack.append(arr[_])
                top += 1
                break
            else:
                stack.pop(top)
                top -= 1
        
        if top == -1:
            ans.append(-1)
            stack.append(arr[_])
            top += 1
    
    return ans


if __name__ == '__main__':
    arr = enter_array()
    print(smaller_element(arr))