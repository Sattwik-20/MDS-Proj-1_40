#This code was already shared with us. 
#We updated the file location.
#we changed the PIL mode to RGB which generated 3 different images
#and used a for loop to generate A_inv, y and C for each image individually (R,G,B).

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as spfft
import scipy.ndimage as spimg
import imageio
#%% Discrete Cosine Transform 
def dct2(x):
    return spfft.dct(spfft.dct(x.T, norm='ortho', axis=0).T, norm='ortho', axis=0)

def idct2(x):
    return spfft.idct(spfft.idct(x.T, norm='ortho', axis=0).T, norm='ortho', axis=0)

#%% VARIABLES FOR YOU TO CHANGE
path_to_your_image="/content/1612675662165.jpg"
zoom_out=0.9999999 #Fraction of the image you want to keep.
corruption=0.7#Fraction of the pixels that you want to discard
#%% Get image and create y
# read original image and downsize for speed
Xorig =imageio.imread(path_to_your_image,pilmode='RGB') # read in grayscale
#Downsize image orig
Xtemp = spimg.zoom(Xorig, zoom_out)
print(Xtemp.shape)
plt.imshow(Xtemp)
plt.title("Original")
plt.show()
mask_array=np.zeros((100,100,3))
xm_array=np.zeros((100,100,3))

for i in range(0,3):
  X=Xtemp[:,:,i]
  b = X.T.flat[ri]
  b = np.expand_dims(b, axis=1)
  #%% CREATE A inverse and C
  # *******************************************************************************************
  """This part consumes a lot of memory. Your PC might crash if the images you load are larger than 100 x 100 pixels """
  # create dct matrix operator using kron (memory errors for large ny*nx)
  Aa = np.kron(np.float16(spfft.idct(np.identity(nx), norm='ortho', axis=0)),
      np.float16(spfft.idct(np.identity(ny), norm='ortho', axis=0))
      )
  A = Aa[ri,:] # same as B times A
# *******************************************************************************************
# create images of mask (for visualization)
  mask = np.zeros(X.shape)
  mask.T.flat[ri] = True
  mask[mask==0]=False
  masked=X*mask

  Xm = 255 * np.ones(X.shape)
  Xm.T.flat[ri] = X.T.flat[ri]
  #print("Xm-shape",Xm.shape)
  #%%
  plt.imshow(masked)
  plt.title("Mask{}".format(i))
  plt.show()

  np.save("/content/C{}.npy".format(i),A)
  np.save("/content/A_inv{}.npy".format(i),Aa)
  np.save("/content/y{}.npy".format(i),b)
  plt.imsave("/content/incomplete{}.png".format(i),Xm)
  plt.imsave("/content/original_cropped{}.png".format(i),X)
