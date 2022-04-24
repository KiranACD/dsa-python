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