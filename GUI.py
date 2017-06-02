from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import subprocess

leftFilePath = ""
rightFilePath = ""
root = Tk()
root.title("AutoPC")
focal = 0.0
prinX = 0.0
prinY = 0.0
base = 0.0
enterFlag = False # to be used if entering from Samples

# set up framework
mainframe = ttk.Frame(root, padding="30 30 80 80")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

focalLength = StringVar(root)

# extra spacing to make layout of GUI look nicer
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

# extra spacing to make layout of GUI look nicer
ttk.Label(mainframe, text="").grid(column=2, row=8, sticky=W)
ttk.Label(mainframe, text="").grid(column=3, row=8, sticky=W)
ttk.Label(mainframe, text="").grid(column=4, row=8, sticky=W)

# function that is called when disparity button is pushed
def disparity():
    subprocess.call(["./library", "disparity", leftFilePath, rightFilePath])
    
    #print('Disparity!')

# disparity button
b = ttk.Button(mainframe, text="Disparity", command=disparity)
b.grid(column=3, row=9, sticky=E)

# function that is called when point cloud button is pushed
def pointCloud():
    global enterFlag
    global focal
    global base
    global prinX
    global prinY
    if (not enterFlag):
        focal = focalLength.get()
        base = baseline.get()
        prinX = principleX.get()
        prinY = principleY.get()

    temppath = leftFilePath[:-4] + '_disp.pgm'

    subprocess.call(["./library", "populate", leftFilePath, temppath, str(focal), str(base), str(prinX), str(prinY)])
    enterFlag = False

    #print('Point Cloud!')

# point cloud button
b2 = ttk.Button(mainframe, text="Point Cloud", command=pointCloud)
b2.grid(column=4, row=9, sticky=S)

# function that is called when visualize button is pushed
def visualize(): #liz will fix this 
    subprocess.call(["./library", "visualize", "point_cloud.pcd"])
    
    #print('Visualize!')

# visualize button
b3 = ttk.Button(mainframe, text="Visualize", command=visualize)
b3.grid(column=5, row=9, sticky=W)

# function to allow user to upload a left image
def browseLeft():
    global leftFilePath
    leftFilePath = filedialog.askopenfilename()
    pathLeftLabel.config(text=os.path.basename(leftFilePath))

pathLeftLabel = Label(root)
# pathLeftLabel.grid(column=3, row=2, sticky=W)

# function to allow user to upload a right image
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

# extra spacing to make layout of GUI look nicer
ttk.Label(mainframe, text="").grid(column=3, row=10, sticky=W)
ttk.Label(mainframe, text="").grid(column=4, row=10, sticky=W)
ttk.Label(mainframe, text="").grid(column=5, row=10, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=11, sticky=W)
ttk.Label(mainframe, text="").grid(column=2, row=11, sticky=W)
ttk.Label(mainframe, text="").grid(column=3, row=11, sticky=W)

# sample of two images converted to disparity image, point cloud and then fully visualized
def sample1(): 
    global enterFlag
    enterFlag = True
    global focal
    focal = 1216.001
    global prinX 
    prinX = 672.99
    global prinY 
    prinY = 265.32
    global base 
    base = 357.8

    global leftFilePath 
    leftFilePath = 'samples/I1_000055.pgm'
    global rightFilePath 
    rightFilePath = 'samples/I2_000055.pgm'

    disparity()
    pointCloud()
    visualize()
    print('Sample 1!')

# sample 1 button
b6 = ttk.Button(mainframe, text="Sample 1", command=sample1)
b6.grid(column=3, row=11, sticky=E)

# sample of two images converted to disparity image, point cloud and then fully visualized
def sample2():
    global enterFlag
    enterFlag = True
    global focal 
    focal = 1216.001
    global prinX 
    prinX = 672.99
    global prinY 
    prinY = 265.32
    global base 
    base = 357.8

    global leftFilePath 
    leftFilePath = 'samples/I1_000080.pgm'
    global rightFilePath 
    rightFilePath = 'samples/I2_000080.pgm'

    disparity()
    pointCloud()
    visualize()
    print('Sample 2!')

# sample 2 button
b7 = ttk.Button(mainframe, text="Sample 2", command=sample2)
b7.grid(column=4, row=11, sticky=S)

# sample of two images converted to disparity image, point cloud and then fully visualized
def sample3():
    global enterFlag
    enterFlag = True
    global focal 
    focal = 1216.001
    global prinX 
    prinX = 672.99
    global prinY 
    prinY = 265.32
    global base 
    base = 357.8

    global leftFilePath 
    leftFilePath = 'samples/I1_000879.pgm'
    global rightFilePath 
    rightFilePath = 'samples/I2_000879.pgm'

    disparity()
    pointCloud()
    visualize()
    print('Sample 3!')

# sample 3 button
b8 = ttk.Button(mainframe, text="Sample 3", command=sample3)
b8.grid(column=5, row=11, sticky=W)

root.mainloop()
