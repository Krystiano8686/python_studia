from typing import Any

class Node:
    value: Any
    next: 'Node'
    def __init__(self, val: Any, val_next: 'Node'):
      self.value = val
      self.next = val_next
 
class LinkedList:
    head: Node
    tail: Node
    def __init__(self) -> None:
      self.head = None
      self.tail = None
    
    def push(self, val: Any) -> None:
      newNode = Node(val, self.head)
      self.head = newNode
      if self.tail == None:
         self.tail = self.head 
    
    def append(self, val: Any) -> None:
        newNode = Node(val, None)
        self.tail.next = newNode 
        self.tail = newNode
        
        if self.head == None:
            self.tail = self.head    
   
    def node(self, at: int) -> Node:
     i = 0
     newObj = self.head
     while i < at:
       if newObj == None:
         return None
       newObj = newObj.next
       i+=1
     return newObj

    def insert(self, value: Any, after: Node) -> None:
      helpObj = self.head
      while helpObj != after:        
        helpObj = helpObj.next

      newNode = Node(value, helpObj.next)
      if helpObj.next == None: 
        self.tail = Node(value, None)    
      helpObj.next = newNode

    def pop(self) -> Node:
      Obj = self.head 
      self.head = self.head.next
      return Obj.value

    def remove_last(self) -> Node:
      if self.head == None:
        return None
      helpObj = self.head

      while helpObj.next.next != None:
        helpObj = helpObj.next
    
      helpObj2 = helpObj.next  
      self.tail = helpObj
      helpObj.next = None

      return helpObj2.value

    def remove(self, after: Node) -> Node:
      if (self.head == None):
        return None

      helpObj = self.head
    
      while helpObj != after: 
        helpObj = helpObj.next

      helpObj2 = helpObj 
      helpObj.next = None
      self.tail = helpObj2

    def __str__(self):
      helpObj = self.head
      string = ''
      while helpObj != None:
        string += (str(f'{helpObj.value} -> '))   
        helpObj = helpObj.next
        
      string = string.strip(' ->') 
      return str(string)

    def __len__(self):
      helpObj = self.head
      i = 0
      while helpObj != None:
        helpObj = helpObj.next
        i+=1

      return i

class Stack:

  _storage: LinkedList
      
  def __init__(self):
        self._storage = LinkedList()


  def push(self, element: Any) -> None:
    self._storage.push(element)

  def pop(self) -> None:
    return self._storage.pop()

  def __str__(self): 
      helpObj = self._storage.head
      string = ''
      while helpObj != None:
        string += (str(f'{helpObj.value}\n' ))   
        helpObj = helpObj.next
        
      string = string.strip(' \n') 
      return str(string)


  def __len__(self):
    return len(self._storage) 


list_ = LinkedList()
assert list_.head == None

list_.push(1)
list_.push(0)
print('Nasza lista ma 2 elementy (ponieważ je dodajemy za pomocą metody push na początek listy): ' ,list_)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

print('Nasza lista ma 4 elementy (ponieważ dodaliśmy 2 na jej koniec za pomocą metody append): ' ,list_)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

print('Nasza lista ma 5 elementów (ponieważ za pomocą metody node byliśmy w stanie znaleźć dany węzeł a metodą insert wstawić go za wskazane wcześniej miejsce): ' ,list_)


assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()

print('Nasza lista ma 4 elementy (ponieważ za pomocą metody pop usuneliśmy pierwszy element): ' ,list_)


assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

print('Nasza lista ma 3 elementy (ponieważ za pomocą metody remove_last usuneliśmy ostatni element): ' ,list_)


assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

print('Nasza lista ma 2 elementy (ponieważ za pomocą metody remove usuneliśmy następny element po tym co wybrała metoda node)')


assert str(list_) == '1 -> 5'

print(list_)
print('Dlugosc listy wynosi: ',len(list_))

stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)


assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2

print(stack)

pass