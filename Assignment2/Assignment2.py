from Manhattan import *
from Other import *
import sys
import numpy as np
from math import sqrt 
from itertools import product 

world = sys.argv[1]
heuristic_cline = sys.argv[2]

'''#testing the heuristic idea 
if heuristic_cline == "Manhattan.py":
	print "Works"
elif heuristic_cline == "Other.py":
	print "Works"

# that does work, so dont need seperate files for heuristics'''


# turn text file into 2d integer matrix
with open(world) as file:
	world_matrix = np.array([[int(i) for i in line.split()] for line in file], np.int32)

# testing that it worked
'''print world_matrix 
print world_matrix[1,1] #access the *2,*2 unit because indexed at zero'''

# build node object, using inheritance to get the x,y coords
class Node(object):
	def __init__(self):
		self.g = 0 #distance to start
		self.h = 0 # heuristic
		self.parent = None
	def movement_cost(self, other, value):
		raise NotImplementedError
		
class GridNode(Node):
	def __init__(self, x, y, value):
		self.x = x
		self.y = y
		self.value = value
		super(GridNode, self).__init__()
	def movement_cost(self, other, value):
		diagonal = abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1
		if diagonal == 1 and value == 0:
			retVal = 14
		elif diagonal == 1 and value == 1:
			retVal = 24
		elif diagonal == 0 and value == 0:
			retVal = 10
		elif diagonal == 0 and value == 1:
			retVal = 20
		else: ## instead of just not going to the wall nodes, making them an
			retVal = 200000000 ## 'infinite' value so that they just wont be chosen regardless
		return retVal
## so far above code gives no SYNTAX errors



class Astar(object):
	def __init__(self, graph):
		self.graph = graph
	
	def heuristic(self, node, start, end):
		raise NotImplementedError
		
	def search(self, start, end):
		openSet = set()
		closedSet = set()
		current = start
		openset.add(current)
		while openset:
			current = min(openset, key = lambda o:o.g + o.h)
			if current == end:
				path = []
				while current.parent:
					path.append(current)
					current = current.parent
				path.append(current)
				return path[::-1]
			openSet.remove(current)
			closedSet.add(current)
			for node in self.graph[current]:
				if node in closedSet:
					continue
				if node in openSet:
					new_g = current.g + current.movement_cost(node)
					if node.g > new_g:
						node.g = new_g
						node.parent = current
				else:
					node.g = current.g + current.movement_cost(node)
					node.h = self.heuristic(node, start, end)
					node.parent = current
					openset.add(node)
		return None 

if heuristic_cline == "Manhattan.py":
	class Astar_Heur(Astar):
		def heuristic(self, node, start, end):
			return 10*(abs(end.x - node.x) + abs(end.y - node.y))
elif heuristic_cline == "Other.py": ## just doing a straight line distance
	class Astar_Heur(Astar):
		def heuristic(self, node, start, end):
			return sqrt((end.x - node.x)**2 + (end.y - node.y))
else:
	print "An invalid heuristic option was given"

def build_graph(matrix):
	width = len(matrix)
	height = len(matrix[0])
	graph = {}
	for x in range(0, width):
		for y in range(0, height):
			newNode = GridNode(x, y, matrix[x][y])
			graph[newNode] = []
			for i,j in product([-1,0,1], [-1,0,1]):
				if not (0 <= x + i < width):
					continue
				if not (0 <= y + j < height):
					continue
				graph[newNode[x][y]].append(newNode[x+i][y+j])
	return graph, newNode
				
graph, newNode = build_graph(world_matrix)
paths = Astar_Heur(graph)
start, end = newNode[9,0] , newNode[0,9]
path = paths.search(start, end)

print path
	
		

		
		
 
	

