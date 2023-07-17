import numpy as np
import genetskialgoritam
import time
import matplotlib.pyplot as plt

variables  = 3
popSize = 100
crossover_rate = 20
mutation_rate = 10
n = 300
lower_bounds = [0,0,0]
upper_bounds = [2,2,2]
stepSize = 5
rate = 10
pop = np.zeros((popSize,variables))
for s in range(popSize):
    for h in range(variables):
        pop[s,h] = np.random.uniform(lower_bounds[h],upper_bounds[h])

extendedPop = np.zeros((popSize+crossover_rate+mutation_rate+2*variables*rate,pop.shape[1]))

#Vizualizacija
fig = plt.figure()
ax = fig.add_subplot()
fig.show()
plt.title("Evolucija ciljne funkcije")
plt.xlabel("Iteracija")
plt.ylabel("Ciljna funkcija")

A = []
a = 5
g = 0
globalBest = pop
k = 0

while g<n:
    for i in range(n):
        offspring1 = genetskialgoritam.crossover(pop,crossover_rate)
        offspring2 = genetskialgoritam.mutation(pop,mutation_rate)
        fitness = genetskialgoritam.objective(pop)
        offspring3 = genetskialgoritam.local_search(pop,fitness,lower_bounds,upper_bounds,stepSize,rate)
        stepSize = stepSize*0.98
        if stepSize < 1:
            stepSize = 1
        extendedPop[0:popSize] = pop
        extendedPop[popSize:popSize+crossover_rate] = offspring1
        extendedPop[popSize + crossover_rate:popSize+crossover_rate+mutation_rate] = offspring2
        extendedPop[popSize + crossover_rate+mutation_rate:popSize + crossover_rate + mutation_rate+2*variables*rate] = offspring3
        fitness = genetskialgoritam.objective(extendedPop)
        pop = genetskialgoritam.selection(extendedPop,fitness,popSize)
        print("Generation: ",g, " , Fitness value: " , 10e6-min(fitness))
        A.append(10e6-min(fitness))
        g = g+1
        if i>=a:
            if (sum(abs(np.diff(A[g-a:g]))) <= 0.05).any():
                index = np.argmin(fitness)
                currentBest = extendedPop[index]
                pop = np.zeros((popSize, variables))
                for s in range(popSize):
                    for h in range(variables):
                        pop[s,h]  = np.random.uniform(lower_bounds[h],upper_bounds[h])
                stepSize = 5
                globalBest[k] = currentBest
                k = k+1
                break

            #Vizualizacija
            ax.plot(A, color = 'r')
            fig.canvas.draw()
            ax.set_xlim(left=max(0, g-n), right=g+3)
            if g>n:
                break
        if g>n:
            break


fitness = genetskialgoritam.objective(globalBest)
index = np.argmin(fitness)
print("Najbolje resenje: " , globalBest[index])
print("Najbolja vrednost ciljne funkcije: ", 10e6-min(fitness))
plt.show();


