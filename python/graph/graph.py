from stacks_and_queues.stacks_and_queues import Node ,Queue
from collections import deque

class Vertex:
  def __init__(self, value):
    self.value = value
    
  
class Graph:
  def __init__(self) -> None:
      self.adjacency_list = {}
      
    
  def add_vertex(self,value):
    new_vertex = Vertex(value)
    self.adjacency_list[new_vertex] = {}
    return new_vertex
  
  def add_edge(self, start_node, end_node, weight=0):
    self.adjacency_list[start_node][end_node] = weight
  
  def get_vertexes(self):
    return self.adjacency_list
  
  def get_neighbors(self, vertex):
    return self.adjacency_list[vertex]
  
  def size(self):
    return len(self.adjacency_list)
  
  def traverse(self, node, debug=False):
    queue = Queue()
    ret_baby = []
    if not node:
      return 'babies'
    visited = {}
    queue.enqueue(node)
    while queue.peek():
      current = queue.dequeue()
      visited[current] = True
      if current == 'this queue is empty buddy':
        break
      for baby_node in self.adjacency_list[current]:
        if baby_node == None:
          break
        if not baby_node in visited:
          queue.enqueue(baby_node)
      ret_baby.append(current.value)
      if debug:
        breakpoint()
    return ret_baby
      
    