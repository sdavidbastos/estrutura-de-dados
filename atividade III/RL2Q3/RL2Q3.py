ROOT = "root"
file = open('L2Q3.in', 'r').readlines()


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.predecessor = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    result = ""
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
            
    def handle(self, node):
        height = self.height_node(node)
        self.result = f"{self.result} {node.data} ({height})"
    
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        self.handle(node)
    
        if node.right:
            self.inorder_traversal(node.right)
    
    def height_node(self, node):
        height = -1
        while node != None:
            node = node.predecessor
            height += 1
        return height

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = -1
        hright = -1
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1


class BinarySearchTree(BinaryTree):

    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right

        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
            parent.left.predecessor = parent
        else:
            parent.right = Node(value)
            parent.right.predecessor = parent

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node

        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node

    def remove(self, value, node=ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return node

        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node == self.root and self.root.left is None and self.root.right is None:
                self.root = None
                return 
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.min(node.right).data
                node.data = substitute
                node.right = self.remove(substitute, node.right)
        return node

    def __repr__(self):
        return self.result

    def __str__(self):
        return self.__repr__()


class RL2Q3():
    def __init__(self):
        self.process_file()
        self.create_tree_list()
        self.create_file()

    def process_file(self):
        length = len(file)
        self.processed_data = [None]*length
        for i in range(length):
            current_line = file[i].strip().split(" ")
            line_array = [None] * int(len(current_line)/2)
            for j in range(0, len(current_line), 2):
                line_array[j//2] = [current_line[j], eval(current_line[j+1])]
            self.processed_data[i] = line_array

    def handle_operation(self, bst: BinarySearchTree, data):
        ADD = 'a'
        REMOVE = 'r'

        simbol = data[0]
        value = data[1]

        if simbol == ADD:
            bst.insert(value)

        if simbol == REMOVE:
            node = bst.search(value)
            if node == None:
                bst.insert(value)
            else:
                bst.remove(value)

    def create_tree_list(self):
        current_list = self.processed_data
        length = len(current_list)
        self.list_tree = [None]*length

        for i in range(length):
            bst = BinarySearchTree()
            line_length = len(current_list[i])
            for j in range(line_length):
                current_value = current_list[i][j]
                self.handle_operation(bst, current_value)
            self.list_tree[i] = bst

    def create_file(self):
        response = open('L2Q3.out', 'w')
        array = self.list_tree
        for i in range(len(array)):
            array[i].inorder_traversal()
            response.write(array[i].__str__().strip())
            if(i < len(array)-1):
                response.write("\n")
        response.close()


response = RL2Q3()
# response.list_tree[1].inorder_traversal()
# print(response.list_tree[1])
