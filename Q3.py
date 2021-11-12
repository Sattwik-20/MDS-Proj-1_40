import cvxpy as cp
#imported cvxpy library for solving optimization problems
import numpy as np
#imported scipy for solving linear algebra equation
import scipy

#loading the contents of C, y and A_inv which are in the form of .npy files to form numpy arrays to be used in the program
C=np.load("/content/C.npy")
y=np.load("/content/y.npy")
A_inv=np.load("/content/A_inv.npy")

#Reshaping the sizeq of y as a single column vector
y=y.reshape(y.shape[0],1)
#Reshaping the value of s as a column vector with the no. of rows as the no. of columns of C (eligibility for matrix multiplication)
s= cp.Variable((C.shape[1],1))

#Shapes were printed just for confimration
print(A_inv.shape)
print(C.shape)
print(y.shape)
print(s.shape)

#After the shapes were confirmed
#CVXPY library fucntions were used to define the convex optimzation problem
objective = cp.Minimize(cp.norm(s,1)); # objective function definition
constraints = [y-C@s==0] #constraints were defined
prob=cp.Problem(objective,constraints) #problem was created

result = prob.solve(verbose=True) # result i:e an optimal solution (column vector will be ovtained) verbose=True helped track the steps while the prob.solve was running

#Solving the linear algebra equation to obtain x.
x=scipy.linalg.solve(A_inv,s.value)#using the s

print(x)
print(s.value)

#contents were saved
np.save("/content/s.npy",s)
np.save("/content/x.npy",x)



