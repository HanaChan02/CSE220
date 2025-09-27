class GraphMatrix:
  def __init__(self, size):
    self.size = size
    self.matrix = [[0]*size for _ in range(size)]
    self.directed = False

  def add_edge(self, x, y, weight=1):
    self.matrix[x][y] = weight
    if not self.directed:
      self.matrix[y][x] = weight

  def get_degree(self, v):
    in_degree = 0
    out_degree = 0
    for i in range(self.size):
      if self.matrix[v][i] != 0:
        out_degree += 1
      if self.matrix[i][v] != 0:
        in_degree += 1
    return in_degree + out_degree

  def get_out_degree(self, v):
    degree = 0
    for i in range(self.size):
      if self.matrix[v][i] != 0:
        degree += 1
    return degree

  def get_weight_sum(self, v):
    total = 0
    for i in range(self.size):
      total += self.matrix[v][i]
      if self.directed:
        total += self.matrix[i][v]
    return total

  def get_out_weight_sum(self, v):
    total = 0
    for i in range(self.size):
      total += self.matrix[v][i]
    return total

  def to_undirected(self):
    und_graph = GraphMatrix(self.size)
    und_graph.directed = False
    for i in range(self.size):
      for j in range(self.size):
        if self.matrix[i][j] != 0:
          und_graph.add_edge(i, j, self.matrix[i][j])
    return und_graph

class GraphList:
  def __init__(self, size):
    self.size = size
    self.adj_list = [[] for _ in range(size)]
    self.directed = False

  def add_edge(self, u, v, weight=1):
    self.adj_list[u] = self.adj_list[u] + [(v, weight)]
    if not self.directed:
      self.adj_list[v] = self.adj_list[v] + [(u, weight)]

  def get_degree(self, v):
    in_degree = 0
    out_degree = len(self.adj_list[v])
    if self.directed:
      for u in range(self.size):
        for neighbor, _ in self.adj_list[u]:
          if neighbor == v:
              in_degree += 1
    return in_degree + out_degree

  def get_out_degree(self, v):
    return len(self.adj_list[v])

  def get_weight_sum(self, v):
    total = 0
    for n, w in self.adj_list[v]:
      total += w
    if self.directed:
      for u in range(self.size):
        for n, w in self.adj_list[u]:
          if n == v:
              total += w
    return total

  def get_out_weight_sum(self, v):
    total = 0
    for n, w in self.adj_list[v]:
      total += w
    return total

  def to_undirected(self):
    und_graph = GraphList(self.size)
    und_graph.directed = False
    for u in range(self.size):
      for v, weight in self.adj_list[u]:
        exists = False
        for neighbor, _ in und_graph.adj_list[u]:
          if neighbor == v:
            exists = True
            break
        if not exists:
          und_graph.add_edge(u, v, weight)
    return und_graph

matrix_graph = GraphMatrix(7)
list_graph = GraphList(7)

edges = [
    (0, 1, 2), (0, 2, 3), (0, 3, 4),
    (1, 2, 1), (1, 4, 4), (1, 5, 5),
    (2, 3, 2), (2, 5, 5), (2, 6, 6),
    (3, 6, 1), (4, 5, 3), (5, 6, 7),
    (1, 0, 2), (2, 0, 3), (3, 0, 4),
    (4, 1, 4), (6, 2, 6)
]

for u, v, w in edges:
  matrix_graph.add_edge(u, v, w)
  list_graph.add_edge(u, v, w)

# Test cases
print("Matrix Graph:")
print("Degree of vertex 2:", matrix_graph.get_degree(2))  # Expected: 5
print("Out weight sum of vertex 2:", matrix_graph.get_out_weight_sum(2))  # Expected: 12

print("\nList Graph:")
print("Degree of vertex 2:", list_graph.get_degree(2))  # Expected: 5
print("Out weight sum of vertex 2:", list_graph.get_out_weight_sum(2))  # Expected: 12

  # Create directed version
directed_matrix = GraphMatrix(7)
directed_matrix.directed = True
directed_list = GraphList(7)
directed_list.directed = True
directed_edges = edges[:11]  # First 11 original edges
for u, v, w in directed_edges:
    directed_matrix.add_edge(u, v, w)
    directed_list.add_edge(u, v, w)

#TASK-1
def max_degree_matrix(graph):
  maxD = -1
  for v in range(graph.size):
    d = graph.get_degree(v)
    if d > maxD:
      maxD = d
  return maxD

def max_degree_list(graph):
  maxD = -1
  for v in range(graph.size):
    d = graph.get_degree(v)
    if d > maxD:
      maxD = d
  return maxD

  # Test Task 1
print("\nTask 1 - Max Degree:")
print("Matrix:", max_degree_matrix(matrix_graph))  # Expected: 5 (vertex 2)
print("List:", max_degree_list(list_graph))       # Expected: 5
