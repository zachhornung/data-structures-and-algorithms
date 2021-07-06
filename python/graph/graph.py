from stacks_and_queues.stacks_and_queues import Node ,Queue
from collections import deque

class Graph:
    def __init__(self,kind='single direction'):
        self._adjacency_list = {}
        self.type = kind


    def add_vertex(self, value):
        v = Vertex(value)
        if v not in self._adjacency_list:
          self._adjacency_list[v] = {}
          return v

    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not found in graph")

        if start_vertex not in self._adjacency_list:
          self.add_node(start_vertex)

        self._adjacency_list[start_vertex][end_vertex] = weight

        if self.type == 'bidirectional':
          self._adjacency_list[end_vertex][start_vertex] = weight


    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex)
      
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
        for baby_node in self._adjacency_list[current]:
          if baby_node == None:
            break
          if not baby_node in visited:
            queue.enqueue(baby_node)
        ret_baby.append(current.value)
        if debug:
          breakpoint()
      return ret_baby
    
    


class Vertex:
    def __init__(self, value):
        self.value = value
  

      
    