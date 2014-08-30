#Edited from https://github.com/chrispy645/kaggle-cifar10-extract/blob/master/getpx.py

import sys
import csv
from PIL import Image

data = []
labels = []
f = open("C:/Users/kassidy/Desktop/Noel/kaggle/Object Recognition in Images/trainLabels.csv")
for line in f:
	labels.append(line.rstrip().split(',')[1])
f.close()

arr = []
for i in range(0,32*32):
	for j in ['r','g','b']:
		arr.append("px" + j + str(i))
arr.append("class")
data.append(",".join(arr))

for x in range(1, 50000+1):
	#im = Image.open('train/' + str(x) + '.png').convert('LA')
	im = Image.open('C:/Users/kassidy/Desktop/Noel/kaggle/Object Recognition in Images/train/' + str(x) + '.png')
	#im.show()
	arr = []
	for i in range(0, 32):
		for j in range(0, 32):
			tp = im.getpixel((i,j))
			arr.append( str(tp[0]) )
			arr.append( str(tp[1]) )
			arr.append( str(tp[2]) )
			
	data.append(",".join(arr) + "," + labels[x])
    
out = csv.writer(open("images.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
out.writerow(data)