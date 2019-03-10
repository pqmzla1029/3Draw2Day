import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

im = np.array(Image.open('frame0000.jpg'), dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# List to hold x values.
x_number_values = [463, 753, 988, 851, 463, 463, 753, 988, 851, 463]

# List to hold y values.
y_number_values = [930, 972, 972, 930, 930, 1332, 1215 ,1215, 1332, 1332]

# Create a Rectangle patch
#rect = patches.Rectangle((463,930),(930-463),971,linewidth=1,edgecolor='r',facecolor='none')
plt.plot(x_number_values, y_number_values, linewidth=3, color='cyan')
x_number_values = [753,753]
y_number_values = [972,1215]
plt.plot(x_number_values, y_number_values, linewidth=3, color='cyan')

x_number_values = [988,988]
y_number_values = [972,1215]
plt.plot(x_number_values, y_number_values, linewidth=3, color='cyan')

x_number_values = [851,851]
y_number_values = [930,1332]
plt.plot(x_number_values, y_number_values, linewidth=3, color='cyan')
# Add the patch to the Axes
#ax.add_patch(rect)

plt.show()
