import random


class AnimalShelter:
  def __init__(self, cats, dogs):
    self.cats = cats
    self.cat_names = ['fuzzy', 'lazy', 'cuddly', 'maui', 'kitty', 'kitty kat', 'another cat', 'so many cats']
    self.dogs = dogs
    self.dog_names = ['peter', 'doug', 'douglas', 'kyle', 'zach', 'river', 'cedar', 'tree', 'banana', 'baby goat']
    
    
  def enqueue(self, animal):
    if animal == 'cat':
      self.cats.enqueue(random.choice(self.cat_names))
      
    if animal == 'dog':
      self.dogs.enqueue(random.choice(self.dog_names))
      
  def dequeue(self, pref=None):
    if pref == 'dog':
      return self.dogs.dequeue()
    
    if pref == 'cat':
      return self.cats.dequeue()
    else:
      return 






class Queue:
  """This class is a queue
  """
  def __init__(self, front=None):
    self.front = front
    self.back = None
    
  def enqueue(self, value=None):
    if self.front is None:
      self.front = self.back = Node(value)
    else:
      self.back.next = Node(value)
    
  def dequeue(self):
    if self.front is None:
      return 'this queue is empty buddy'
    ret = self.front.value
    self.front = self.front.next
    return ret
    
  def peek(self):
    if self.front is not None:
      return self.front.value
    return 'this queue is empty buddy'
  
class Node:
  def __init__(self, value, next_=None):
    self.value = value
    self.next = next_
    