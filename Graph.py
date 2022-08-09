# NeetCode Challenge
# Solving Problems from NeetCode website, Graph

We use BFS & DFS for solving Graph related problems.

BFS uses Queue                                                                            DFS uses stack
BFS is iterative                                                                          DFS is recursive
Queue follows FIFO (First In First Out)                                                   Stack follows LIFO  (Last In First Out)


https://stackoverflow.com/questions/10974922/what-is-the-basic-difference-between-stack-and-queue   ---->  (picture)


#=============================================================================================================================================================================


Implementing BFS

graph = {
    'A':['B' , 'C'],
    'B':['A','C'],
    'C':['B'],
    'D':['A','E','F'],
    'E':['D','E','G'],
    'F':['D','E','H'],
    'G':['E','H'],
    'H':['G','F']
        }

visited = []
queue = []

def bfs(visited , queue , node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s , end=' --> ')



        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

bfs(visited, queue, 'E')


output: E --> D --> G --> A --> F --> H --> B --> C

> > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

Implementing DFS


graph = {
    'A':['B' , 'C'],
    'B':['A','C'],
    'C':['B'],
    'D':['A','E','F'],
    'E':['D','E','G'],
    'F':['D','E','H'],
    'G':['E','H'],
    'H':['G','F']
        }

visited= set()

def dfs(visited , graph , node):

    if node not in visited:
        print(node, end= ' --> ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')

Output: A --> B --> C


#=============================================================================================================================================================================

1. Number of Islands

# iterate through the grid to find the blocks of '1' we have

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

class Solution:
    def dfs(self, grid, r, c):
        rows , cols = len(grid) , len(grid[0])      # define our row & column
        grid[r][c] = '0'    #  mark our current index az Zero
        direction = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]      # for each position we make DFS check (horizontally or vertically):     left     right     down     up
        for row, col in direction:
            if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == '1':# check for not being out of bounds & make sure the next position also be island
                self.dfs(grid, row, col)


    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        for r in range(len(grid)):          # iterate through each row
            for c in range(len(grid[r])):       # iterate through each column
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)        # we trigger our DFS function to explore all connected island
                    islands += 1
        return islands


Output: 3
#=============================================================================================================================================================================

2.  Clone Graph
# for this question we use hashmap & and DFS. Basically, we map the old Node to the New node. Every time we clone a node, take a look at the neighbor.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}       # create a hashmap & nested in another function

        def dfs(node):
            if node in oldToNew:        # if the node is in the hashmap, means we already clone it and return that clone
                return oldToNew[node]

            copy = Node(node.val)       # The 'copy' is a new node that we just cloned. if the node is not in the hashmap, we create the copy
            oldToNew[node] = copy           # in the hashmap set new node(copy) as value for the old node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None


#=============================================================================================================================================================================
