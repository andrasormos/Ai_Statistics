# DELETING A ROW OR A COLUMN

import numpy as np
from numpy import array
import matplotlib.pyplot as plt
import random
np.set_printoptions(threshold=np.nan, linewidth=600)


#  3 x (5h x 4w image with 3 channels)  in other words, 3 boxes that are 5x4
mat = np.zeros((3, 5, 4, 3))

# in the 3rd box we are setting the 2nd column 2nd row value to 5
mat[2, 1, 1, 2] = 5

# we print this value
print("ELEMENT VALUE", mat[2, 1, 1, 2])

print("mat shape:", np.shape(mat))
print(mat)
print("\n")

# we extract the 5x4 2d image from the 3rd depth of the 3rd box
mat = mat[2, :, :, 2]
print("mat shape:", np.shape(mat))
print(mat)



if 1 == 1:
    plt.imshow(mat, cmap='hot')
    plt.colorbar()
    plt.show()