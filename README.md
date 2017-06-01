# AutoPC
Automated Stereo Depth Visualization

About Our Product:
Our product is a library that can be accessed through UNIX or our GUI to generate and visualize point clouds. 
It can take two rectified stereo images and create a disparity map of them. This map can then be used to generate a point cloud.
Our software also allows the user to visualize this point cloud. 

What Our Product Requires:
The user needs to have rectified images, meaning that the images were taken along the same camera plane. Images from a stereo camera are rectified. 
The images need to be in a .pgm (grayscale) format, websites like convertio.co can do this conversion for free. 
They also need to know the focal length and coordinates of the principle point of the camera, as well as the distance between where the images were taken (baseline).
A user can automatically get these parameters from a calibration of a stereo camera. 

What Our Product is Not:
Our product cannot take a collection of unrectified images and reconstruct the space. 
That is structure from motion, not stereovision, and other software handles that topic, like Photoscan. 
Our product also cannot rectify images, or calibrate a camera to obtain camera feature paramaters. 



