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
            
  lets_test_this_breakpoint_thing()
  
def test_breadth_first_traversal():
  graph = Graph()
  
  pandora = graph.add_vertex('Pandora')
  arendelle = graph.add_vertex('Arendelle')
  metroville = graph.add_vertex('Metroville')
  monstroplolis = graph.add_vertex('Monstroplolis')
  narnia = graph.add_vertex('Narnia')
  naboo = graph.add_vertex('Naboo')
  graph.add_edge(pandora, arendelle)
  # graph.add_edge(arendelle, pandora)
  graph.add_edge(arendelle, metroville)
  # graph.add_edge(metroville, arendelle)
  graph.add_edge(arendelle, monstroplolis)
  # graph.add_edge(monstroplolis, arendelle)
  # graph.add_edge(metroville, monstroplolis)
  graph.add_edge(monstroplolis, metroville)
  graph.add_edge(metroville, narnia)
  # graph.add_edge(narnia, metroville)
  graph.add_edge(metroville, naboo)
  # graph.add_edge(naboo,metroville)
  graph.add_edge(monstroplolis, naboo)
  # graph.add_edge(naboo, monstroplolis)
  graph.add_edge(naboo, narnia)
  # graph.add_edge(narnia, naboo)

  babies = graph.traverse(pandora)
  # breakpoint()
  assert babies == ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Naboo', 'Narnia']
  

  
  
  
  
  