# NeetCode Challenge
# Solving Problems from NeetCode website, Graph

We use BFS & DFS for solving Graph related problems.

BFS uses Queue                                                                            DFS uses stack
BFS is iterative                                                                          DFS is recursive
Queue follows FIFO (First In First Out)                                                   Stack follows LIFO  (Last In First Out)


https://stackoverflow.com/questions/10974922/what-is-the-basic-difference-between-stack-and-queue   ---->  (picture)



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

ROWS, COLS = len(grid)
