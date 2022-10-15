def combo_sum(j, curr_list, k, A, B, ans, n):

    if (k==B):
        ans.append(curr_list.copy())
        return
    if (k > B):
        return
    
    for i in range(j, n):
        k += A[i]
        curr_list.append(A[i])
        combo_sum(i, curr_list, k, A, B, ans, n)
        k -= A[i]
        curr_list.pop(-1)

A = input()
A = list(map(int, A.split()))
B = int(input())
curr_list = []
k = 0
ans = []
n = len(A)
combo_sum(0, curr_list, k, A, B, ans, n)
print(ans)

x = [2, 2, 3]
y = [2, 2, 3]
z = [x]
print(y in z)
