from Linked_List import Linked_List


class Deque():

    def __init__(self):
        self.__list = Linked_List()

    def __str__(self):
        return str(self.__list)

    def __len__(self):
        return len(self.__list)
