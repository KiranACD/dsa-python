# Trees

### Hierarchical data structure

Arrays, linked-lists are linear data structures. Trees bring hierarchy into the picture. All the nodes are connected one single node. This single node is like the oldest living member in your family, like your grandfather or grandmother or your great-grandmother. The nodes just below are children of this single node. This single node is called the root node.  

### Root Node

Root node has no parent. They only have children. Root node is a parent node that has no parent. 

Just like your root node can have no parent, a node that can have no children is called the leaf node.

### Leaf Node

Leaf nodes are the ending nodes of a tree as they have no children. 

Leaf node has no children

### Parent Nodes and Children Nodes

Traversal in the tree structure is always from parent to child. We cannot go from a child node to the parent node. 

For a given single node, the nodes that are directly connected to this single node and are reachable are its children nodes. The single node itself will then be their parent node.

### Edges

The connection between two nodes is an edge. 

If a tree has N nodes, how many edges are there? 

Irrespective of the number of children a node has, each node will have only 1 parent. There is only one exception to this, the root node. The root node has no parent. Hence there are N-1 edges. 

### Height of a node

Distance from the node to the farthest reachable leaf node. The distance can be measured as the number of edges between the node and the farthest reachable leaf node. A leaf node has a height of 0.

Depending on the person, the height of a node can also be the number nodes between it and the farthest reachable node.

Height of a NULL node is -1.

### Depth of a node

This is the distance from the root to the node in question. The distance be measured as the number of edges between the root and the node.

### Height of a binary tree

Height of a binary tree is the height of the root node, which is the distance from the root node to the farthest reachable leaf node.

### Structure of a Node

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

### Tree Traversals

The convention is that the left child will be visited before the right node. 

How many ways to traverse a tree? 3 - PreOrder, InOrder, PostOrder

1. PreOrder

Visit root, left, right
```
def preorder(root):
    if root is None:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)
```
This is a depth first search. This algorithm can be used in an application that requires a fail fast approach. For e.g., Given 2 trees, check if they are identical. If the root value does not match, then we can return False. PreOrder helps us here as we check the root node first and then traverse to the sub trees. If the root nodes dont match, we reach our answer faster.

TC : O(N)
SC : O(N) - Order of height of the tree, because we use the recursion stack. In the worst case scenario, all the nodes will be on one side of the tree.

2. InOrder
    - Visit left, root, right

3. PostOrder

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

Postorder is handy when we need to use data from the left and right side of a node. For e.g., given a tree, return its height. 
```
def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1
```





