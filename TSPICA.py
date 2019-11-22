from pulp import *

# name the problem
problemName = 'transportationProblem'

# define the problem as min
prob = LpProblem(problemName, LpMinimize)

# the costs of shipping from every supply location to every customer
costs = {
			'WareHouse'	:   {'Node1'		: 45,	'Node2' : 70,   'Node3' : 10,  'Node4' : 10},
            'Node1'		:   {'Warehouse' 	: 45,	'Node2' : 12,   'Node3' : 10,  'Node4' : 10},
            'Node2'    	:   {'Warehouse' 	: 45,	'Node1' : 12,   'Node3' : 10,  'Node4' : 10},
            'Node3'    	:	{'Warehouse' 	: 45,	'Node1' : 12,   'Node2' : 10,  'Node4' : 10},
			'Node4'    	:	{'Warehouse' 	: 45,	'Node1' : 12,   'Node2' : 10,  'Node3' : 10},
		}

# supply limitations
supplyAmounts = {
					'Townsville' 	:   5000,
                    'Pendleton' 	:   8000,
                    'Anderson'  	:   6500,
                    'Pickens'   	:   9500
                }

# demand minimums
demandAmounts = {   'Pumpkintown'   :   3000,
                    'Asheville'     :   2500,
                    'TR'            :   4500,
                    'Greenville'    :   1500,
                    'MtRest'        :   6500,
                    'Cola'          :   4000
                }


# create and populate the list of decision variables
decisionVars = []

# make a 2D list of decision variables
for i, fromTown in enumerate(costs):
    temp = []
    for j, toTown in enumerate(costs[fromTown]):
        variable = str(fromTown + toTown)

		# variables are >= 0 and integers
        variable = pulp.LpVariable(str(variable), lowBound = 0, cat= 'Integer')
        temp.append(variable)
    decisionVars.append(temp)

# print the number of decision variabls that we have
print ("Total number of decision_variables: " + str(len(decisionVars)))

# make our total cost formula
totalCost = ""
for i, fromTown in enumerate(costs):
    for j, toTown in enumerate(costs[fromTown]):
        formula = costs[fromTown][toTown]*decisionVars[i][j]
        totalCost += formula

prob += totalCost
print ("Optimization function: " + str(totalCost))

# subject to supply constraints
for i, fromTown in enumerate(supplyAmounts):
	resource = supplyAmounts[fromTown]
	consumedResource= ""

	for j, toTown in enumerate(costs[fromTown]):
	    consumed = decisionVars[i][j]
	    consumedResource += formula
	prob += (consumedResource <= resource)

# subject to demand constraints
for j, toTown in enumerate(demandAmounts):
	demandAmount = demandAmounts[toTown]
	shippedResource= ""

	for i, fromTown in enumerate(costs):
		supplied = decisionVars[i][j]
		shippedResource += supplied

	prob += (shippedResource >= demandAmount)

# solve the problem
result = prob.solve()

# assert optimal result
assert result == pulp.LpStatusOptimal

prob.writeLP(problemName + ".lp" )
print("Status:", LpStatus[prob.status])
print("Optimal Solution to the problem: ", value(prob.objective))
print ("Individual decision_variables: ")
for v in prob.variables():
	if v.varValue > 0:
		print(v.name, "=", v.varValue)
