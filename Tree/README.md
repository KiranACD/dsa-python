# Trees

## Hierarchical data structure

Arrays, linked-lists are linear data structures. Trees bring hierarchy into the picture. All the nodes are connected one single node. This single node is like the oldest living member in your family, like your grandfather or grandmother or your great-grandmother. The nodes just below are children of this single node. This single node is called the root node.  

## Root Node

Root node has no parent. They only have children. Root node is a parent node that has no parent. 

Just like your root node can have no parent, a node that can have no children is called the leaf node.

## Leaf Node

Leaf nodes are the ending nodes of a tree as they have no children. 

Leaf node has no children

## Parent Nodes and Children Nodes

Traversal in the tree structure is always from parent to child. We cannot go from a child node to the parent node. 

For a given single node, the nodes that are directly connected to this single node and are reachable are its children nodes. The single node itself will then be their parent node.

## Edges

The connection between two nodes is an edge. 

If a tree has N nodes, how many edges are there? 

Irrespective of the number of children a node has, each node will have only 1 parent. There is only one exception to this, the root node. The root node has no parent. Hence there are N-1 edges. 

## Height of a node

Distance from the node to the farthest reachable leaf node. The distance can be measured as the number of edges between the node and the farthest reachable leaf node. A leaf node has a height of 0.

Depending on the person, the height of a node can also be the number nodes between it and the farthest reachable node.

Height of a NULL node is -1.

## Depth of a node

This is the distance from the root to the node in question. The distance be measured as the number of edges between the root and the node.

## Height of a binary tree

Height of a binary tree is the height of the root node, which is the distance from the root node to the farthest reachable leaf node.

## Structure of a Node

Binary tree has maximum 2 children per node. Ternary tree has maximum 3 children per node. Quad tree has maximum 4 children per node.

```
# Binary Tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

```
# N number of children

class Node:
    def __init__(self, val):
        self.val = val
        self.children = [None for _ in range(n)]
```
## Complete Binary Tree

A binary tree where all levels of the tree are completely filled, except possibly the last level. In case, the last level is not completely filled, they have to be left aligned.

The number of nodes in a complete binary tree can be expressed as:

2^0 + 2^1 + 2^2 + 2^3 + ... + 2^h = N

a = 2^0
r = 2
n = h+1

LHS can be written as:

(2^(h+1) - 1)/(2 - 1) = N

h = log(N+1) -1

Number of nodes in the last level, n = 2^h

n = 2^(log(N+1) - 1)

n = (2^log(N+1)) / 2

n = (N + 1) / 2

## Tree Traversals

The convention is that the left child will be visited before the right node. 

How many ways to traverse a tree? 3 - PreOrder, InOrder, PostOrder

### PreOrder

Visit root, left, right
```
def preorder(root):
    if root is None:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)
```
This is a depth first search. This algorithm can be used in an application that requires a fail fast approach. For e.g., Given 2 trees, check if they are identical. If the two root values do not match, then we can return False. PreOrder helps us here as we check the root node first and then traverse to the sub trees. If the root nodes dont match, then we do not need to traverse to the sub trees and we can return False fast.

TC : O(N)
SC : O(N) - Order of height of the tree, because we use the recursion stack. In the worst case scenario, all the nodes will be on one side of the tree.

Given a tree, search a val k in it
```
def search(root, k):
    if root is None:
        return False
    if root.val == k:
        return True
    return search(root.left, k) or search(root.right, k) # Makes use of boolean short circuting
```

### InOrder
    - Visit left, root, right
```
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```
Most problems in binary tree are solved using preOrder or postOrder traversal. InOrder traversal is useful when dealing with binary search trees or when there is a specific order present.

### PostOrder

Visit left, right, root
```
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)
```
This is a depth first search. Flow of control is from the bottom to the top because we are using recursion. This is different from the preorder traversal where data is processed from top to bottom.  

Postorder is handy when we need to use data from the left and right side of a node. 
For e.g., given a tree, return its height. 
```
def height(root):
    if root is None:
        return -1 # Height of Null node is -1
    return max(height(root.left), height(root.right)) + 1
```
Given a tree, count number of nodes of a tree
```
def num_nodes(root):
    if root is None:
        return 0
    return num_nodes(root.left) + num_node(root.right) + 1
