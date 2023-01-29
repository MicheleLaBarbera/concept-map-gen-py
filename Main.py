import json
import os 

from lib.ConceptMap import ConceptMap
from lib.Input import Input as inp
from lib.NumpyArrayEncoder import NumpyArrayEncoder

class Main:
  DIRECTORY_OUTPUT_PATH = 'output_maps/'
  MIN_MAPS_COUNT_ALLOWED = 1
  MIN_NODE_COUNT_ALLOWED = 1

  def __init__(self):
    self.maps = []
    self.adjacency_matrix_list = []

    if not os.path.exists(self.DIRECTORY_OUTPUT_PATH): # Create output directory if not exists
      os.makedirs(self.DIRECTORY_OUTPUT_PATH)

  def start(self):
    # Input from the user
    maps_count = inp.ask_integer("Quante mappe vuoi generare?", self.MIN_MAPS_COUNT_ALLOWED)
    node_min = inp.ask_integer("Inserire il numero minimo di nodi da generare:", self.MIN_NODE_COUNT_ALLOWED)
    node_max = inp.ask_integer("Inserire il numero massimo di nodi da generare:", node_min)

    # Generate 'n' concept maps
    for _ in range(maps_count):
      map = ConceptMap() # Create ConceptMap object
      map.generate(node_min, node_max) # Generate a random directed acyclic graph (DAG) with given parameters
      
      map.draw() # Draw on screen the generated directed acyclic graph (DAG)
      print(map.get_adjacency_matrix()) # Just for debug purposes

      self.maps.append(map) # Append the generated map in a maps list
      self.adjacency_matrix_list.append(map.get_adjacency_matrix()) # Append the adjacency matrix of the generated map in a adjacency matrix list

    # Save the generated output of adjacency matrix list to an arbitrary JSON file
    file_name = input("Inserire il nome del file dove si desidera salvare l'output generato: ")
    with open(self.DIRECTORY_OUTPUT_PATH + file_name + ".json", "w") as write_file:
      json.dump(self.adjacency_matrix_list, write_file, cls=NumpyArrayEncoder) # To read them just use json.load() and numpy.asarray()

Main().start()