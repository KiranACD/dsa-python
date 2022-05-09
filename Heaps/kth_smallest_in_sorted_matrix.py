import heapq

def solve(A, B):

    heap = []
    n = len(A)
    m = len(A[0])

    for i in range(n):
        heapq.heappush(heap, (A[i][0], (i, 0)))
    
    print(heap)
    print('----------------------------------------')
    k = B
    while (len(heap) and k):
        k -= 1
        if k == 0:
            break
        
        num, idx = heapq.heappop(heap)
        i, j = idx
        if j < m-1:
            heapq.heappush(heap, (A[i][j+1], (i, j+1)))
        print(A[i][j])
    num, idx = heapq.heappop(heap)

    return num

if __name__ == '__main__':

    n = int(input('Number of rows: '))
    m = int(input('Number of columns: '))
    B = int(input('B: '))

    A = []

    for i in range(n):
        rows = []
        for j in range(m):
            i = int(input('Num: '))
            rows.append(i)
        A.append(rows)
    print('----------------------------------------')
    print(A)
    print('----------------------------------------')
    print(solve(A, B))