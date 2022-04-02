from array import array
from ctypes import sizeof
from random import Random
import re
import string
from tokenize import Double
from typing import List, Tuple


class Vertex:
  def __init__(self) -> None:
    self.neighbours = array('i')
    self.color: int
    self.pff: int

  def add_neighbour(self, neighbour: int) -> None:
    self.neighbours.append(neighbour)

  def get_neighbours_list(self) -> List:
    return self.neighbours


class Graph:
  def __init__(self) -> None:
    self.graph: List[Vertex] = []

  def load_from_file(self, path: string) -> None:
    self.graph.clear()
    with open(path, mode='r') as f:
      for line in f.readlines():
        if line.split()[0] == 'p':
          arguments: List[str] = re.split(r' |\n', line)
          original_size: int = arguments[2]
          for i in range(0, (original_size * 2)):
            self.graph.append(Vertex())
          # print("length", len(graph))
        if line.split()[0] == 'e':
          arguments: List[str] = re.split(r' |\n', line)
          if arguments[1] != arguments[2]:
            # print("argument1", int(arguments[1]), "argument2", int(arguments[2]))
            self.graph[int(arguments[1]) -
                       1].add_neighbour(neighbour=int(arguments[2]))
            self.graph[int(
                arguments[1]) - 1].add_neighbour(neighbour=int(arguments[1] - 1 + original_size))
            self.graph[int(arguments[1] - 1 + original_size)
                       ].add_neighbour(neighbour=int(arguments[1]))
    # print("Vertex %i" % 0)
    # print("Neighbours", graph[0].get_neighbours_list(), "address", id(graph[0]))

  def _colorize_graph(self, color_amount: int) -> None:
    for element in self.graph:
      element.color = Random.randint(0, color_amount)

  def _evaluate_pff(self) -> None:
    for element in self.graph:
      for neighbour in element.neighbours:
        if element.color == self.graph[neighbour].color:
          element.pff = element.pff + 1

  def _evaluate_conflicts(self) -> int:
    count: int = 0
    for element in self.graph:
      count = count + element.pff
    return count * 0.5

  def _find_min_pff(self) -> int:
    min: int = self.graph.__len__
    for element in self.graph:
      if element.pff < min:
        min = element.pff
    return min

  def _find_max_pff(self) -> int:
    max: int = 0
    for element in self.graph:
      if element.pff > max:
        max = element.pff
    return max

  def _calculate_avg_pff(self) -> int:
    avg: int = 0
    for element in self.graph:
      avg = avg + element.pff
    return avg / self.graph.__len__
