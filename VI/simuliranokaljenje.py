# from numpy import asarray ;
# from numpy import exp;
# from numpy.random import randn;
# from numpy.random import rand;
# from numpy.random import seed;
# import matplotlib.pyplot as plt;
#
# #ciljna funkcija
# def objective(x1,x2,x3):
#     return (4/3)*(x1[0]**2.0+x2[0]**2.0-x1[0]*x2[0])**0.75+x3[0];
#
# #algoritam simuliranog kaljenja
# def simuliranoKaljenje(objective, bounds, n, stepSize, tk):
#     #generisanje inincijalne tacke
#     best = bounds([2,0],[2,0],[2,0]);
#     #izracunavanje inicijalne tacke
#     best_eval = objective(best);
#     #trenutno resenje
#     curr, curr_eval = best, best_eval;
#     #skorovi
#     scores = list();
#     for i in range(n):
#         candidate = curr + randn(len(bounds))*stepSize;
#         candidate_eval = objective(candidate);
#         if candidate_eval<best_eval:
#             best,best_eval = candidate, candidate_eval;
#             scores.append(best_eval);
#             print('>%d f(%s) = %.5f' % (i,best,best_eval));
#             #razlika izmedju kandidata i trenutne tacke izracunavanja
#             diff = candidate_eval - curr_eval;
#             #temperatura za trenutnu iteraciju
#             t = tk/ float(i+1);
#             #metropolis acceptance kriterijum za prihvatanje gorih rezultata nego trenutnih
#             m = exp(-diff/t);
#             if diff < 0 or rand() <  m:
#                 curr,curr_eval = candidate, candidate_eval;
#     return [best,best_eval,scores];
#
#
# #pseudogenerator
# seed(1);
# #opseg za ulaz
# bounds = asarray([[0,2.0],[0,2.0],[0,2.0]]);
# #broj iteracija
# n = 100;
# #korak iteriranja
# stepSize =  0.1;
# #inicijalna temperatura
# tk =  10;
#
# #izvrsavanje algoritma
# best,score,scores = simuliranoKaljenje(objective,bounds,n,stepSize,tk);
# print("Gotovo!");
# print("f(%s) = %f" % (best,score));
#
# plt.plot(scores, '.-');
# plt.xlabel("Poboljsanje");
# plt.ylabel("Evaluacija f(x)");
# plt.show();

import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Parametri:
initial_temperature = 100
cooling = 0.8  # koeficijent hladjenja
number_variables = 3
upper_bounds = [2, 2, 2]
lower_bounds = [0, 0, 0]
computing_time = 1  # u sekundama


def objective(X):
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    value = (4/3)*(x1**2.0+x2**2.0-x1*x2)**0.75+x3;
    return value


# Simulirano kaljenje:
initial_solution = np.zeros((number_variables))
for v in range(number_variables):
    initial_solution[v] = random.uniform(lower_bounds[v], upper_bounds[v])

current_solution = initial_solution
best_solution = initial_solution
n = 1  # broj prihvacenih resenja
best_fitness = objective(best_solution)
current_temperature = initial_temperature  # trenutna temperatura
start = time.time()
no_attempts = 100  # broj iteracija za svaku vrednost temperature
record_best_fitness = []

for i in range(9999999):
    for j in range(no_attempts):
        for k in range(number_variables):
            current_solution[k] = best_solution[k] + 0.1 * (random.uniform(lower_bounds[k], upper_bounds[k]))
            current_solution[k] = max(min(current_solution[k],upper_bounds[k]),lower_bounds[k]) #popravka resenja

            current_fitness = objective(current_solution)
            err = abs(current_fitness-best_fitness)
            if i == 0 and j == 0:
                e = err

            if current_fitness > best_fitness:
                p = math.exp(-err/(e*current_temperature)) #verovatnoca s kojom donosimo odluku prisvajanja losijeg resenja
                if random.random() < p:
                    accept = True;
                else:
                    accept = False;
            else:
                accept = True; #bolje resenje se bezuslovno prihvata
            if accept == True:
                best_solution = current_solution; #najbolje resenje postaje trenutno resenje
                best_fitness = objective(best_solution);
                n = n+1;
                e = (e*(n-1) + e)/n

    print("iteracija br: {}, najbolje resenje: {}, najbolja fitness funkcija: {}".format(i,best_solution,best_fitness));
    record_best_fitness.append(best_fitness);
    current_temperature = current_temperature*cooling;
    end = time.time();
    if end-start >= computing_time:
        break;

plt.plot(record_best_fitness);
plt.show();

