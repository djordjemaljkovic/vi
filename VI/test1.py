from numpy import arange
import matplotlib.pyplot as plt

# #ciljna funkcija
# def objective(x):
#     #return (4/3)*(x1[0]**2.0+x2[0]**2.0-x1[0]*x2[0])**0.75+x3[0];
#     return x[0]**2.0;
#
# #opseg ciljne funkcije
# rmin,rmax = -2.0,2.0;
# inputs = arange(rmin,rmax,1.0);
# #izracunati ciljeve
# results = [objective([x]) for x in inputs]
# #iscrtavanje
# plt.plot(inputs,results);
# x_opt = 0.0;
# plt.axvline(x = x_opt,ls ="--",color = "red");
# plt.show()

n = 100;
init_tk = 10;
n = [i for i in range(n)];
temperatures = [init_tk/float(i+1) for i in n];
plt.plot(n,temperatures);
plt.xlabel("Iteracije");
plt.ylabel("Temperature");
plt.show();
