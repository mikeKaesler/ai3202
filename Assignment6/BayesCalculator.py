#Mike Kaesler
#Assignment 6
import networkx as nx
import matplotlib.pyplot as plt


#create node class
# only takes the conditional probabilities as an argument and holds them
'''class Node(object):
	def __init__(self, conditional):
		self.conditional = conditional'''
#trying without class for node, as networkX can attribute attributes to nodes


#create bayes net as graph using networkx (directed graph)
#then create all 5 nodes 
Bayes = nx.DiGraph()
Bayes.add_node("Pollution")
Bayes.add_node("Smoker")
Bayes.add_node("Cancer")
Bayes.add_node("XRay")
Bayes.add_node("Dyspnoea")

#create edges in graph according to handout we were given
Bayes.add_edges_from([("Pollution", "Cancer"), ("Smoker", "Cancer"), 
						("Cancer", "XRay"), ("Cancer", "Dyspnoea")])

#testing changing a node's attribute,
# WORKS
'''Bayes.node["Pollution"]["P(P=L)"] = 0.9
print Bayes.node["Pollution"]'''


#testing to see if graph is drawn correctly (without probabilities) 
#WORKS						
'''nx.draw(Bayes)
plt.show()'''

#DEFINE STARTING PROBABILITIES BELOW, THEN FUNCTIONS TO CALCULATE, THEN GETOPT






