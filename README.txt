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

*****************
* How to Extend *
*****************
	To extend the product:
		Step 1). Locate the library.C file in the AutoPC folder

		Step 2). Open library.C with the text editor of your choice

		Step 3). Create the function that you would like to add

		Step 4). Navigate to the main function and follow the example code to be able to call your new function from the main function

		Step 5). Recompile using:
			-cmake .
			-make
	
	You can now call your function using ./library <your_function> <parameters>


****************
* Dependencies *
****************
	This project requires that you have installed:
		-Python 3
		-CMake
		-OpenCV
		-Point Cloud Library
