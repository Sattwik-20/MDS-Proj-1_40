import cvxpy as cp
import numpy as np
import scipy
C=np.load("/content/C.npy")
y=np.load("/content/y.npy")
A_inv=np.load("/content/A_inv.npy")
y=y.reshape(y.shape[0],1)
s= cp.Variable((C.shape[1],1))
print(A_inv.shape)
print(C.shape)
print(y.shape)
print(s.shape)


objective = cp.Minimize(cp.norm(s,1));
constraints = [y-C@s==0]
prob=cp.Problem(objective,constraints)
result = prob.solve(verbose=True)

x=scipy.linalg.solve(A_inv,temp)

print(x)
print(s.value)

np.save("/content/s.npy",s)
np.save("/content/x.npy",x)



