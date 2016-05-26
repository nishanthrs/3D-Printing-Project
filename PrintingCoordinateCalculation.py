import numpy as np
import sys

def calculateExtrusion(x, y, x1, y1):
	distance = (((x1-x)*(x1-x)) + ((y1-y)*(y1-y)))**0.5;
	return distance * 0.1;

def createFunctionPointsAndGCode(function, firstBound, finalBound):
	x1 = -1;
	y1 = -1;

	extrusionValue = 0;

	xValues = []; 
	yValues = [];
	zValues = [];
	extrusionValues = [];

	axis = 2;

	iterationArray = np.arange(int(firstBound), int(finalBound), .005);

	for x in iterationArray: ## for x in range(firstxBound, finalxBound):
		for i in range(1,60): ## Range must be twice the unit of measurement to rotate around 2*pi (full circle)
			xValue = x * np.cos(np.pi*i/30) + 50; ## Rotate x point by using cosine 
			yValue = x * np.sin(np.pi*i/30) + 50; ## Rotate y point by using sine 
			zValue = -1 * eval(function);         ## z point is simply elevation or function
			## xValue = eval(function);
			## yValue = x * np.sin(np.pi*i/30) + 50;
			## zValue = x * np.cos(np.pi*i/30) + 50;
			xValues.append(xValue); 
			yValues.append(yValue);
			zValues.append(zValue);
			if (x1 != -1 and y1 != -1):
				extrusionValue = calculateExtrusion(xValue, yValue, x1, y1);
				extrusionValues.append(extrusionValue); 
			## Previous values used to calculate distance between points and thus, extrusion values 
			x1 = xValue; 
			y1 = yValue;

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

	for num in range(1, (int(finalBound)-int(firstBound))*200*59-1): ## 5309 with 0.1
		maxHeight = -1 * zValues[(int(finalBound)-int(firstBound))*200*59-1]; ## merely a constant
		print("MAX HEIGHT: " + str(maxHeight));
		gCodeString += "G1" + " X" + str(xValues[num]) + " Y" + str(yValues[num]) + " Z" + str(zValues[num] + maxHeight) + " E" + str(extrusionValues[num]) + " F" + "2.5" + "\n";

	print "G CODE: " + gCodeString;	
	return gCodeString;

def write(gCode):

	try:
		file = open('G-Code.txt', 'w'); ## Create text file 
		file.write(gCode);

	except:
		print("Error");
		sys.exit(0); ## quit Python


