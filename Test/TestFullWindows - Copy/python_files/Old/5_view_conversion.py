import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import os
#os.chdir("..")
#print(os.getcwd())
print(os.getcwd())
def plot_total(filename):
	
	im = np.array(Image.open('image_files/frame0000.jpg'), dtype=np.uint8)

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
	a = np.loadtxt("working_data/bounding_data/"+filename+".txt", skiprows=0, usecols = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
	#print(a)
	
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
	"""
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
	"""
	
	color_array=["blue","red","green","cyan","orange","pink"]
	len_a=a.shape
	#print(len_a[0])
	for index_item in range(0,len_a[0]):
		x_number_values= np.zeros(5)
		y_number_values= np.zeros(5)
		
		count=0
		for i in range(0,5):
			x_number_values[i] = a[index_item][count%8]
			y_number_values[i] = a[index_item][count%8+1]
			count=count+2
		plt.plot(x_number_values, y_number_values, linewidth=3, color=color_array[index_item])
		#plt.show()
	
		start=count-2
		count=8
		for i in range(0,5):
			x_number_values[i] = a[index_item,count%8+start]
			y_number_values[i] = a[index_item,count%8+1+start]
			count=count+2
		plt.plot(x_number_values, y_number_values, linewidth=3, color=color_array[index_item])
	
		count=0
		inter=8
		for i in range(0,4):
		    x_number_values = [a[index_item,count],a[index_item,count+inter]]
		    y_number_values = [a[index_item,count+1],a[index_item,count+1+inter]]
		    #print(x_number_values, y_number_values)
		    plt.plot(x_number_values, y_number_values, linewidth=3, color=color_array[index_item])
		    count=count+2

	plt.show()

def main():
	#item_curr=0
	filename="frame0001"
	plot_total(filename)

main()
