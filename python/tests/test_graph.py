from graph.graph import Graph, Vertex

def test_imports():
  assert Graph and Vertex
  
def test_graph_can_be_instantiated():
  assert Graph()
  
def test_can_add_vertex_to_graph():
  graph = Graph()
  babies = graph.add_vertex('babies')
  assert babies.value == 'babies'
  
def test_can_add_multiple_vertexes():
  graph = Graph()
  babies = graph.add_vertex('babies')
  goats = graph.add_vertex('goats')
  assert goats.value == 'goats'
  assert babies.value == 'babies'

def test_can_get_size_of_graph():
  graph = Graph()
  babies = graph.add_vertex('babies')
  goats = graph.add_vertex('goats')
  assert graph.size() == 2
  
def test_can_add_edge():
  graph = Graph()
  babies = graph.add_vertex('babies')
  goats = graph.add_vertex('goats')
  graph.add_edge(babies, goats, 10)
  assert goats in graph.adjacency_list[babies]
  assert graph.adjacency_list[babies][goats] == 10
  
def test_get_neighbors():
  graph = Graph()
  babies = graph.add_vertex('babies')
  goats = graph.add_vertex('goats')
  graph.add_edge(babies, goats, 10)
  neighbors = graph.get_neighbors(babies)
  assert goats in neighbors
  
def test_insert_lots_of_things_added():
  def lets_test_this_breakpoint_thing(debug=False):
    graph = Graph()
    farm_animals = ['goats', 'chickens', 'cows', 'pigs', 'more cows', 'zebra', 'lions', 'more pigs', 'spiders', 'more goats', 'more chickens']
    barnyard = [graph.add_vertex(animal) for animal in farm_animals]
    [graph.add_edge(animal1, animal2, 'double food for you guys') for animal1 in barnyard for animal2 in barnyard if animal1.value in animal2.value[1:]]
    for animal1 in barnyard:
      for animal2 in barnyard:
        if animal1.value in animal2.value[1:]:
          n1, n2 = animal1.value, animal2.value
          assert graph.adjacency_list[animal1][animal2] == 'double food for you guys'
          print(n1,n2)
          if debug:
            breakpoint()
            
  lets_test_this_breakpoint_thing(debug=False)
  

  
  
  
  
  