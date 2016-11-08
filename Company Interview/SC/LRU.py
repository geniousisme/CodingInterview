from collections import OrderedDict

class Node(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class DoublyLinkedList(object):
    def __init__(self):
        self.tail = None
        self.head = None

    def is_empty(self):
        return not self.tail

    def remove_last(self):
        self.remove(self.tail)
        return

    def remove(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        if self.head == node:
            node.next.prev = None
            self.head = node.next
            return

        if self.tail == node:
            node.prev.next = None
            self.tail = node.prev
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        return

    def add_first(self, node):
        if not self.head:
            self.head = self.tail = node
            node.prev = node.next = None
            return

        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None

class LRUCache(object):
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.curr_len = 0
        self.dict = {}
        self.cache = DoublyLinkedList()

    def get(self, key):
        if not self.dict.get(key):
            return -1
        else:
            val = self.dict[key].val
            self.cache.remove(self.dict[key])
            self.cache.add_first(self.dict[key])
            return val
            
    def set(set, key, value):
        if self.dict.get(key):
            self.cache.remove(self.dict[key])
            self.cache.add_first(self.dict[key])
            self.dict[key].val = value
        else:
            node = Node(key, value)
            self.dict[key] = node
            self.cache.add_first(node)
            self.curr_len += 1
            if self.curr_len > self.capacity:
                self.curr_len -= 1
                del self.cache[self.cache.tail.key]
                self.cache.remove_last()


class LRUCache1(object):
    '''
    Implement with OrderedDict
    '''
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = OrderedDict()
        self.curr_len = 0
        

    def get(self, key):
        """
        :rtype: int
        """
        try:
            val = self.dict[key]
            del self.dict[key]
            self.dict[key] = val
            return val

        except KeyError:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        try:
            del self.dict[key]
            self.dict[key] = value

        except KeyError:
            if self.curr_len == self.capacity:
                self.dict.popitem(last=False)
                self.curr_len -= 1
            self.dict[key] = value
            self.curr_len += 1

