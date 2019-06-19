#!/usr/bin/python
import numpy as np
import random
m,n=input("enter the dimensions of first array").split()
a,b=input("enter the dimensions of second array").split()
x=np.random.randint(100,size=(int(m),int(n)))
y=np.random.randint(100,size=(int(a),int(b)))
with open("random_array.txt","w") as f:
    f.write("array 1 : \n"+str(x))
    f.write("\narray 2 : \n"+str(y))
