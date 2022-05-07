# Heaps

Given lengths of N ropes, merge all of them to form a single rope. In one merge operation pick 2 ropes and merge them. The cost of a merge operation is the sum of the length of the two ropes.

Cost(merge(r1, r2)) = len(r1) + len(r2)

Minimize the overall cost of merging

Approach 1: 

- Sort the lengths of the ropes in ascending order.
- Take the smallest two ropes and merge them.
- Insert the merged length into the sorted array in such a way that the array remains sorted in the ascending order. Remove the two lengths used to merge
- Repeat steps 2 and 3 till all ropes are merged.

TC: O(Nlog(N)) + O(N^2)
SC: O(1)

Approach 2: If we make a balanced binary search tree from the given information, we can perform the merge operations in log(n) time complexity. After every insert operation, we will have to balance the binary tree.

Approach 3: Use Heap data structure. The operations we have to use are get_min()/extract_min and insert().

As approach 2 requires us to use data structures like AVL tree or red-black trees, which are complicated data structures, we will use heap to implement the above solution.

## Characteristics

### Complete Binary Tree

All levels are completely filled except, possibly, the last level. The nodes in the last level are all left aligned if the last level is not completely filled.

The height of a heap is log(N). The number of nodes in the last level = N/2.

### Minimum or Maximum Property

Value of a node must be greater (max heap) / smaller (min heap) than both LST and RST. This has to be followed by all the nodes of the binary tree.

### Implementation

Heap is stored as an array/list. The elements of the heap follow a tree structure logically. So, given a node at index i, its children will be at (2i + 1) and (2i + 2). Given a node j, its parent will be at (j-1)//2.

### Insertion

- Append the value to be inserted at the end of the heap. 
- Compare with parent to find whether it is smaller.
- If smaller, swap with parent. 
- Repeat steps 2 and 3 till we reach the top of the tree.
```
def insert(k):
    A.append(k)
    n = len(A)
    i = n-1
    while (i>0):
        p = (i-1)//2
        if (A[p] > A[i]):
            A[p], A[i] = A[i], A[p]
            i = p
        else:
            break
```

### Deletion

Deleting the index at the end of the array/list is an O(1) operation. At every other index, we will have to shift the elements after the index back 1 place.

#### Delete min from min-heap

- Swap the first and last element. 
- Delete the last element.
- Compare the first element with its children. Swap with any of the child that is smaller.
- Continue till either we reach the end of the array or the resulting node satisfies the min-heap characteristics.
```
def delete():
    A[0], A[-1] = A[-1], A[0]
    ans = A.pop(-1)
    n = len(A)
    i = 0
    while (i < n):
        min_idx = i
        l = (2*i) + 1
        r = (2*i) + 2
        if (l < n) and (A[l] < A[min_idx]):
            min_idx = l
        if (r < n) and (A[r] < A[min_idx]):
            min_idx = r
        if min_idx == i:
            break
        A[i], [min_index] = A[min_index], A[i]
        i = min_index
    return ans
```

## Convert Array to Heap






