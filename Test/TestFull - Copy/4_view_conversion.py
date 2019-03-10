import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

im = np.array(Image.open('frame0000.jpg'), dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)
'''
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
'''
a = np.loadtxt('outfile.txt')
#print(a)
x_number_values= np.zeros(5)
y_number_values= np.zeros(5)
'''
# List to hold x values.
for i in range(0,4+1):
    j=i%4
    x_number_values[i] = a[0,j]

# List to hold y values.
for i in range(0,4+1):
    j=i%4
    y_number_values[i] = a[1,j]
print(x_number_values, y_number_values)
# Create a Rectangle patch
#rect = patches.Rectangle((463,930),(930-463),971,linewidth=1,edgecolor='r',facecolor='none')
plt.plot(x_number_values, y_number_values, linewidth=3, color='blue')

# List to hold x values.
for i in range(4,8+1):
    j=(i%4)+4
    x_number_values[i-4] = a[0,j]

# List to hold y values.
for i in range(4,8+1):
    j=(i%4)+4
    y_number_values[i-4] = a[1,j]
print(x_number_values, y_number_values)
# Create a Rectangle patch
#rect = patches.Rectangle((463,930),(930-463),971,linewidth=1,edgecolor='r',facecolor='none')
plt.plot(x_number_values, y_number_values, linewidth=3, color='blue')
'''
rv=4
for k in range(0,2):
    start_val=(k*rv)
    # List to hold x values.
    for i in range(start_val,(rv+start_val)+1):
        j=(i%4)+start_val
        x_number_values[i-start_val] = a[0,j]

    # List to hold y values.
    for i in range(start_val,(rv+start_val)+1):
        j=(i%4)+start_val
        y_number_values[i-start_val] = a[1,j]
    print(x_number_values, y_number_values)
    # Create a Rectangle patch
    #rect = patches.Rectangle((463,930),(930-463),971,linewidth=1,edgecolor='r',facecolor='none')
    plt.plot(x_number_values, y_number_values, linewidth=3, color='blue')

for i in range(0,4):
    x_number_values = [a[0,i],a[0,i+4]]
    y_number_values = [a[1,i],a[1,i+4]]
    #print(x_number_values, y_number_values)
    plt.plot(x_number_values, y_number_values, linewidth=3, color='blue')

plt.show()
