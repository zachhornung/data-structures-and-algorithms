def depth_first_pre_order(first_vertex,graph,debug=False):
  if debug:
    breakpoint()
  visited = {}
  collection = []
  def walk(start_vertex):
    nonlocal visited, collection, graph
    if start_vertex is None:
      return
    if start_vertex not in visited:
      collection.append(start_vertex)
      visited[start_vertex] = True
    if graph._adjacency_list.get(start_vertex):
      for end_vertex in graph._adjacency_list.get(start_vertex):
        walk(end_vertex)
  walk(first_vertex)
  
  return collection