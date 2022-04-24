# Binary Search Tree

For all nodes, all elements on the left side of the root are smaller than the root value and all elements on the right side of the root are larger than the root value.

When two nodes have equal values, we can place them on the left or the right side of the root, with the caveat that, the same rule should be followed for the entire tree.
```
       Some examples of BST                           This is not a binary tree because 8 is 
                                                                 to the left of 10

    2              1               1                                    10         
   / \                              \                                  /  \
  1   3                              2                                5    12
                                      \                              /     / \ 
                                       4                            4     8   14
                                        \
                                         6

```
