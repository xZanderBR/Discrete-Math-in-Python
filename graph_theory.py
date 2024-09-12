"""### Task 1.) Degree of a Node

Write a Python function `degree(adj_list: dict, node: str) -> int` that takes the following inputs:
*   `adj_list` := the adjacency list of a graph G
*   `node` := the node in the graph that you will calculate the degree of

The function `degree(adj_list, node)` will output the degree of `node` from the graph G's `adj_list`.

For example, suppose a graph G has the following adjacency list:

`0 -> ['1', '2', '3']`

`1 -> ['0', '2']`

`2 -> ['0', '1', '4']`

`3 -> ['0']`

`4 -> ['2']`

Then, `degree(G.adj_list, "1") = 2`, and `degree(G.adj_list, "3") = 1`.
"""

def degree(adj_list: dict, node: str) -> int:
  return len(adj_list[node])

"""### Task 2.) Number of Edges

Write a Python function `number_edges(adj_list: dict) -> int` that takes the following inputs:
*   `adj_list` := the adjacency list of a graph G

The function `number_edges(adj_list, node)` will output the number of edges contained in the graph G from the adjacency list `adj_list`

For example, suppose a graph G has the following adjacency list:

`0 -> ['1', '2', '3']`

`1 -> ['0', '2']`

`2 -> ['0', '1', '4']`

`3 -> ['0']`

`4 -> ['2']`

Then, `number_edges(G.adj_list) = 5`
"""

def number_edges(adj_list: dict) -> int:
  sum = 0
  for vertices in adj_list.values():
    sum += len(vertices)
  return int(sum / 2)

"""### Task 3.) Number of Nodes

Write a Python function `number_nodes(adj_list: dict) -> int` that takes the following inputs:
*   `adj_list` := the adjacency list of a graph G

The function `number_nodes(adj_list, node)` will output the number of nodes contained in the graph G from the adjacency list `adj_list`

For example, suppose a graph G has the following adjacency list:

`0 -> ['1', '2', '3']`

`1 -> ['0', '2']`

`2 -> ['0', '1', '4']`

`3 -> ['0']`

`4 -> ['2']`

Then, `number_nodes(G.adj_list) = 5`
"""

def number_nodes(adj_list: dict) -> int:
  return len(adj_list)

"""### Task 4.) Has Loop(s)

Write a Python function `has_loops(adj_list: dict) -> bool`
*   `adj_list` := the adjacency list of a graph G

The function `has_loops(adj_list)` will output `True` if the graph G's `adj_list` has a loop, and `False` otherwise


For example, suppose a graph G has the following adjacency list:

`0 -> ['0', '0', '1']`

`1 -> ['0', '2']`

`2 -> ['1']`

Then,

`has_loops(G.adj_list) = True`
"""

def has_loops(adj_list: dict) -> bool:
  for (node, vertices) in adj_list.items():
    if vertices.count(node) >= 2:
      return True
  return False

"""### Task 5.) Highest Degree Node

Write a Python function `highest_degree_node(adj_list: dict) -> tuple[str, int]` that takes the following inputs:
*   `adj_list` := the adjacency list of a graph G

The function `highest_degree_node(adj_list)` will output a tuple where the first component is the node of highest degree and the second component is the degree of that node.

In the case that there is a tie of more than one node, then the function will return one of the nodes with highest degree. It will not return all instances of nodes that reach that maximum degree.

For example, suppose a graph G has the following adjacency list:

`0 -> ['1', '2', '3']`

`1 -> ['0', '2']`

`2 -> ['0', '1', '4']`

`3 -> ['0']`

`4 -> ['2']`

Then,

`highest_degree_node(G.adj_list) = ("0", 3)`
"""

def highest_degree_node(adj_list: dict) -> tuple[str, int]:
  degree = 0
  key = ""
  for (node, vertices) in adj_list.items():
    if len(vertices) > degree:
      degree = len(vertices)
      key = node
  return (key, degree)

"""### Task 6.) Has Isolated Node(s)

Write a Python function `has_isolated_node(adj_list: dict) -> bool` that takes the following inputs:
*   `adj_list` := the adjacency list of a graph G

The function `has_isolated_node(adj_list)` will `True` if the graph G has at least one isolated node, and `False` otherwise.


For example, suppose a graph G has the following adjacency list:

`0 -> ['1', '2', '3']`

`1 -> ['0', '2']`

`2 -> ['0', '1', '4']`

`3 -> ['0']`

`4 -> ['2']`

Then,

`has_isolated_node(G.adj_list) = False`
"""

