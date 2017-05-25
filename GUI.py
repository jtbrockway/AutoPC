from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

filename = ""
root = Tk()
root.title("AutoPC")

# set up framework
mainframe = ttk.Frame(root, padding="30 30 80 80")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

focalLength = StringVar(root)

ttk.Label(mainframe, text="").grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="").grid(column=4, row=2, sticky=W)

# text field to enter focal length
ttk.Label(mainframe, text="Focal Length").grid(column=2, row=3)
ttk.Entry(mainframe, text='', textvariable=focalLength, width=8).grid(column=3, row=3)

principleX = StringVar(root)

# text field to enter principle x
ttk.Label(mainframe, text="Principle X").grid(column=2, row=4)
ttk.Entry(mainframe, text='', textvariable=principleX, width=8).grid(column=3, row=4)

principleY = StringVar(root)

# text field to enter principle y
ttk.Label(mainframe, text="Principle Y").grid(column=2, row=5)
ttk.Entry(mainframe, text='', textvariable=principleY, width=8).grid(column=3, row=5)

baseline = StringVar(root)

# text field to enter baseline
ttk.Label(mainframe, text="Baseline").grid(column=2, row=6)
ttk.Entry(mainframe, text='', textvariable=baseline, width=8).grid(column=3, row=6)

ttk.Label(mainframe, text="").grid(column=2, row=7, sticky=W)
ttk.Label(mainframe, text="").grid(column=3, row=7, sticky=W)
ttk.Label(mainframe, text="").grid(column=4, row=7, sticky=W)

def disparity():
    os.system("./library disparity I1_000055.pgm I2_000055.pgm")       #KRISTEN HARDCODED IN FILENAME FOR LEFT, THEN RIGHT
    print('Disparity!')


# disparity button
b = ttk.Button(mainframe, text="Disparity", command=disparity)
b.grid(column=3, row=8, sticky=E)

def pointCloud():
    global focalLength
    global baseline
    global principleX
    global principleY
    focalLength = 1216.0089
    baseline = 357.8112
    principleX = 672.9872 #Kristen change to be read from boxes, and image names no hardcoded
    principleY = 265.3183
    tempstring = "./library populate I1_000055.pgm I1_000055_disp.pgm " + str(focalLength) + ' '+   str(baseline) + ' ' + str(principleX) + ' '+  str(principleY)
    os.system(tempstring)
    print('Point Cloud!')

# point cloud button
b2 = ttk.Button(mainframe, text="Point Cloud", command=pointCloud)
b2.grid(column=4, row=8, sticky=S)

def visualize(): #liz will fix this 
    os.system("./pcl_visualizer_demo -r point_cloud.pcd")
    print('Visualize!')

# visualize button
b3 = ttk.Button(mainframe, text="Visualize", command=visualize)
b3.grid(column=5, row=8, sticky=W)

def browseFiles():
        global filename
        filename = filedialog.askopenfilename()
        pathlabel.config(text=filename)

pathlabel = Label(root)

# left image button button
b4 = ttk.Button(mainframe, text="Upload Left Image", command=browseFiles)
b4.grid(column=3, row=1) #sticky=E)

# right image button button
b5 = ttk.Button(mainframe, text="Upload Right Image", command=browseFiles)
b5.grid(column=5, row=1) #sticky=W)

root.mainloop()
