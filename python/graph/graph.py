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
    