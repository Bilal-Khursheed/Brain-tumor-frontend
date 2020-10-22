import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Get nibabel image object
def display(path,filename,save='static/uploads/'):
    img = nib.load(path + filename)

    # Get data from nibabel image object (returns numpy memmap object)
    img_data = img.get_data()
    ii=img_data[:,:,80]
    
    # Convert to numpy ndarray (dtype: uint16)
    img_data_arr = np.asarray(img_data)

    # plot a slice
    img = Image.fromarray(img_data_arr[:,:,50], 'L')

    file_save_path=save + "Save" +filename
    # Show Plot
    plt.imsave(file_save_path,ii,          #numpy array generating the image
           cmap = 'viridis')             #color map used to specify colors
                                      #algorithm used to blend square colors; with 'nearest' colors will not be blended
                                      