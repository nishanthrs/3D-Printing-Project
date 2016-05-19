import numpy as np

xValues = [];     
yValues = [];
zValues = [];

firstxBound = 1;       ### starting x Bound 
finalxBound = 10;      ### starting y Bound
deltaX = (finalBound - firstBound) * .01 ###steps for the x-values 

### For x^2
for (x=firstxBound; x<finalxBound; x+=deltaX) {
	for i in range(1,60) {
		yValue = xValue**2 * np.cos(np.pi*x/30);
		zValue = xValue**2 * np.sin(np.pi*x/30);
		yValues.append(yValue);
		zValues.append(zValues);
	}
}





