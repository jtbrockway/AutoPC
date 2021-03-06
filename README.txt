*************************
* What is this Product? *
*************************
This product uses libelas, Point Cloud Library, and OpenCV to create a single program that allows you to:
	-Generate a disparity image
	-Generate a point cloud from a disparity image and a rectified image 
	-Visualize a point cloud.

This product comes with a GUI that you can use to create a disparity image, create a point cloud, and visualize a point cloud.

This product also has the ability to be ran purely from the terminal.

Please note:
	The GUI is best used if you are meaning to generate and visualize a single point cloud. 
		If you would like to generate more point clouds, please use the command line functionality

	We have also included a set of rectified stereo pairs to be used if you would like to sample the product.
		These are located in the "samples" folder.
		These images are from www.cvlibs.net/datasets/karlsruhe_sequences

*************************
* What is the Algorithm *
*************************
	For help understanding the linear algebra behind generating the point cloud, please read the "Stereovision Tutorial" file.

**************************
* How to Use the Product *
**************************
	For help using the product, please read the "Tutorial.txt" file

****************
* Dependencies *
****************
	This project requires that you have installed:
		-Python 3
		-CMake
		-OpenCV
		-Point Cloud Library

*****************
* How to Extend *
*****************
	To extend the product:
		Step 1). Locate the library.C file in the AutoPC folder

		Step 2). Open library.C with the text editor of your choice

		Step 3). Create the function that you would like to add
			Please note: To recieve input from terminal your function should take in argc and argv

		Step 4). Navigate to the main function and follow the example code to be able to call your new function from the main function
			Please note: We use a single character to call functions.
				When you are adding your function call to main, make sure you do not collide with the other characters used to call other functions.
		Step 5). Save the library.C file and exit

		Step 6). Recompile using:
			-cmake .
			-make
	
	You can now call your function using ./library <your_function> <parameters>

	To extend the GUI:
		Please note: This should be done after adding your new function and recompiling library.

		Step 1). Locate the GUI.py file in the AutoPC folder

		Step 2). Open GUI.py with the text editor of your choice

		Step 3). Follow the example at the bottom of the file to:
			-Create a new button in the GUI that will be used to call your function
			-Add any extra input boxes to your function
			-Create a function that will be called when your button is pressed

		Step 4). Save the GUI.py file and exit

	You have now extended the GUI to be able to use your new function
