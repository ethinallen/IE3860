locations = {   0   :   [0, 0],
                1   :   [15, 30],
                2   :   [5, 30],
                3   :   [10, 20],
                4   :   [5, 5],
                5   :   [20, 10]
            }

costs = {}

for fr in locations:
    costs[fr] = {}
    for to in locations:
        if fr < to:
            key = ((fr, to))
            cost = ((locations[fr][0] - locations[to][0])**2 + (locations[fr][1] - locations[to][1])**2)**.5
            costs[fr][to] = cost
            print(fr, to, cost)
print('__________________\n\n')
savings = {}
for i in range(1,5):
    savings[i] = {}
    for j in range(1,6):
        if j > i:
            saving = costs[0][i] + costs[0][j] - costs[i][j]
            savings[i][j] = saving
            print(i, j, saving)


print('COSTS:\t{}'.format(costs))
print('SAVINGS:\n{}'.format(savings))
