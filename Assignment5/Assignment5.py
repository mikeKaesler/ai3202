#Mike Kaesler
#Assignment 5

import sys

import numpy

world = sys.argv[1] #reading in the world text file from c-lline
epsilon = sys.argv[2] #reading in epsilon value fron c-line
gamma = 0.9 #decay value at .9

#retrieving world, then making it into graph nodes

def get_world(world):
	f = open(world, "r")
	world_list = []
	line = f.readline()
	while line != " ":
		world_list.append(line.split())
		line = f.readline()
	for i in range(0, len(world_list)):
		for j in range(0, len(world_list[i]):
			world_list[i][j] = Graph_Node(i, j, int world_list[i][j])
	return world_list
	
#making graph nodes for the world matrix
# input: x and y location, and the value at that location
# turns that value into utility and reward for the MDP 

class Graph_node(object):
	def __init__(self, x, y, value):
		self.x = x
		self.y = y
		self.value = value
		
		if (value == 0): #open square, reward 0
			self.reward = 0
		
		elif (value == 1): #mountain, reward = -1
			self.reward = -1
		
		elif (value == 2): #wall, cant pass through wall's at all
			self.reward = None
		
		elif (value == 3): #snakes, reward = -2
			self.reward = -2
		
		elif (value == 4): #barn, reward  = +1
			self.reward = 1
			
		elif (value == 50): #the end goal, win once reaching here
			self.reward = 50
			
	
			
class MDP(object):
	def __init__(self, world_list, epsilon, gamma):
		self.world = world_list #recieving world 
		self.epsilon = epsilon #getting epsilon from command line
		self.gamma = gamma #getting gamma from predefined (0.9)
	
	#returns a specific node, but note no restrictions here, so must 
	#add those at later time 
	def get_position(self, x, y):
		return world_list[x][y]
	
	#getting the utility at a specific node, also note, no restrictions 
	#on unviable nodes, again must implement at later date
	def get_utility(self, x, y):
		return world_list[x][y].reward
	
	def calc_utility(x, y, world_list):
		current = world_list[x][y]
		node_value = world_list[x][y].get_utility
		
		#make a list of all expected utilities (up, down, left, right)
		exp_utilities = []
		
		if (x - 1) < 0:
			left_utility = 0
		else:
			left_utility = get_utility(x - 1,y)
		
		if (x + 1) >= len(world_list):
			right_utility = 0
		else:
			right_utility = get_utility(x+1,y)
			
		if (y - 1) < 0:
			down_utility = 0
		else:
			down_utility = get_utility(x, y-1)
		
		if (y + 1) >= len(world_list[x]):
			up_utility = 0
		else:
			up_utility = get_utility(x, y + 1)
			
		#now add those to the list
		move_up = ((0.8*up_utility + 0.1*right_utility + 0.1*left_utility), up)
		exp_utilities.append(move_up)
		move_down = ((0.8*down_utility + 0.1*right_utility + 0.1*left_utility, down)
		exp_utilities.append(move_down)
		move_right = ((0.8*move_right + 0.1*move_up + 0.1*move_down, right)
		exp_utilities.append(move_right)
		move_left = ((0.8*move_left + 0.1*move_up + 0.1*move_down, left
		exp_utilties.append(move_left)
		
		current_utility = get_utility(x,y)
		
			
		
		
		
		
		
	
	
	
	 
	
		
			
		
		
	
