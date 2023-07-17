import random

def objective(x1,x2,x3):
    return (4/3)*(x1**2.0+x2**2.0-x1*x2)**0.75+x3

def fitness(x1,x2,x3):
    ans = objective(x1,x2,x3)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)


solutions = []
for s in range(1000):
    solutions.append((random.uniform(0,10000), random.uniform(0,10000),random.uniform(0,10000)))

print(solutions[:5])

for i in range(10000):

    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0],s[1],s[2]),s))
        rankedsolutions.sort()
        rankedsolutions.reverse()
        print("=== Gen {} best solutions ===".format(i))

        print(rankedsolutions[0])

