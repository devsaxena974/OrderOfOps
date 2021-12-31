class Linked_List:

    class __Node:

        def __init__(self, value):
            self.next = None
            self.previous = None
            self.value = value

    def __init__(self):
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.previous = self.__header
        self.__size = 0

    def __len__(self):
        return self.__size

    def append_element(self, val):
        new_node = Linked_List.__Node(val)
        before = self.__trailer.previous
        before.next = new_node
        new_node.previous = before
        new_node.next = self.__trailer
        self.__trailer.previous = new_node
        self.__size += 1

    def insert_element_at(self, val, index):
        if index < 0 or index > self.__size-1:
            raise IndexError
        elif self.__header.next is self.__trailer:
            raise IndexError
        elif index == self.__size:
            self.append_element(val)
        else:
            new_node = Linked_List.__Node(val)
            current = self.__header
            for i in range(0, index):
                current = current.next
            new_node.next = current.next
            new_node.next.previous = new_node
            current.next = new_node
            new_node.previous = current
            self.__size = self.__size + 1

    def remove_element_at(self, index):
        if index > self.__size-1 or index < 0:
            raise IndexError
        if self.__header.next is self.__trailer:
            raise IndexError
        else:
            current = self.__header.next
            for i in range(index):
                current = current.next
            removed_value = current.val
            current.next.previous = current.previous
            current.previous.next = current.next
        self.__size = self.__size - 1
        return removed_value

    def get_element_at(self, index):
        if index > self.__size-1 or index < 0:
            raise IndexError
        if self.__header.next is self.__trailer:
            raise IndexError
        current = self.__header.next
        for i in range(self.__size):
            if i == index:
                return current.val
            current = current.next

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= self.__size:
            raise StopIteration
        result = self.get_element_at(self.__index)
        self.__index = self.__index + 1
        return result

    def __str__(self):
        result = "" + "[ "
        current = self.__header.next
        for i in range(self.__size):
            result += str(current.val)
            if i == self.__size-1:
                result += " "
            else:
                result += ", "
            current = current.next
        result += "]"
        return result