```
Using this traversal, we can find max node value, sum of all node values and other problems like these.

### Level Order Traversal

We have to use a queue here. We print the value of the root node first and insert its children into the queue. Then `popleft()` from the queue and print its value and insert its children into the queue.

Continue this operation till the queue is empty.
```
q = deque()
node = root
print(node.val)
if node.left:
    q.append(node.left)
if node.right:
    q.append(node.right)
while (q):
    node = q.popleft()
    print(node.val)
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)
```
Return a list of lists where each list consists of values of the nodes of each level of the tree

- Approach 1
Combine the level of the node with the node while appending to the queue. This way we can start a new list when we detect level change.

TC: O(N)
SC: O(width of the tree) + Level being added = O(N)

- Approach 2
Append Nonetype object to the queue each time we pop out a Nonetype object. When a Nonetype object is popped, start a new list.

TC: O(N) + O(logN)
SC: O(width of the tree)

- Approach 3
Keep track of the size of queue. When first node in queue, number of pops needed to get to the next level is equal to 1, which is also the size of the queue. When one pop is done, we record the size of the queue again. In this case, it is going to be 2 nodes. Once 2 pops are done, record the size of the queue again.

```
def level_order(root):
    if root is None:
        return None
    
    ans = []
    q = deque()
    q.append(root)
    while (q):
        level = []
        size = len(q)
        for i in range(n):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    
    return ans
```

### Vericial Order Traversal

                                       9         Output: [[7],
                                      / \                 [2, 14],
                                     /   \                [6, 11, 5],
                                    6     4               [9, 3, 8],
                                   / \   / \              [4, 12],
                                  /   \ /   \             [1]]
                                 2    3 8    1
                                / \  /      /
                               /   \/      / 
                              7  11  5    12
                               \
                                \
                                14

Use a hashmap with keys as the distance of each node from the root node. Then when we move to the left, we decrement the distance by 1. When we move to the right, we increment the distance by 1.

We cannot do this using a depth first search. We have to use level order traversal
```
TreeInfo = collections.namedtuple('TreeInfo', 'node dist')

hmap = default_dict(list)
node = root
q = deque()
q.append(TreeInfo(node, 0))
min_dist = 0
max_dist = 0
while q:
    node_info = q.popleft()
    min_dist = min(min_dist, node_info.dist)
    max_dist = max(max_dist, node_info.dist)
    hmap[node_info.dist].append(node_info.node.value)
    if node_info.node.left is not None:
        q.append(TreeInfo(node_info.node.left, node_info.dist - 1))
    if node_info.node.right is not None:
        q.append(TreeInfo(node_info.node.right, node_info.dist + 1))
```
    
## Build binary tree using preorder and inorder traversal arrays

First element of a preorder array will be the root of the tree. Find the position of the root value in the inroder array. Elements to the left of the position in the inorder array will be elements that constitute the left tree and elements to the right of the position in the inorder array will be elements that constitire the right tree. Get the root of all subtrees recursively and finally return the root of the fully constructed tree.

## Build binary tree using postorder and inorder traversal arrays

The approach is the same as above, except we iterate from the back of the postorder array as that is where the root is present.

## Return inorder traversal array without using recursion

Use a stack to store the nodes as we traverse the array.
```
while (node is not None or len(stack) != 0):
    if node is not None:
        stack.append(node)
        node = node.left
    else:
        node = stack.pop()
        ans.append(node.value)
        node = node.right
```

## Return postorder traversal array without using recursion

What changes in this case, is where you append the values of the node.

```
while (node is not None or len(stack) != 0):
    if node is not None:
        stack.append(node)
        ans.append(node.value)
        node = node.left
    else:
        node = stack.pop()
        node = node.right
```

## Print the left view of a tree

Print the first element of each level. Approach is similar to the one where we return the list of lists of each level.

## Print the right view of a tree

Just like the above, but we are printing the last element of each level.

## Print the top view of a tree

Use the vertical order traversal and print the first element of the list generated there. You dont need to append any value to the list where the key is already present.

## Print the bottom view of a tree

Edge case of 2 values in the same level and the same distance away from the root.

## Print the boundary of a tree

Take care of the edge case where some nodes will be repeated.

## Find the LCA of two nodes n1, n2

Approach 1:
```
def lca(root, n1, n2):
    if root is None:
        return None
    if root == n1 or root == n2:
        return root
    found_n1 = find(root.left, n1)
    found_n2 = find(root.left, n2)

    if (found_n1 and found_n2):
        return lca(root.left, n1, n2)
    if (found_n1 or found_n2):
        return root
    else:
        return lca(root.right, n1, n2)
