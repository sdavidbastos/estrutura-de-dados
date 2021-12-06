ROOT = "root"
file = open('L2Q2.in', 'r').readlines()

class NodeSum:
    def __init__(self, node=None, summation=0):
        self.node = node
        self.summation = summation
    
    def __repr__(self):
        return f"{self.node} ({self.summation})"
    
    def __str__(self):
        return self.__repr__()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.predecessor = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None, node=None):
        self.response = []
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
        
    def postorder_traversal_sum(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal_sum(node.left)
        if node.right:
            self.postorder_traversal_sum(node.right)
        print(node)
        
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        current_summation_left = self.postorder_sum(node.left)
        current_summation_right = self.postorder_sum(node.right)
        current_summation = current_summation_right - current_summation_left
        node_sum = NodeSum(node, current_summation)
        self.response.append(node_sum)
        if node.right:
            self.inorder_traversal(node.right)
            
    def postorder_sum(self, node):
        left = 0
        right = 0
        if node == None:
            return 0
        if node.left:
            left = left + self.postorder_sum(node.left)
        if node.right:
            right = right + self.postorder_sum(node.right)
        return left + right + node.data


class BinarySearchTree(BinaryTree):

    def insert(self, value):
        current_value = self.search(value)
        if current_value:
            return
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

    def __repr__(self):
        length=len(self.response)
        result = ""
        for i in range(length):
            result = f"{result} {self.response[i]}"
            
        return result

    def __str__(self):
        return self.__repr__()


class RL2Q2():
    def __init__(self):
        self.process_file()
        self.create_tree_list()
        self.create_file()

    def process_file(self):
        length = len(file)
        self.processed_data = [None]*length
        for i in range(length):
            current_line = file[i].strip().split(" ")
            line_length = len(current_line)
            for j in range(line_length):
                current_line[j] = eval(current_line[j])
            self.processed_data[i] = current_line

    def create_tree_list(self):
        current_list = self.processed_data
        length = len(current_list)
        self.list_tree = [None]*length

        for i in range(length):
            bst = BinarySearchTree()
            line_length = len(current_list[i])
            for j in range(line_length):
                current_value = current_list[i][j]
                bst.insert(current_value)
            self.list_tree[i] = bst
    def create_file(self):
        response = open('L2Q2.out', 'w')
        array = self.list_tree
        for i in range(len(array)):
            array[i].inorder_traversal()
            response.write(array[i].__str__().strip())
            if(i < len(array)-1):
                response.write("\n")
        response.close()
        
    
response = RL2Q2()