def has_isolated_node(adj_list: dict) -> bool:
  for vertices in adj_list.values():
    if len(vertices) == 2 and vertices[0] == vertices[1]:
      return True
    elif len(vertices) == 0:
      return True
  return False

"""### Task 7.) Has Multiple Edges

Write a Python function `has_multi_edges(adj_list: dict) -> bool`
*   `adj_list` := the adjacency list of a graph G

The function `has_multi_edges(adj_list)` will output `True` if the graph G's `adj_list` has multiple edges, and `False` otherwise


For example, suppose a graph G has the following adjacency list:

`0 -> ['1', '1']`

`1 -> ['0', '0', '3', '2']`

`2 -> ['1']`

`3 -> ['1']`

Then,

`has_multi_edges(G.adj_list) = True`
"""

def has_multi_edges(adj_list: dict) -> bool:
  for (node, vertices) in adj_list.items():
    if len(vertices) > 1:
      previous = vertices[0]
      for i in range(1, len(vertices)):
        if vertices[i] == previous and adj_list[vertices[i]].count(node) >= 1:
          return True
  return False

"""### Task 8.) Is Simple

Write a Python function `is_simple(adj_list: dict) -> bool`
*   `adj_list` := the adjacency list of a graph G

The function `is_simple(adj_list)` will output `True` if the graph G's `adj_list` represents a simple graph, and `False` otherwise


For example, suppose a graph G has the following adjacency list:

`0 -> ['1', '1']`

`1 -> ['0', '0', '3', '2']`

`2 -> ['1']`

`3 -> ['1']`

Then,

`is_simple(G.adj_list) = False`
"""

def is_simple(adj_list: dict) -> bool:
  for vertices in adj_list.values():
    if len(vertices) != len(set(vertices)):
      return False
  return True

"""### Task 9.) Is Connected

Write a Python function `is_connected(adj_list: dict) -> bool` that takes the following inputs:
*   `adj_list` := the adjacency list of a graph G

The function `is_connected(adj_list)` will output `True` if the graph G is connected, and `False` otherwise.

For example, suppose a graph G has the following adjacency list:

`0 -> ['1', '2', '3']`

`1 -> ['0', '2']`

`2 -> ['0', '1', '4']`

`3 -> ['0']`

`4 -> ['2']`

If one were to draw the corresponding graph G on paper, they would see that G is connected. Therefore,

`is_connected(G.adj_list) = True`

In order to complete this task you will need to use the given function `dfs_iter(adj_list: dict, v: str) -> list` INSIDE your `is_connected(adj_list)` function.  

`dfs_iter(adj_list, v)` completes a Depth-First Search on a graph G's adjacency list starting at node `v`. It will return the Depth-First Search traversal as a list.

For example,

`dfs_iter(G.adj_list, "0") = [0, 3, 2, 4, 1]`.
"""

def dfs_iter(adj_list: list, v: str):
  visited = set((v,))
  output = [v]
  stack = [v]

  while stack:
    node = stack.pop()
    if node not in visited:
      output.append(node)
      visited.add(node)
    for neighbor in adj_list[node]:
          if neighbor not in visited:
              stack.append(neighbor)
  return output

def is_connected(adj_list: dict) -> bool:
  for vertices in adj_list.values():
    for vertice in vertices:
      if vertice not in dfs_iter(adj_list, "0"):
        return False
  return True

"""### Task 10.) Is Minimally Connected

Write a Python function `is_minimally_connected(adj_list: dict) -> bool` that takes the following inputs:
*   `adj_list` := the adjacency list of a graph G

The function `is_minimally_connected(adj_list)` will output `True` if the graph G is minimally connected, and `False` otherwise.

For example, suppose a graph G has the following adjacency list:

`0 -> ['1', '2', '3']`

`1 -> ['0', '2']`

`2 -> ['0', '1', '4']`

`3 -> ['0']`

`4 -> ['2']`

If one were to draw the corresponding graph G on paper, they would see that G is not minimally connected. Therefore,

`is_minimally_connected(G.adj_list) = False`

In order to complete this task you will need to use your previously written function `is_connected(adj_list)`.
"""

def is_minimally_connected(adj_list: dict) -> bool:
  if is_connected(adj_list):
    return number_edges(adj_list) == number_nodes(adj_list) - 1
  else:
    return False
