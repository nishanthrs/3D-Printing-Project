from Tkinter import *
from PrintingCoordinateCalculation import *
import parser
import re

## Creates the window
root = Tk();

root.title("G-Code Generator");
root.geometry("1000x400");

app = Frame(root);
app.grid();

label = Label(app, text = "Enter a function!");
label.grid(row = 1, column = 0, sticky = W);
function = Entry(app);
function.grid(row = 3, column = 0, sticky = W)

firstxBound = Entry(app);
firstxBound.grid(row = 0, column = 2, sticky = W);
finalxBound = Entry(app);
finalxBound.grid(row = 1, column = 2, sticky = W);

def generateGCode():
	print("FUNCTION: " + function.get());
	## maxDegree = float(function.get()[6]);
	## print("MAX DEGREE: " + str(maxDegree));
	gCodeString = createFunctionPointsAndGCode(function.get(), firstxBound.get(), finalxBound.get(), 2);
	writeToFile(gCodeString);

generateGCodeButton = Button(app, text = "Generate", command = generateGCode);
generateGCodeButton.grid(row = 4, column = 0, sticky = W);

label.grid();

root.mainloop();