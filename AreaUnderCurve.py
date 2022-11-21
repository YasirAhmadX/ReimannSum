import numpy as np

E=input("Enter the expression: ");
L=int(input("Enter lower interval, closed bracket: "));
U=int(input("Enter upper interval, closed bracket: "));
steps=int(input("Enter number of rectangluar steps: "));
X=np.linspace(L,U,steps);
Y=np.matrix([eval(E)for x in X]);
print(X,Y,sep="\n");
print([i for i in X],type([i for i in X]));

def ReA(x,y):
    area=0;
    for i in range(1,steps):
        area+= abs(x[i]-x[i-1])*y[0,i];
    return area;
def LeA(x,y):
    area=0;
    for i in range(0,steps-1):
        area+= abs(x[i+1]-x[i])*y[0,i];
    return area;
print("Right Endpoint Estimated area is:  ",ReA(X,Y));
print("Left Endpoint Estimated area is: ",LeA(X,Y));