class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class ConstructBinaryTree:

    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)
        self.root = None
    
    def insert_node(self, i):

        if i >= self.length:
            return None
        
        if self.arr[i] is None:
            return None
        new_node = Node(self.arr[i])
        new_node.left = self.insert_node((2*i)+1)
        new_node.right = self.insert_node((2*i)+2)

        return new_node
    
    def start(self):
        i = 0
        new_node = Node(self.arr[i])
        new_node.left = self.insert_node((2*i)+1)
        new_node.right = self.insert_node((2*i)+2)
        self.root = new_node
    
    def print_tree(self, node):

        if node is None:
            return

        self.print_tree(node.left)
        print(node.val)
        self.print_tree(node.right)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]

    make_tree = ConstructBinaryTree(arr)
    make_tree.start()
    make_tree.print_tree(make_tree.root)
    # print(make_tree.root.right.val)
        

