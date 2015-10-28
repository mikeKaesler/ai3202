#Mike Kaesler
#Assignment 6
import networkx as nx
import matplotlib.pyplot as plt
import getopt
import sys

#create bayes net as graph using networkx (directed graph)
#then create all 5 nodes 
Bayes = nx.DiGraph()
#global Bayes                           maybe not
Bayes.add_node("P")  #Pollution node
Bayes.add_node("S")  #Smoker node
Bayes.add_node("C")  #Cancer node
Bayes.add_node("X")  #Xray node
Bayes.add_node("D")  #Dyspnoa node

#create edges in graph according to handout we were given
Bayes.add_edges_from([("P", "C"), ("S", "C"), 
						("C", "X"), ("C", "D")])

#definging starting probablities below. Updated from last version,
#making names more intutitive, if statements will work the control from the cline in the functions 


#      NEED TO MAKE THESE SET AT THSE VALUES, UNLESS PRIORS RESET, NEED TO CHANGE HERE TOO
 
Bayes.node["P"]["p"] = .9 #prior probablity for pollution, LOW
Bayes.node["S"]["s"] = 0.3 #prior hard coded prob Smoker is TRUE




#probability priors are high or false
Bayes.node["P"]["~p"] = 1 - Bayes.node["P"]["p"] #prob pollution is HIGH
Bayes.node["S"]["~s"] = 1 - Bayes.node["S"]["s"] #prob somker is FALSE

#conditional probablities for having Cancer
Bayes.node["C"]["ps"] = 0.03 #pollution low, smoker true
Bayes.node["C"]["p~s"] = 0.001 #pollution low, smoker false
Bayes.node["C"]["~ps"] = 0.05 #pollution high, smoker true
Bayes.node["C"]["~p~s"] = 0.02 #pollution high, smoker false

Bayes.node["X"]["xc"] = 0.9 #xray is true given cancer is true
Bayes.node["X"]["x~c"] = 0.2 #xray is true given cancer is false

Bayes.node["D"]["dc"] = 0.65 #dys is true given cancer is true
Bayes.node["D"]["d~c"] = 0.3 #dis is true given cancer is false


#calculate priors
def setPrior(a, f):
	if (a == "P"):
		Bayes.node["P"]["p"] = f
		Bayes.node["P"]["~p"] = 1 - f
		print "probability pollution is low set at", Bayes.node["P"]["p"]
		
	elif (a == "S"):
		Bayes.node["S"]["s"] = f
		Bayes.node["S"]["~s"] = 1 - f
		print "probablility smoker is true is set at", Bayes.node["S"]["s"]
		 
	else:
		print "not valid argument"

#calculate marginal probabilities
def calcMarginal(a):
	if (a == "S"):
		marginal = Bayes.node["S"]["s"]
		return marginal
	if (a == "~s"):
		marginal = Bayes.node["S"]["~s"] #continue others in similar vein later, fixing local prior sets NOW, FIXED
		return marginal
	if (a == "P"):
		marginal = Bayes.node["P"]["p"]
		return marginal
	if (a == "~p"):
		marginal = Bayes.node["P"]["~p"]
		return marginal
	if (a == "C"):
		marginal = ((Bayes.node["C"]["ps"]*Bayes.node["S"]["s"] * Bayes.node["P"]["p"]) + (Bayes.node["C"]["p~s"]*Bayes.node["P"]["p"]*
		Bayes.node["S"]["~s"]) + (Bayes.node["C"]["~p~s"] * Bayes.node["P"]["~p"] * Bayes.node["S"]["~s"]) + (Bayes.node["C"]["~ps"] *
		Bayes.node["P"]["~p"]*Bayes.node["S"]["s"]))
		return marginal
	if (a == "~c"):
		marginal = 1 - calcMarginal("C") #honestly, this might not work how I think it works, but still going with it
		return marginal
	if (a == "X"):
		marginal = (Bayes.node["X"]["xc"]*calcMarginal("C")) + (Bayes.node["X"]["x~c"]* (1 - calcMarginal("C")))
		return marginal
	if (a == "~x"):
		marginal = 1 - calcMarginal("X")
		return marginal
	if (a == "D"):
		marginal = (Bayes.node["D"]["dc"]*calcMarginal("C")) + (Bayes.node["D"]["d~c"]*(1 - calcMarginal("C")))
		return marginal
	if (a == "~d"):
		marginal = 1 - calcMarginal("D")
	

#def calcConditional(a, n):
	#calc conditional
	#return 0
	

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
	except getopt.GetoptError as err:
		#print help info and exit
		print(err)
		sys.exit(2)
	for o, a in opts:
		if o in ("-p"):
			setPrior(a[0], float(a[1:]))
		elif o in ("-m"):
			marginal = calcMarginal(a)
			print(marginal)
		elif o in ("-g"):
			p = a.find("|")
			#do conditional shit
		elif o in ("-j"):
			return 
			#do joint shit
        #else:             for some reason, still triggers this else anyway, so dont mess up input
			#assert False, "unhandled option"
	
if __name__ == "__main__":
	main()
			
