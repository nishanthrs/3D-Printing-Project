from Tkinter import *
from PrintingCoordinateCalculation import *
import parser

## Creates the window
root = Tk();

root.title("G-Code Generator");
root.geometry("1000x400");

app = Frame(root);
app.grid();

label = Label(app, text = "Enter a function!");
label.grid(row = 1, column = 0, sticky = W);
function = Entry(app);
function.grid(row = 3, column = 0, sticky = W);

v = IntVar();

xRevolveRadioButton = Radiobutton(root, text = "Revolve about x-axis", variable=v, value=1);
xRevolveRadioButton.grid(row = 1, column = 2, sticky = W);
yRevolveRadioButton = Radiobutton(root, text = "Revolve about y-axis", variable=v, value=2);
yRevolveRadioButton.grid(row = 2, column = 2, sticky = W);

def generateGCode():
	print("FUNCTION: " + function.get());
	print(v.get());
	gCodeString = createFunctionPointsAndGCode(function.get(), v.get());
	write(gCodeString);

generateGCodeButton = Button(app, text = "Generate", command = generateGCode);
generateGCodeButton.grid(row = 4, column = 0, sticky = W);

label.grid();

root.mainloop();