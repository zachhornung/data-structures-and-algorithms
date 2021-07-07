from graph.graph import Graph, Vertex
from graph_depth_first_traversal.graph_depth_first_traversal import depth_first_pre_order

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
  assert goats in graph._adjacency_list[babies]
  assert graph._adjacency_list[babies][goats] == 10
  
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
          assert graph._adjacency_list[animal1][animal2] == 'double food for you guys'
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
  graph.add_edge(arendelle, metroville)
  graph.add_edge(arendelle, monstroplolis)
  graph.add_edge(monstroplolis, metroville)
  graph.add_edge(metroville, narnia)
  graph.add_edge(metroville, naboo)
  graph.add_edge(monstroplolis, naboo)
  graph.add_edge(naboo, narnia)

  babies = graph.traverse(pandora)
  
  assert babies == ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Naboo', 'Narnia']
  

def test_city_path_finder():
  def business_trip(graph, arr_cities):
    if not graph._adjacency_list:
      return False, 0

    cost = 0
    for i,city in enumerate(arr_cities):
      neighbors = graph.get_neighbors(city)
      if i+1 >=len(arr_cities): # if we're at the end of the list
        return True, cost
      if arr_cities[i+1] in neighbors:
        cost += neighbors.get(arr_cities[i+1])
        continue
      return False, 0
  
  graph = Graph('bidirectional')
  
  pandora = graph.add_vertex('Pandora')
  arendelle = graph.add_vertex('Arendelle')
  metroville = graph.add_vertex('Metroville')
  monstroplolis = graph.add_vertex('Monstroplolis')
  narnia = graph.add_vertex('Narnia')
  naboo = graph.add_vertex('Naboo')

  cities1 = [metroville, pandora]
  cities2 = [arendelle, monstroplolis, naboo]
  cities3 = [naboo, pandora]
  cities4 = [narnia, arendelle, naboo]
  test_cases = [cities1, cities2, cities3, cities4]
  expected_results = [(True, 82), (True, 115), (False, 0), (False, 0)]

  graph.add_edge(pandora, arendelle, 150)
  graph.add_edge(pandora, metroville, 82)
  graph.add_edge(arendelle, metroville, 99)
  graph.add_edge(arendelle, monstroplolis, 42)
  graph.add_edge(metroville, monstroplolis, 105)
  graph.add_edge(metroville, narnia, 37)
  graph.add_edge(metroville, naboo, 26)
  graph.add_edge(naboo, narnia, 250)
  graph.add_edge(monstroplolis, naboo, 73)
  
  for i,test in enumerate(test_cases):
    assert business_trip(graph, test) == expected_results[i]
    
def test_depth_first_traversal():
  
  graph = Graph()
  nodes = {node:graph.add_vertex(node) for node in ['a','b','c','d','e','f','g','h']}

  graph.add_edge(nodes['a'], nodes['b'])
  graph.add_edge(nodes['a'], nodes['d'])
  graph.add_edge(nodes['b'], nodes['c'])
  graph.add_edge(nodes['b'], nodes['d'])
  graph.add_edge(nodes['c'], nodes['g'])
  graph.add_edge(nodes['d'], nodes['e'])
  graph.add_edge(nodes['d'], nodes['h'])
  graph.add_edge(nodes['a'], nodes['f'])
  
  
  assert [node.value for node in depth_first_pre_order(list(graph._adjacency_list.keys())[0],graph)] == ['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']
  
def test_babies():
  assert 'babies'
  
  
  
  
  
  
  