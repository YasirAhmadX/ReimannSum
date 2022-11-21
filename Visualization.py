from matplotlib import pyplot
from math import *
import numpy as np

def ReA(x,y,steps):
    area=0;
    for i in range(1,steps):
        area+= abs(x[i]-x[i-1])*y[i];
    return area;
def LeA(x,y,steps):
    area=0;
    for i in range(0,steps-1):
        area+= abs(x[i+1]-x[i])*y[i];
    return area;

E=input("Enter the expression: ");
L=int(input("Enter lower interval, closed bracket: "));
U=int(input("Enter upper interval, closed bracket: "));
steps=int(input("Enter number of rectangluar steps: "));
X=list(np.linspace(L,U,steps));
Y=[eval(E)for x in X];
print(X,Y,sep="\n");

rA=ReA(X,Y,steps);
lA=LeA(X,Y,steps);
print("Right Endpoint Estimated area is:  ",rA);
print("Left Endpoint Estimated area is: ",lA);

print("Overall estimation: ",(rA+lA)/2);
#parsing X,Y for bar for bar graphs
#Rx = 
#graphs
pyplot.xlabel("X axis");
pyplot.ylabel("Y axis");
pyplot.title("f(x) = "+E);
pyplot.grid(True,color='black');
pyplot.plot(X,Y,'r',label=E,linewidth=2);
#pyplot.show();
fig, axs = pyplot.subplots(2)
fig.suptitle('Reiman estimations')
axs[0].set_title(label="Right endpoints Area");
axs[1].set_title(label="Left endpoints Area");
axs[0].grid();
axs[0].plot(X,Y,'r',label=E);
axs[0].bar(X,Y,width = -abs(U-L)/steps,color='yellow',align='edge');
axs[1].bar(X,Y,width = abs(U-L)/steps,color='blue',align='edge');
axs[1].plot(X,Y,'r',label=E);
axs[1].grid();
pyplot.legend();
pyplot.show();