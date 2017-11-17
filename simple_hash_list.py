#!/usr/bin/python

import hashlib


class ListNode:
    def __init__(self, name):
        self.list = []    
        self.name = name
   
    def __str__(self):
        return str(map(str, self.list))
 
    def __repr__(self):
        return str(self)    

    def __len__(self):
        return len(self.list)

    def _hash(self, s):
        return hashlib.sha256(s).hexdigest()

    def append(self, msg):
        if len(self) == 0:
            p = ""
        else:
            p = self._hash(str(self.list[-1]))
        n = Node(msg, p)
        self.list.append(n)


class Node:
    def __init__(self, msg, prev):
        self.msg = str(msg) 
        self.prev = prev
      
    def __str__(self):
        return "(%s, %s)" % (self.msg, self.prev)
