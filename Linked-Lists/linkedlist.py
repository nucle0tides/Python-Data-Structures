'''
    Gabby Ortman - I totally know what I'm doing
'''

class Node(object): 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
        self.previous = None

class SinglyLinkedList(object): 
    def __init__(self): 
        self.head = None 
        self.size = 0 
        self.cursor = None 

    def size(self): 
        return self.size 

    def next(self):  
        if self.cursor is None: 
            raise Exception
        else: 
            ret_node = self.cursor
            self.cursor. self.cursor.next 
            return ret_node 


    def add_node(self, data): 
        if self.head is None: 
            self.head = Node(data) 
            self.cursor = self.head 
        else: 
            node = Node(data)  
            node.next = self.head 
            self.head = node 

        self.size += 1

    def delete_node(self, data):  
        pass

    def contains(self, to_find):
        if self.head is not None: 
            curr = self.head 
            while curr is not None: 
                if curr.data is to_find: 
                    return True
                curr = curr.next 
        return False

class DoublyLinkedList(SinglyLinkedList): 
    def __init__(self):
        pass 

if __name__ == '__main__': 
    test_list = SinglyLinkedList()
    test_list.add_node(1)
    test_list.add_node(2)
    test_list.add_node(3)