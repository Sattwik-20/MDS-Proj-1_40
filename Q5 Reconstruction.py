import numpy as np
final=np.zeros((100,100,3))
for i in range (0,3):

  x=np.load("/content/x{}.npy".format(i))
  x=normalize(np.reshape(x,(100,100)))
  final[:,:,i]=x.T
plt.imsave("/content/final.png",final)