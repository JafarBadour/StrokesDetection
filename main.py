import os

import numpy as np
import matplotlib.pyplot as plt
def show_slices(slices):

   """ Function to display row of image slices """

   fig, axes = plt.subplots(1, len(slices))

   for i, slice in enumerate(slices):

       axes[i].imshow(slice.T, cmap="gray", origin="lower")


example_filename = os.path.join('/home/jafar/PycharmProjects/CTstrokes', 'VSD.Brain.XX.O.MR_4DPWI.127015.nii.gz')
import nibabel as nib

img = nib.load(example_filename)

data = img.get_fdata()
print(data.shape)



