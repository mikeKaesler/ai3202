#Mike Kaesler
#Assignment 6
import networkx as nx
import matplotlib.pyplot as plt
import getopt
import sys


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
#starting with storing the conditional probabilities, hard coding first, and then
#changing to the getopt input

Bayes.node["Pollution"]["P(P=L)"] = 0.9   #might be able to put the input thing where the float value is here
Bayes.node["Pollution"]["P(P=H)"] = 1 - Bayes.node["Pollution"]["P(P=L)"]

Bayes.node["Smoker"]["P(S=T)"] = 0.3
Bayes.node["Smoker"]["P(S=F)"] = 1 - Bayes.node["Smoker"]["P(S=T)"]

Bayes.node["Cancer"]["P(C=T|P=H, S=T)"] = 0.05 #and these might not change
Bayes.node["Cancer"]["P(C=T|P=H, S=F)"] = 0.02
Bayes.node["Cancer"]["P(C=T|P=L, S=T)"] = 0.03
Bayes.node["Cancer"]["P(C=T|P=L, S=F)"] = 0.001

Bayes.node["XRay"]["P(X=T|C=T"] = 0.9
Bayes.node["XRay"]["P(X=T|C=F"] = 0.2

Bayes.node["Dyspnoea"]["P(D=T|C=T"] = 0.65
Bayes.node["Dyspnoea"]["P(D=T|C=F"] = 0.3

print Bayes.nodes()
#do functions below

x = Bayes.node["Dyspnoea"]["P(D=T|C=T"] *2
print x

def setPrior(a, f):
	#set prior, add to bayes net

def calcMarginal(a):
	#calc marginal probability

def calcConditional(a, n):
	#calc conditional


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)
    for o, a in opts:
		if o in ("-p"):
			print "flag", o
			print "args", a
			print a[0]
			print float(a[1:])
			#setting the prior here works if the Bayes net is already built
			#setPrior(a[0], float(a[1:])
		elif o in ("-m"):
			print "flag", o
			print "args", a
			print type(a)
			#calcMarginal(a)
		elif o in ("-g"):
			print "flag", o
			print "args", a
			print type(a)
			'''you may want to parse a here and pass the left of |
			and right of | as arguments to calcConditional
			'''
			p = a.find("|")
			print a[:p]
			print a[p+1:]
			#calcConditional(a[:p], a[p+1:])
		elif o in ("-j"):
			print "flag", o
			print "args", a
		else:
			assert False, "unhandled option"
		
    # ...

if __name__ == "__main__":
    main()


	









