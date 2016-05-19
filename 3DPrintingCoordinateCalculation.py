import numpy as np
import sys

xValues = [];     
yValues = [];
zValues = [];

firstBound = 1;       ### starting x Bound 
finalBound = 10;      ### starting y Bound
deltaX = (finalBound - firstBound) * .1; ###steps for the x-values 

### For x^2
for x in np.arange(firstBound, finalBound, .1): ## for x in range(firstxBound, finalxBound):
	for i in range(1,60): ## Range must be twice the unit of measurement to rotate around 2*pi (full circle)
		xValue = x * np.cos(np.pi*i/30) + 50; ## Rotate x point by using cosine 
		yValue = x * np.sin(np.pi*i/30) + 50; ## Rotate y point by using sine 
		zValue = x**0.5;                  ## z point is simply elevation or function
		xValues.append(xValue); 
		yValues.append(yValue);
		zValues.append(zValue);

print(xValues);
print(yValues);
print(zValues);

gCodeString = "G90\n";
gCodeString += "M107\n";
gCodeString += "M190 S55\n";
gCodeString += "M104 S196\n";
gCodeString += "G28\n";
gCodeString += "G1 Z5 F5000\n";
gCodeString += "M109 S196\n";
gCodeString += "G90\n";
gCodeString += "G92 E0\n";
gCodeString += "M82\n";
gCodeString += "G1 F1800.000 E-1.00000\n";
gCodeString += "G92 E0\n";

for num in range(1, 5310):
	## E part of GCode is calculated via formula (do later)
	gCodeString += "G1" + " " + "X" + str(xValues[num]) + " " + "Y" + str(yValues[num]) + " " + "Z" + str(zValues[num]) + " " + "E" + "5.0" + " " + "F" + "2.5" + "\n";

print gCodeString;	

def write():

	try:
		file = open('G-Code.txt', 'w'); ## Create text file 
		file.write(gCodeString);

	except:
		print("Error");
		sys.exit(0); ## quit Python

write(); 


