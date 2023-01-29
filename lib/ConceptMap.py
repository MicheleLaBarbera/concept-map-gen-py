import networkx as nx
import random
import matplotlib.pyplot as plt
import math 

class ConceptMap:
  def __init__(self):
    self.graph = nx.null_graph()
    self.adjacency_matrix = None
    self.entropy = 0

  def generate(self, node_min: int, node_max: int) -> bool:
    if node_min > node_max: # Check if minimum nodes is above than its maximum
      return False

    nodes_count = random.randint(node_min, node_max) # Generate a number between the minimum and the maximum of nodes count

    # Generate a directed acyclic graph (DAG) with 2/3 probability to have the default generated edges direction reversed
    self.graph = nx.gn_graph(nodes_count) if random.randint(0, 2) == 2 else nx.gn_graph(nodes_count).reverse()

    # Convert the generated directed acyclic graph (DAG) to an adjacency matrix
    self.adjacency_matrix = nx.adjacency_matrix(self.graph).todense()

    # Entropy calculation
    self.entropy = self.calculate_entropy()
    return True

  def draw(self):
    if nx.is_empty(self.graph) == False: # Draw only if graph isn't empty
      nx.draw(self.graph)
      plt.show()

  def get_adjacency_matrix(self):
    return self.adjacency_matrix

  def get_nodes_count(self) -> int:
    return self.graph.number_of_nodes()

  def get_edges_count(self) -> int:
    return self.graph.number_of_edges()

  def get_entropy(self) -> int:
    return self.entropy

  def calculate_entropy(self) -> int:
    for x in self.adjacency_matrix:
      links_count = 0 
      for y in x: # Check for every node how many links it has
        if y == 1:
          links_count = links_count + 1
      
      node_entropy = 0
      if links_count > 0:
        probability = 1 / links_count 
        for _ in range(links_count):
          node_entropy = node_entropy + abs((probability * math.log(probability, 2))) # Entropy formula

      self.entropy = self.entropy + node_entropy
