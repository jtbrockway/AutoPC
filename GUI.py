from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import subprocess

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
    print(leftFilePath)
    print(rightFilePath)
#os.system("#!./library disparity {}.format(leftFilePath) {}.format(rightFilePath)")       #KRISTEN HARDCODED IN FILENAME FOR LEFT, THEN RIGHT
    subprocess.call(["./library", "disparity", leftFilePath, rightFilePath])
    print('Disparity!')


# disparity button
b = ttk.Button(mainframe, text="Disparity", command=disparity)
b.grid(column=3, row=9, sticky=E)

def pointCloud():
    global focalLength
    global baseline
    global principleX
    global principleY

    temppath = leftFilePath[:-4] + '_disp.pgm'

    subprocess.call(["./library", "populate", leftFilePath, temppath, focalLength.get(), baseline.get(), principleX.get(), principleY.get()])
    print('Point Cloud!')

# point cloud button
b2 = ttk.Button(mainframe, text="Point Cloud", command=pointCloud)
b2.grid(column=4, row=9, sticky=S)

def visualize(): #liz will fix this 
    subprocess.call(["./library", "visualize", "point_cloud.pcd"])
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

ttk.Label(mainframe, text="").grid(column=1, row=10, sticky=W)
ttk.Label(mainframe, text="").grid(column=2, row=10, sticky=W)
ttk.Label(mainframe, text="").grid(column=3, row=10, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=11, sticky=W)
ttk.Label(mainframe, text="").grid(column=2, row=11, sticky=W)
ttk.Label(mainframe, text="").grid(column=3, row=11, sticky=W)

def sample1():  
    global focalLength 
    focalLength = 1216.001
    global principleX 
    principleX = 672.99
    global principleY 
    principleY = 265.32
    global baseline 
    baseline = 357.8

    global leftFilePath 
    leftFilePath = 'I1_000050.pgm'
    global rightFilePath 
    rightFilePath = 'I2_000050.pgm'

    disparity()
    pointCloud()
    visualize()
    print('Sample 1!')

# sample 1 button
b6 = ttk.Button(mainframe, text="Sample 1", command=sample1)
b6.grid(column=3, row=10, sticky=E)

def sample2():

    global focalLength 
    focalLength = 1216.001
    global principleX 
    principleX = 672.99
    global principleY 
    principleY = 265.32
    global baseline 
    baseline = 357.8

    global leftFilePath 
    leftFilePath = 'I1_000080.pgm'
    global rightFilePath 
    rightFilePath = 'I2_000080.pgm'

    disparity()
    pointCloud()
    visualize()
    print('Sample 2!')

# sample 2 button
b7 = ttk.Button(mainframe, text="Sample 2", command=sample2)
b7.grid(column=4, row=10, sticky=E)

def sample3():

    global focalLength 
    focalLength = 1216.001
    global principleX 
    principleX = 672.99
    global principleY 
    principleY = 265.32
    global baseline 
    baseline = 357.8

    global leftFilePath 
    leftFilePath = 'I1_000879.pgm'
    global rightFilePath 
    rightFilePath = 'I1_000879.pgm'

    disparity()
    pointCloud()
    visualize()
    print('Sample 3!')

# sample 3 button
b8 = ttk.Button(mainframe, text="Sample 3", command=sample3)
b8.grid(column=3, row=11, sticky=E)

# def sample4():

#     focalLength = '1216.001'
#     principleX = '672.99'
#     principleY = '265.32'
#     baseline = '357.8'

#     leftFilePath = ''
#     rightFilePath = ''

#     disparity()
#     pointCloud()
#     visualize()
#     print('Sample 4!')

# # sample 4 button
# b9 = ttk.Button(mainframe, text="Sample 4", command=sample4)
# b9.grid(column=4, row=11, sticky=E)

root.mainloop()
