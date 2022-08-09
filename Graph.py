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

# iterate through the grid to finds the blocks of '1' we have

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