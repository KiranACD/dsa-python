# Binary Search Tree

For all nodes, all elements on the left side of the root are smaller than the root value and all elements on the right side of the root are larger than the root value.

When two nodes have equal values, we can place them on the left or the right side of the root, with the caveat that, the same rule should be followed for the entire tree.
```
       Some examples of BST                           This is not a binary tree because 8 is 
                                                                 to the right of 10

    2              1               1                                    10         
   / \                              \                                  /  \
  1   3                              2                                5    12
                                      \                              /     / \ 
                                       4                            4     8   14
                                        \
                                         6

```
A tree with only a null node is also a binary search tree as there is nothing else to compare it to.

## Given a binary search tree, insert a value maintaining the BST property

Assumption: insert(node, k) will insert k at the appropriate position in tree rooted at node and returns the updated root.

```
def insert(root, k):
    if root is None:
        return TreeNode(k)
    
    if k > root.val:
        root.right = insert(root.right, k)
    else:
        root.left = insert(root.left, k)
    
    return root
```
TC: O(N) - If all the nodes in a BST are along the left side and we have to insert at the last node.
SC: O(N) - The space required by the recursion stack.

## Given a binary search tree, check if target k is present in it.

After traversing the BST, if we reach Null root, then value is not present. 
```
def search(root, k):
    if root is None:
        return False
    if root.val == k:
        return True
    if root.val > k:
        return search(root.left, k)
    else:
        return search(root.right, k)
```

TC: O(N)
SC: O(N)

## Given a binary search tree, delete a value k from it.

Assume there are no duplicates.

Case 1: k is present at a leaf node, so we just have to make it Null.

Case 2: k is present at a node with only 1 child. After deletion, return the non-null child.

Case 3: k is present at a node with 2 children. Replace the node to be deleted by the max(left sub tree) and delete the max or by min(right sub tree) and delete the min.

```
def isleaf(root):
    if root.left is None and root.right is None:
        return True
    else:
        return False

def has1child(root):
    if root.left and root.right is None:
        return True
    elif root.right and root.left is None:
        return True
    else:
        return False

def max_sub_tree(root):
    while root.right is not None:
        root = root.right
    return root
    
def delete(root, k):
    if root is None:
        return root
    if root.val > k:
        root.left = delete(root.left, k)
    elif root.val < k:
        root.right = delete(root.right, k)
    else:
        if isleaf(root):
            return None:
        elif has1child(root):
            if root.left:
                return root.left
            if root.right:
                return root.right
        else:
            max_sub_tree = get_max(root.left)
            root.val = max_sub_tree.val
            root.left = delete(root.left, max_sub_tree.val)

    return root
```
TC: O(N) to find the node. O(N) to find the max. So O(N)
SC: O(N)

Try to delete without swapping the values

## Given a BST and a range l to h, delete every node which has a val outside the range [l,h]

Approach 1:
Use the delete function from above. When we reach a node whose value is outside the range, then call the delete function for that node.

TC: O(N^2)
SC: O(N^2)

Approach 2:
```
def trim(node):
    if not node:
        return None
    if node.val > h:
        return trim(node.left)
    elif node.val < l:
        return trim(node.right)
    else:
        node.left = trim(node.left)
        node.right = trim(node.right)
        return node
```
TC: O(N)
SC: O(N)

## Given a binary tree, return True if it is a BST.

Assume no duplicates. Solve using all three traversals

Approach 1: Preorder traversal
```
def isBst(root, lower, upper):
    if root is None:
        return True
    return ((lower < root.val < upper) 
            and isBst(root.left, lower, root.val)
            and isBst(root.right, root.val, upper)
```
Edge cases are if the root value itself is INT_MAX or INT_MIN. If a node is INT_MAX and the right subtree is not None, then the tree cannot be a BST. However if duplicates are allowed, send None as lower and upper. Perform the comparison, only if the node is not none.

Approach 2: Inorder traversal
Inorder traversal of_ BST will always return a sorted array.
TC: O(N)
SC: O(N)

Approach 3: Postorder traversal
Information needed for each node: Max from left sub tree and min from right sub tree. if lst is a BST and if rst is a BST

In this case return will be an object. Lets use a named tuple.
```
from collections import namedtuple

TreeInfo = namedtuple('TreeInfo', 'min max is_bst')

def isBST(root):
    if root is None:
        return TreeInfo(INT_MAX, INT_MIN, True)
    left = isBST(root.left)
    right = isBST(root.right)

    if (left.is_bst and right.is_bst and root.val>left.max and root.val<right.min):
        return TreeInfo(min(root.val, left.min, right.min), max(root.val, left.max, right.max), True)
    else:
        return TreeInfo(min(root.val, left.min, right.min), max(root.val, left.max, right.max), False)
```

## Given a BT, return the size of max BST sub-tree inside the BT.

```
                            5
                           / \
                          2   4
                         / \ 
                        1   3 
```
The subtree rooted at 2 is the max BST. So the answer is 3.

Approach:
The root node needs to know the max size BST subtree on left side, the max size BST subtree on the right side and whether the tree from the current node itself is a BST.
```
from collections import namedtuple

TreeInfo = namedtuple('TreeInfo', 'max min is_bst max_bst curr_size')

def maxBST(root):
    if root is None:
        return TreeInfo(INT_MIN, INT_MAX, True, 0, 0)

    left = maxBST(root.left)
    right = maxBST(root.right)

    if (left.is_bst and right.is_bst and root.val < right.min and root.val > left.max):
        return TreeInfo(right.max, 
                        left.min, 
                        False, 
                        right.curr_size + left.curr_size + 1,
                        right.curr_size + left.curr_size + 1)
    else:
        return TreeInfo(max(root.val, left.max, right.max),
                        min(root.val, left.min, right.min),
                        False,
                        max(left.max_bst, right.max_bst),
                        right.curr_size + left.curr_size + 1)
```

## Given a BST where two nodes have been swapped. Fix it.

Approach:

Do an inorder traversal of the tree and append all nodes into a list. Then find the nodes where there is a violation of the sorted order. In the first occurence of this, the first node is the incorrect node and in the second occurence of this, the second node is the incorrect node. In case of two adjacent swapped nodes, there will be only one occurence of violation of the sorted order. In this case the two nodes are the swapped nodes.
```
lst = []

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    lst.append(root)
    inorder(root.right)

ans = []
for _ in range(1, len(lst)):
    if lst[_].val < lst[_-1].val:
        lst.append(lst[_-1])
        lst.append(lst[_])

n1 = ans[0]
n2 = ans[-1]
```
Approach 2:

This can be done with constant space. We just have to maintain the prev node we travelled to.
```
n1 = None
n2 = None
prev = None

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    if prev is not None:
        if root.val < prev.val:
            if n1 is None:
                n1 = prev
                n2 = root
            else:
                n2 = root
    prev = root
    inorder(root.right)
```

            