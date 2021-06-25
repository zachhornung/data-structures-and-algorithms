import random
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l''m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class HashTable:
  def __init__(self, size=1024):
    self._buckets = [[] for _ in range(size)]

  def add(self, key, value):
    hash_index = self.hash(key)
    if not self._buckets[hash_index]:
      self._buckets[hash_index].append((key, value))
      return
    
    for i in range(len(self._buckets[hash_index])):
      if self._buckets[hash_index][i][0] == key:
        self._buckets[hash_index][i][1] = value
        return

    self._buckets[hash_index].append((key, value))
      

  def get(self, key):
    hash_index = self.hash(key)
    if key in self._buckets[hash_index][0]:
      return self._buckets[hash_index][0][1]
    
    for i in range(len(self._buckets[hash_index])):
      if self._buckets[hash_index][i][0] == key:
        return self._buckets[hash_index][i][1]
    

  def hash(self, key):
    num = 0
    for char in key:
      num += ord(char)
    num *= 599
    return num % len(self._buckets)
  
  def contains(self, key):
    hash_index = self.hash(key)
    if self._buckets[hash_index][0]:
      return True
    
    i=0
    while self._buckets[hash_index][i]:
      if self._buckets[hash_index][i][0] == key:
        return True
      i += 1
      
    return False
    
  def find_collision_key(self, key):
    collision_key = ''
    
    while (self.hash(collision_key) != self.hash(key)) and not (collision_key == key):
      for letter in alphabet:
        collision_key += letter
        collision_index = self.hash(collision_key)
        if collision_index == self.hash(key):
          print('hey look i found a collision! ',collision_key)
          return collision_key
        collision_key = collision_key[:-1]
      collision_key += random.choice(alphabet)
  
      