This project uses libelas, Point Cloud Library, and OpenCV to create a single program that allows you to generate a disparity image, generate a point cloud from the disparity image, and visualize the point cloud.

For help understanding what stereovision is, our algorithm, and the math behind the alogrithm, please read the "Stereovision Tutorial" file.

For help using our project, please read the "Tutorial" file.

This project comes with a GUI that you can use to create a disparity image, create a point cloud, and to visualize a point cloud.
This project also has the ability to be ran purely from the terminal.
	The reason that this project has both a GUI and the ability to be ran from terminal is so that if you are using a system that does not have the ability to visualize a GUI you are still able to use the project to generate a disparity image and a point cloud.
		It also allows you the possibility to call our project from other files. 

Please note:
	The GUI is best used if you are meaning to generate and visualize a single point cloud. 

Dependencies:
	This project requires that you have installed:
		-Python 3
		-CMake
		-OpenCV
		-Point Cloud Library
