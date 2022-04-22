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

- Approach 2
Append Nonetype object to the queue each time we pop out a Nonetype object. When a Nonetype object is popped, start a new list.

TC: O(N)
SC: O(width of the tree)



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



