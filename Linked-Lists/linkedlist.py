'''
    Gabby Ortman - I totally know what I'm doing
'''

class Node(object): 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class SinglyLinedList(object): 
    def __init__(self): 
        self.head = None 
        self.size = 0 
        #points to Node 
        self.cursor = None 


    def size(self): 
        return self.size 

    def next(self):  
        if self.cursor is None: 
            raise Exception
        else: 
            ret_node = self.cursor.data 
            self.cursor. self.cursor.next 
            return ret_node 


    def add_node(self, data): 
        '''
            add node to beginning of the list 
        '''
        #empty list
        if self.head is None: 
            self.head = Node(data) 
            self.cursor = self.head 
        else: 
            node = Node(data)  
            node.next = self.head 
            self.cursor = node 
            self.head = node 

        self.size += 1

    def delete_node(self, data): 
        pass 