#printing pattern
import numpy as np
for i in range(5):
    j,k,m=4,0,1
    while(j>i):
        print(" ",end="")
        j-=1
    while(k<=i):
        print("*",end="")
        k+=1
    while(m<=i):
        print("*",end="")
        m+=1
    print("")