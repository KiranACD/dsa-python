from locale import currency


class Solution:

	# @param A : list of integers
	# @return a list of list of integers
    def fact(self, n):
        ans = 1
        while n:
            ans *= n
            n = n-1
        return ans

    def permute(self, A):

        n = len(A)
        def get_perms(curr_list, A, ans, n):
            if len(curr_list) == n:
                ans.append(curr_list.copy())
                print('ans: ', ans)
                return
            
            for i in range(n):
                if A[i] in curr_list:
                    continue
                print(curr_list)
                curr_list.append(A[i])
                get_perms(curr_list, A, ans, n)
                curr_list.pop(-1)
        
        ans = []
        curr_list = []
        get_perms(curr_list, A, ans, n)

        return ans
        

if __name__ == '__main__':
    sol = Solution()

    A = input()
    A = list(map(int, A.split()))
    print(sol.permute(A)) 