import numpy as np
import sys

def calculateExtrusion(x, y, x1, y1):
	distance = (((x1-x)*(x1-x)) + ((y1-y)*(y1-y)))**0.5;
	return distance * 0.1;

def createFunctionPointsAndGCode(function, firstBound, finalBound, maxDegree):
	x1 = -1;
	y1 = -1;
	z1 = -1;

	extrusionValue = 0;

	xValues = []; 
	yValues = [];
	zValues = [];
	extrusionValues = [];

	## zValue = 0;

	epsilon = 0.3;

	deltaBounds = .005; ## Default value

	if (maxDegree > 0 and maxDegree <= 1):
		deltaBounds = .01; ## Adjust this based on maximum height (calculate some formula)
	elif (maxDegree > 1 and maxDegree <= 2):
		deltaBounds = .008;
	elif (maxDegree > 2 and maxDegree <= 3):
		deltaBounds = .001;

	iterationArray = np.arange(int(firstBound), int(finalBound), deltaBounds); ## Adjust this based on maximum height (calculate some formula)

	for x in iterationArray[::-1]: ## for x in range(firstxBound, finalxBound):
		for i in range(1,60): ## Range must be twice the unit of measurement to rotate around 2*pi (full circle)
			xValue = x * np.cos(np.pi*i/30) + 100; ## Rotate x point by using cosine 
			yValue = x * np.sin(np.pi*i/30) + 100; ## Rotate y point by using sine 
			zValue = -1 * eval(function);         ## z point is simply elevation or function - change to tempzValue later
			## Only fix below issue if above idea (adjustment of deltaBounds based on max height)
			'''
			if (np.absolute(z1-tempzValue) > epsilon):
				print("Z STEP EXCEEDED");
				print("Z1: " + str(z1));
				print("TEMP Z: " + str(tempzValue));
				## zValue = z1 + epsilon; Issue is occuring here because this value ends up being way off the actual z calculation (figure out math behind it)
				print("Z: " + str(zValue));
			else:
				## print("Z STEP NOT EXCEEDED");
				## print("Z1: " + str(z1));
				## print("Z: " + str(zValue));
				zValue = -1 * eval(function);
			## xValue = eval(function);
			## yValue = x * np.sin(np.pi*i/30) + 50;
			## zValue = x * np.cos(np.pi*i/30) + 50;
			'''
			xValues.append(xValue); 
			yValues.append(yValue);
			zValues.append(zValue);
			if (x1 != -1 and y1 != -1):
				extrusionValue += calculateExtrusion(xValue, yValue, x1, y1);
				extrusionValues.append(extrusionValue);
			## Previous values used to calculate distance between points and thus, extrusion values 
			x1 = xValue; 
			y1 = yValue;
			z1 = zValue;

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

	## maxHeight = -1 * zValues[(int(finalBound)-int(firstBound))*int(1/deltaBounds)*59-1]; ## merely a constant
	maxHeight = -1 * zValues[0]; ## merely a constant
	print("MAX HEIGHT: " + str(maxHeight));

	for num in range(1, (int(finalBound)-int(firstBound))*int(1/deltaBounds)*59-1): ## 5309 with 0.1
		gCodeString += "G1" + " X" + str(xValues[num]) + " Y" + str(yValues[num]) + " Z" + str(zValues[num] + maxHeight) + " E" + str(extrusionValues[num]) + " F" + "1500.0" + "\n";

	print "G CODE: " + gCodeString;	
	return gCodeString;

def writeToFile(gCode):

	try:
		file = open('G-Code.txt', 'w'); ## Create text file 
		file.write(gCode);

	except:
		print("Error");
		sys.exit(0); ## quit Python


