class Linked_List:

    class __Node:

        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.next = None
            self.previous = None
            self.val = val

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.previous = self.__header
        self.__size = 0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        new = Linked_List.__Node(val)
        # Make sure you connect the node before tail to the new tail node using .next
        before = self.__trailer.previous
        before.next = new
        new.previous = before
        self.__trailer.previous = new
        new.next = self.__trailer
        self.__size = self.__size + 1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        if index < 0 or index > self.__size-1:
            raise IndexError
        elif self.__header.next is self.__trailer:
            raise IndexError
        elif index == self.__size:
            self.append_element(val)
        else:
            newest = Linked_List.__Node(val)
            current = self.__header
            for i in range(0, index):
                current = current.next
            newest.next = current.next
            newest.next.previous = newest
            current.next = newest
            newest.previous = current
            self.__size = self.__size + 1

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
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
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index > self.__size-1 or index < 0:
            raise IndexError
        if self.__header.next is self.__trailer:
            raise IndexError
        current = self.__header.next
        for i in range(self.__size):
            if i == index:
                return current.val
            current = current.next

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__size != 1:
            new_header = self.__header.next.next
            new_trailer = self.__header.next
            new_trailer.previous = self.__trailer.previous
            second_to_last_node = self.__trailer.previous
            second_to_last_node.next = new_trailer
            self.__trailer.previous = new_trailer
            new_trailer.next = self.__trailer
            self.__header.next = new_header

    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
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

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__index = 0
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__index >= self.__size:
            raise StopIteration
        result = self.get_element_at(self.__index)
        self.__index = self.__index + 1
        return result

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        new_list = Linked_List()
        current = self.__trailer.previous
        for i in range(self.__size):
            new_list.append_element(current.val)
            current = current.previous
        return new_list
