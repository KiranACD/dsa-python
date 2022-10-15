from asyncio import current_task
from locale import currency


def is_perfect_square(n):
    s = 0
    e = n
    while(s<=e):
        mid = s+(e-s)//2
        ans = mid*mid
        if ans == n:
            return True
        elif ans > n:
            e = mid - 1
        else:
            s = mid + 1
    return False

def is_squareful(a):

    n = len(a)
    for i in range(1, n):
        if not is_perfect_square(a[i] + a[i-1]):
            return False
    return True

def num_squareful(A):

    def permute(curr_list, index_list, n, A, ans):
        print('here')
        print(n)
        print(len(curr_list))

        if len(curr_list) > 1 and not is_perfect_square(curr_list[-1]+curr_list[-2]):
            print('return becuase adj elements not perfect square')
            print('curr_list: ', curr_list)
            print('-------------------------------------')
            return 0
        if len(curr_list) == n:
            print('end of array')
            print('curr_list: ', curr_list)
            print('ans: ', ans)
            if curr_list not in ans:
                ans.append(curr_list.copy())
                print('return 1')
                print('-------------------------------------')
                return 1
            else:
                print('-------------------------------------')
                return 0

        c = 0
        for i in range(n):
            if i in index_list:
                continue
            print(f'A[{i}]: ', A[i])
            print('i: ', i) 
            print('index_list: ', index_list)
            print('c: ', c)
            print('-------------------------------------')
            curr_list.append(A[i])
            index_list.append(i)
            print('after append')
            print(f'A[{i}]: ', A[i])
            print('i: ', i) 
            print('index_list: ', index_list)
            print('c: ', c)
            print('-------------------------------------')
            c += permute(curr_list, index_list, n, A, ans)
            curr_list.pop(-1)
            index_list.pop(-1)
            print('after pop')
            print(f'A[{i}]: ', A[i])
            print('i: ', i) 
            print('index_list: ', index_list)
            print('c: ', c)
            print('-------------------------------------')
        return c
        
    curr_list = []
    index_list = []
    ans = []
    n = len(A)
    c = permute(curr_list, index_list, n, A, ans)
    print(ans)
    return c

A = [1, 17, 8]
print(num_squareful(A))

print(is_squareful([17,8,1]))