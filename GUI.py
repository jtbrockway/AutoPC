from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

leftFilePath = ""
rightFilePath = ""
root = Tk()
root.title("AutoPC")

# set up framework
mainframe = ttk.Frame(root, padding="30 30 80 80")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

focalLength = StringVar(root)

ttk.Label(mainframe, text="").grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="").grid(column=4, row=3, sticky=W)

# text field to enter focal length
ttk.Label(mainframe, text="Focal Length").grid(column=2, row=4)
ttk.Entry(mainframe, text='', textvariable=focalLength, width=8).grid(column=3, row=4)

principleX = StringVar(root)

# text field to enter principle x
ttk.Label(mainframe, text="Principle X").grid(column=2, row=5)
ttk.Entry(mainframe, text='', textvariable=principleX, width=8).grid(column=3, row=5)

principleY = StringVar(root)

# text field to enter principle y
ttk.Label(mainframe, text="Principle Y").grid(column=2, row=6)
ttk.Entry(mainframe, text='', textvariable=principleY, width=8).grid(column=3, row=6)

baseline = StringVar(root)

# text field to enter baseline
ttk.Label(mainframe, text="Baseline").grid(column=2, row=7)
ttk.Entry(mainframe, text='', textvariable=baseline, width=8).grid(column=3, row=7)

ttk.Label(mainframe, text="").grid(column=2, row=8, sticky=W)
ttk.Label(mainframe, text="").grid(column=3, row=8, sticky=W)
ttk.Label(mainframe, text="").grid(column=4, row=8, sticky=W)

def disparity():
    os.system("./library disparity {}.format(leftFilePath) {}.format(rightFilePath)")       #KRISTEN HARDCODED IN FILENAME FOR LEFT, THEN RIGHT
    print('Disparity!')


# disparity button
b = ttk.Button(mainframe, text="Disparity", command=disparity)
b.grid(column=3, row=9, sticky=E)

def pointCloud():
    global focalLength
    global baseline
    global principleX
    global principleY

    tempstring = "./library populate {}.format(leftFilePath) {}.format(rightFilePath) " + focalLength.get() + ' '+   baseline.get() + ' ' + principleX.get() + ' '+  principleY.get()
    # os.system(tempstring)
    print(tempstring)
    print('Point Cloud!')

# point cloud button
b2 = ttk.Button(mainframe, text="Point Cloud", command=pointCloud)
b2.grid(column=4, row=9, sticky=S)

def visualize(): #liz will fix this 
    os.system("./pcl_visualizer_demo -r point_cloud.pcd")
    print('Visualize!')

# visualize button
b3 = ttk.Button(mainframe, text="Visualize", command=visualize)
b3.grid(column=5, row=9, sticky=W)

def browseLeft():
    global leftFilePath
    leftFilePath = filedialog.askopenfilename()
    pathLeftLabel.config(text=os.path.basename(leftFilePath))

pathLeftLabel = Label(root)
# pathLeftLabel.grid(column=3, row=2, sticky=W)

def browseRight():
    global rightFilePath
    rightFilePath = filedialog.askopenfilename()
    pathRightLabel.config(text=os.path.basename(rightFilePath))

pathRightLabel = Label(root)
# pathRightLabel.grid(column=5, row=2, sticky=W)

# left image button button
b4 = ttk.Button(mainframe, text="Upload Left Image", command=browseLeft)
b4.grid(column=3, row=1)

# right image button button
b5 = ttk.Button(mainframe, text="Upload Right Image", command=browseRight)
b5.grid(column=5, row=1)

root.mainloop()
