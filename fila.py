class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, element):
        node = Node(element)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    def pop(self):
        if self._size:
            element = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return element

        raise IndexError("The queu is empty")

    def peek(self):
        if self._size:
            element = self.first.data
            return element
        raise IndexError("The queu is empty")

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
        return "Empty queue"

    def __str__(self):
        return self.__repr__()

fila = Queue()
fila.push(5)
fila.push("David")
fila.push(True)
fila.push(None)
fila.pop()
print(fila)