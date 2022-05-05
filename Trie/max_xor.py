class TrieNode:
    def __init__(self):
        self.hmap = {}
        self.index = None

class Solution:

    def __init__(self):
        pass
    
    def insert(self, num, idx):
        curr = self.root
        for i in range(31, -1, -1):
            x = (num>>i)&1
            if x not in curr.hmap:
                curr.hmap[x] = TrieNode()
            curr = curr.hmap[x]
        curr.index = idx
    
    def get_max_xor(self, num):
        xor = 0
        curr = self.root
        for i in range(31, -1, -1):
            x = (num>>i)&1
            if (1-x) in curr.hmap:
                xor += (1<<i)
                curr = curr.hmap[1-x]
            else:
                xor += 0
                curr = curr.hmap[x]
        return xor, curr.index

    def solve(self, A):
        
        self.root = TrieNode()
        n = len(A)
        max_xor = A[0]
        ans = [0, 0]
        for i in range(1, n):
            A[i] = A[i-1]^A[i]
            if A[i]>max_xor:
                max_xor = A[i]
                ans[1] = i 
        
        print(A)
        for i in range(n):
            self.insert(A[i], i)
        
        for i in range(n):
            xor, idx = self.get_max_xor(A[i])
            if idx <= i:
                s = idx + 1
                e = i
            else:
                s = i + 1
                e = idx
            print(s, e)
            print(xor)
            print(max_xor)
            
            if xor > max_xor:
                ans[0] = s
                ans[1] = e
                max_xor = xor
            elif xor == max_xor:
                if (e-s) < (ans[1]-ans[0]):
                    ans[0] = s
                    ans[1] = e
                elif (e-s) == (ans[1]-ans[0]):
                    if s < ans[0]:
                        ans[0] = s
                        ans[1] = e
            # print(ans)
            print('----------------------------------------------')
        ans[0] += 1
        ans[1] += 1

        return ans

if __name__ == '__main__':
    sol = Solution()
    A = input()
    A = list(map(int, A.split()))
    print(sol.solve(A))
