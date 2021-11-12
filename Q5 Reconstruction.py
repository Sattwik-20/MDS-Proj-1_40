import numpy as np
#creating a final 3d array which will be the merged 2d arrays
final=np.zeros((100,100,3))
for i in range (0,3):
#loading each x0, x1, x2 and then stacking them together
  x=np.load("/content/x{}.npy".format(i))
  #normalizin them to have better final reconstructed image
  x=normalize(np.reshape(x,(100,100)))
  final[:,:,i]=x.T
  #finally saving the 3D image
plt.imsave("/content/final.png",final)
