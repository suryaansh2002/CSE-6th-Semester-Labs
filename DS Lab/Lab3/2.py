import numpy as np

a=np.array([[1,2],[3,4]])


print(a)
print("Sum of Rows " + str(np.sum(a,axis=1)))
print("Sum of Cols " + str(np.sum(a,axis=0)))