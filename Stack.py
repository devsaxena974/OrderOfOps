from Deque import Deque


class Stack:
    def __init__(self):
        self.__deque = Deque()

    def __str__(self):
        return str(self.__deque)

    def __len__(self):
        return len(self.__deque)

    def push(self, val):
        return self.__deque.push_front(val)

    def pop(self):
        return self.__deque.pop_front()

    def peek(self):
        return self.__deque.peek_front()
