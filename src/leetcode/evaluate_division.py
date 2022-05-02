'''
evaluate division
https://leetcode.com/problems/evaluate-division/

You are given an array of variable pairs equations and an array of real numbers values,
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query
where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not
result in division by zero and that there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
'''

from typing import List


class Solution:

  @staticmethod
  def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    '''DFS is faster than BFS in this case'''

    # build the equations graph like { dividend: { divisor: value } }
    graph = {}
    for i in range(len(equations)):
      a, b = equations[i]
      val = values[i]
      rVal = 1 / val
      if a in graph:
        graph[a][b] = val
      else:
        graph[a] = {b: val}
      if b in graph:
        graph[b][a] = rVal
      else:
        graph[b] = {a: rVal}

    # DFS search
    def _dfs(source, target, value, visited) -> float:
      if target in graph[source]:
        return graph[source][target] * value

      visited.append(source)

      for k in [k for k in graph[source] if k not in visited]:
        val = _dfs(k, target, graph[source][k] * value, visited)
        if val is not None:
          return val

    results = []
    for a, b in queries:
      if a not in graph or b not in graph:
        results.append(float(-1))
      else:
        if a == b:
          res = 1
        else:
          res = _dfs(a, b, 1, [])
        results.append(res if res is not None else -1)

    return results

  @staticmethod
  def calcEquationBFS(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

    # build the equations graph like { dividend: { divisor: value } }
    graph = {}
    for i in range(len(equations)):
      a, b = equations[i]
      val = values[i]
      rVal = 1 / val
      if a in graph:
        graph[a][b] = val
      else:
        graph[a] = {b: val}
      if b in graph:
        graph[b][a] = rVal
      else:
        graph[b] = {a: rVal}

    # breadth first search
    def _bfs(source, target) -> float:
      # start search from 1, so can quick return if dividend & divisor are the same
      queue = [[source, 1]]
      visited = set()

      while queue:
        node, val = queue.pop(0)
        if node == target:
          return val
        if node in visited:
          continue
        visited.add(node)

        for g in graph[node]:
          if g not in visited:
            # for 1st time: (a, 1) -> a/b -> 1 * (a/b)
            # for 2nd time: a/b * b/c -> a/c
            queue.append([g, val * graph[node][g]])

      return float(-1)

    results = []
    for a, b in queries:
      if a not in graph or b not in graph:
        results.append(float(-1))
      else:
        res = _bfs(a, b)
        results.append(res)

    return results
