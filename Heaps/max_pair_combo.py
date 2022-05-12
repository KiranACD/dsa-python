class Heap:
    def __init__(self):
        self.heap = []
    
    def insert(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1
        while (i>0):
            p = (i-1)//2
            if self.heap[p][0] > self.heap[i][0]:
                self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
                i = p
            else:
                break
    
    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ans = self.heap.pop(-1)
        i = 0
        while i < len(self.heap):
            min_idx = i
            l = (2*i) + 1
            r = (2*i) + 2
            if l<len(self.heap) and self.heap[min_idx][0] > self.heap[l][0]:
                min_idx = l
            if r<len(self.heap) and self.heap[min_idx][0] > self.heap[r][0]:
                min_idx = r
            if min_idx == i:
                break
            self.heap[i], self.heap[min_idx] = self.heap[min_idx], self.heap[i]
            i = min_idx
        return ans

class Solution:
    def __init__(self):
        pass

    def solve(self, A, B):

        n = len(A)
        A.sort(reverse=True)
        B.sort(reverse=True)

        index_set = set()
        max_pair_heap = Heap()
        ans = []
        max_pair_heap.insert((-(A[0]+B[0]), (0, 0)))

        while (len(ans)<n):
            item = max_pair_heap.pop()
            print(max_pair_heap.heap)
            print(item)
            print(index_set)
            print('------------------------------------')
            if item[1] not in index_set:
                ans.append(-item[0])
                index_set.add(item[1])

            if len(ans) == n:
                break

            index = item[1]
            first_index = (index[0]+1, index[1])
            second_index = (index[0], index[1]+1)

            if (first_index[0] < n and first_index not in index_set):
                max_pair_heap.insert((-(A[first_index[0]] + B[first_index[1]]), (first_index)))
                
            if (second_index[1] < n and second_index not in index_set):
                max_pair_heap.insert((-(A[second_index[0]] + B[second_index[1]]), (second_index)))

        return ans
if __name__ == '__main__':
    # A = input('First list: ')
    # B = input('Second list: ')

    # A = list(map(int, A.split()))
    # B = list(map(int, B.split()))

    # A = [2, 1, 5, 6]
    # B = [2, 3, 1, 4]
    A = [ 36, 27, -35, 43, -15, 36, 42, -1, -29, 12, -23, 40, 9, 13, -24, -10, -24, 22, -14, -39, 18, 17, -21, 32, -20, 12, -27, 17, -15, -21, -48, -28, 8, 19, 17, 43, 6, -39, -8, -21, 23, -29, -31, 34, -13, 48, -26, -35, 20, -37, -24, 41, 30, 6, 23, 12, 20, 46, 31, -45, -25, 34, -23, -14, -45, -4, -21, -37, 7, -26, 45, 32, -5, -36, 17, -16, 14, -7, 0, 37, -42, 26, 28 ]
    B = [ 38, 34, -47, 1, 4, 49, -18, 10, 26, 18, -11, -38, -24, 36, 44, -11, 45, 20, -16, 28, 17, -49, 47, -48, -33, 42, 2, 6, -49, 30, 36, -9, 15, 39, -6, -31, -10, -21, -19, -33, 47, 21, 31, 25, -41, -23, 17, 6, 47, 3, 36, 15, -44, 33, -31, -26, -22, 21, -18, -21, -47, -31, 20, 18, -42, -35, -10, -1, 46, -27, -32, -5, -4, 1, -29, 5, 29, 38, 14, -22, -9, 0, 43 ]

    sol = Solution()
    print(sol.solve(A, B))  