```
TC: O(N^2) - Every iteration we make a call to find() which has a TC of O(N)
SC: O(N)

Approach 2:
```
def lca(root, n1, n2):
    if root is None:
        return None
    
    if root == n1 or root == n2:
        return root
    
    l_lca = lca(root.left, n1, n2)
    r_lca = lca(root.right, n1, n2)

    if (l_lca is not None) and (r_lca is not None):
        return root
    elif l_lca is None:
        return r_lca
    else:
        return l_lca
```
TC: O(N)
SC: O(N)

This approach works only when two nodes are present in the tree.

## Given a BT, find the diameter of the tree

Diameter is the longest path between two node in a tree.

Approach 1:
```
def diameter(root):
    if root is None:
        return -1
    lh = height(root.left)
    rh = height(root.right)
    ld = diameter(root.left)
    rd = diameter(root.right)

    return max(ld, rd, (lh+rh+2))
```
TC: O(N^2)
SC: O(N)

Approach 2:
```
from collections import namedtuple
TreeInfo = namedtuple('TreeInfo', 'height diameter max_diameter')
def diameter(root):
    if root is None:
        return TreeInfo(-1, 0, 0)

    left = diameter(root.left)
    right = diameter(root.right)

    h = max(left.height, right.height) + 1
    d = (left.height+right.height + 2)
    max_d = max(d, left.diameter, right.diameter)
    return TreeInfo(h, d, max_d)
```
TC: O(N)
SC: O(N)

## Given a BT, check whether it s height balanced

Approach 1:
```
def is_balanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if abs(lh-rh) > 1:
        return False
    
    return is_balanced(root.left) and is_balanced(root.right)
```
TC: O(N^2)
SC: O(N)

Approach 2:
```
from collections import namedtuple

TreeInfo = namedtuple('TreeInfo', 'is_bal height')
def is_balanced(root):
    if root is None:
        return TreeInfo(True, -1)
    left = is_balanced(root.left)
    right = is_balanced(root.right)

    is_bal = left.is_bal and right.is_bal and (abs(left.height-right.height) <= 1)
    h = max(left.height, right.height) + 1
    return TreeInfo(is_bal, h)
```
TC: O(N)
SC: O(N)

## Morris Inorder Traversal of a tree

Traversal of a tree without using extra space
```
while curr_node is not None:
    if curr_node.left is None:
        print(curr_node.val)
        curr_node = curr_node.right
    else:
        temp = curr_node.left
        while (temp.right is not None and temp.right is not curr_node):
            temp = temp.right
        if temp.right is None:
            temp.right = curr_node
            curr_node = curr_node.left
        else:
            temp.right = None
            print(curr_node.val)
            curr_node = curr_node.right
```
if we cannot modify the structure of a tree, then there is no way to traverse a tree without using extra space.

TC: O(N) - Every node is visited atmost 3 times
SC: O(1)

How can we implement Pre and post order traversal using this approach

## A binary has nodes that has a next pointer along with left and right pointer. Initially they are pointing to Null. Populate them by pointing them to the node on the right side.

Use level order traversal
```
level = root
while level is not None:
    curr = level
    while curr is not None:
        if curr.left is not None:
            if curr.right is not None:
                curr.left.next = curr.right
            else:
                curr.left.next = get_next_right(curr)

        if curr.right is no None:
            curr.right.next = get_next_right(curr)
    
    if level.left is not None:
        level = level.left
    elif level.right is not None:
        level = level.right
    else:
        level = get_next_right(level)
    #while True:
    #    if level.left is not None:
    #        level = level.left
    #        break
    #    elif level.right is not None:
    #        level = level.right
    #        break
    #    elif level.next is not None:
    #        level = level.next
    #    else:
    #        level = None
    #        break

def get_next_right(root):
    if root is None:
        return None
    temp = root.next
    while temp is not None:
        if temp.left is not None:
            return temp.left
        elif temp.right is not None:
            return temp.right
        else:
            temp = temp.next
    return None

```
TC: O(N)
SC: O(1)

## Given a complete binary tree, count the number of nodes in it

Complete binary tree - All the levels are completely filled, except the last level. If last level not completely filled, they must be left alligned


