import networkx as nx
import random
import matplotlib.pyplot as plt

class ConceptMap:
  def __init__(self):
    self.graph = nx.null_graph()
    self.adjacency_matrix = None

  def generate(self, node_min: int, node_max: int) -> bool:
    if node_min > node_max: # Check if minimum nodes is above than its maximum
      return False

    nodes_count = random.randint(node_min, node_max) # Generate a number between the minimum and the maximum of nodes count

    # Generate a directed acyclic graph (DAG) with 2/3 probability to have the default generated edges direction reversed
    self.graph = nx.gn_graph(nodes_count) if random.randint(0, 2) == 2 else nx.gn_graph(nodes_count).reverse()

    # Convert the generated directed acyclic graph (DAG) to an adjacency matrix
    self.adjacency_matrix = nx.adjacency_matrix(self.graph).todense()
    return True

  def draw(self):
    if nx.is_empty(self.graph) == False: # Draw only if graph isn't empty
      nx.draw(self.graph)
      plt.show()

  def get_adjacency_matrix(self):
    return self.adjacency_matrix



    
