#Mike Kaesler
#Assignment 5

import sys

import math

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
	for x in range(0, len(world_list)):
		for y in range(0, len(world_list[x])):
			world_list[x][y] = Graph_Node(x, y, int(world_list[x][y]))
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
			self.utility = 0
		elif (value == 1): #mountain, reward = -1
			self.reward = -1
			self.utility = -1
		elif (value == 2): #wall, cant pass through wall's at all
			self.reward = None
			self.utility = None
		elif (value == 3): #snakes, reward = -2
			self.reward = -2
			self.utility = -2
		elif (value == 4): #barn, reward  = +1
			self.reward = 1
			self.utility = 1
		elif (value == 50): #the end goal, win once reaching here
			self.reward = 50
			self.utility = 50
			
	
			
class MDP(object):
	def __init__(self, world_list, epsilon, gamma):
		self.world_list = world_list #recieving world 
		self.epsilon = float(epsilon) #getting epsilon from command line
		self.gamma = float(gamma) #getting gamma from predefined (0.9)
	
	#set class variables for success and failure
	pr_success = 0.8
	pr_failure = 0.1
	
	#returns a specific node, but note no restrictions here, so must 
	#add those at later time                CHANGED*********************
	def get_position(self, x, y):
		if (x < 0):
			return None
		elif (y <0):
			return None
		elif (x >= len(self.world_list)):
			return None
		elif (y >= len(self.world_list[0])):
			return None
		elif (self.world_list[x][y].value ==2):
			return None
		else:
			return world_list[x][y]
	
	#getting the utility at a specific node, also note, no restrictions 
	#on unviable nodes, again must implement at later date    CHANGED*******
	def get_utility(self, x, y):
		if (x <0):
			return -999999999
		elif (y < 0):
			return -999999999
		elif (x >= len(self.world_list)):
			return -999999999
		elif (y >= len(self.world_list[0])):
			return -999999999
		elif (self.world_list[x][y].value == 2):
			return -999999999
		else:	
			return world_list[x][y].utility
	
	def calc_utility(self):
		test_val = self.epsilon * (1-self.gamma)/self.gamma 
		delta = 100 #hard coded, not inputed
		#triple while loop, first keeps looping while delta is bigger than test
		# and the second two are to navigate x,y in the 2d array/graph  CHANGED

		while (delta >= test_val):
			delta = -100
			for x in range(0,len(self.world_list)):
				for y in range(0,len(self.world_list[0])):
					current = self.get_position(x,y)
					if (current != None and current.reward != 50): #finding adjacent if valid
						above_node = self.get_position(x, y +1)
						below_node = self.get_position(x, y-1)
						right_node = self.get_position(x+1, y)
						left_node = self.get_position(x-1,y)
						if (right_node == None):
							right_node = current
						if (left_node == None):
							left_node == current
						if (above_node == None):
							above_node == current
						if (below_node == None):
							below_node == current
						#add adjacent utilities to a list of "expected utilities"
						expected_utility = []
						
						up_val = pr_sucess*above_node + pr_failure*right_node + pr_failure*left_node
						expected_utility.append(up_val)
						
						down_val = pr_success*below_node + pr_failure*right_node + pr_failure*left_node
						expected_utility.append(down_val)
						
						right_val = pr_success*right_node + pr_failure*above_node + pr_failure*below_node
						expected_utility.append(right_val)
						
						left_val = pr_success*left_node + pr_failure*above_node + pr_failure*below_node
						expected_utility.append(left_val)
						
						#get current and max utility
						current_utility = current.utility
						max_utility = max(expected_utility)
						
						new.utility = current.reward + self.gamma * max_utility[0]
						
						if (abs(new.utility - current_utility) > delta):
							delta = abs(new.utility - current_utility)
							
	def get_path(self):
		self.calc_utility()
		#begin at bottom corner
		#setting current node at bottom corner
		current = self.get_position(len(self.world_list)-1,0)
		while not (current.reward == 50):
			print "At: ", current.x, current.y
			print "Utility: ", current.utility
			#adjacent nodes in list
			utilities = []
			above_node = self.get_utility(current.x, current.y + 1)
			utilities.append(above_node)
			below_node = self.get_utility(current.x, current.y - 1)
			utilities.append(below_node)
			right_node = self.get_utility(current.x + 1, current.y)
			utilities.append(right_node)
			left_node = self.get_utility(current.x - 1, current.y)
			utilities.append(left_node)
			
			#get the max of those
			max_utility = max(utilities)
			if (max_utility[0] == above_node):
				current = self.get_position(current.x, current.y +1)
			elif (max_utility[0] == below_node):
				current = self.get_position(current.x, current.y - 1)
			elif (max_utility[0] == right_node):
				current = self.get_position(current.x + 1, current.y)
			else:
				current = self.get_position(current.x - 1, current.y)
			
			
		#print final
		print "final node:", current.x, current.y
		print "final utility:", current.x, current.y
		
world1 = get_world(world)	
start = MDP(world, epsilon, 0.9)
start.get_path()
		
		
						
						
						
						 
						
					
					
		
		
			
		
		
		
		
		
	
	
	
	 
	
		
			
		
		
	
