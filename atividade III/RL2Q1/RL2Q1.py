ROOT = "root"
file = open('L2Q1.in', 'r').readlines()


class NodeQueue:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        node = NodeQueue(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    def pop(self):
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next

            if self.first is None:
                self.last = None
            self._size = self._size - 1
            return elem
        raise IndexError("The queue is empty")

    def peek(self):
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"

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
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

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

    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if(node.left):
                queue.push(node.left)
            if(node.right):
                queue.push(node.right)
            print(node, end=" ")


class BinarySearchTree(BinaryTree):

    heights = "0"

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
            self.height_node(parent.left)
        else:
            parent.right = Node(value)
            parent.right.predecessor = parent
            self.height_node(parent.right)

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

    def height_node(self, node):
        height = -1
        while node != None:
            node = node.predecessor
            height+= 1
        self.heights = f"{self.heights} {height}"
    
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
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)
        return node

    def __repr__(self):
        return f"{self.heights} max {self.max()} alt {self.height()} pred {self.max().predecessor} "

    def __str__(self):
        return self.__repr__()


class RL2Q1():
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
        response = open('L2Q1.out', 'w')
        array = self.list_tree
        for i in range(len(array)):
            response.write(array[i].__str__().strip())
            if(i < len(array)-1):
                response.write("\n")
        response.close()
        
        


RL2Q1()