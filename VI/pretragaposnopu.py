import numpy as np
import random

n = 100
beta = 5
number_variables = 3
upper_bounds = [2,2,2]
lower_bounds = [0,0,0]
list = []
nextGen = []
resenja = []
indeksi = []

def objective(X):
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    value = (4/3)*(x1**2.0+x2**2.0-x1*x2)**0.75+x3;
    return value

initial_solution = np.zeros((number_variables))
for v in range(number_variables):
    initial_solution[v] = random.uniform(lower_bounds[v], upper_bounds[v])



#def beamSearch(fitness,beta):
    current_solution = initial_solution
    best_solution = initial_solution
    best_fitness = objective(best_solution)


for j in range (n):
    for k in range (number_variables):
        current_solution[k] = best_solution[k] - 0.01 * (random.uniform(lower_bounds[k], upper_bounds[k]))
        current_solution[k] = max(min(current_solution[k], upper_bounds[k]),lower_bounds[k])  # popravka resenja ukoliko je ispalo iz opsega
    current_fitness = objective(current_solution)
    resenja.append(current_solution)
    list.append(current_fitness)
    sortedList = np.sort(list, axis = 0)
print(resenja)
print(list)
print(sortedList)



for b in range(beta):
    nextGen.append(sortedList[b])
    for t in range(len(list)):
        if (list[t] == sortedList[b]): print(t)
        if (list[t] == sortedList[b]): indeksi.append(t)

print(nextGen)
print(indeksi)




















