#include <assert.h>
#include <iostream>
#include <pcl/visualization/pcl_visualizer.h>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <pcl/common/common_headers.h>
#include <pcl/features/normal_3d.h>
#include <iostream>
#include <pcl/visualization/pcl_visualizer.h>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "elas.h"
#include "image.h"
#include <pcl/console/parse.h>

#include <boost/thread/thread.hpp>\



using namespace cv;
using namespace std;
int populate(int argc, char **argv){
    if(argc < 8){
		fprintf(stderr, "Enter all required parameters in order: Focal Length, Baseline, Principle point x, Principle Point y\n");
		return 0;
	}
//Read in images from command line
    cv::Mat input = cv::imread(argv[2]);
	cv::Mat disp = cv::imread(argv[3], CV_LOAD_IMAGE_GRAYSCALE);
//Initialize point cloud
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr pc(new pcl::PointCloud<pcl::PointXYZRGB>);
//Read in arguments from command line
    double focal = atof(argv[4]); //Focal length of camera
    double baseline = atof(argv[5]); //Baseline of camera
    double x0 = atof(argv[6]); //Principle point x of camera
    double y0 = atof(argv[7]); //Principle point y of camera
    for(double R = 0; R< input.rows; R++){
		for(double C = 0; C < input.cols; C++)
		{
			double d = disp.at<uchar>(R, C);
			pcl::PointXYZRGB p;
                        if ( d < 3)
								//3 is a magic number
								//We chose this number as it creates the best result when visualizing the point cloud
								//This number determines how much a pixel must have moved between the stereo pair to be included in the point cloud, and reduces noise
                            continue;
                        p.x = (-1*(C - x0)*baseline/ d);
			p.y = (-1*(R - y0)*baseline/d);
			
			p.z = (focal *baseline /d) - 1500;
				//1500 is a magic number
				//We chose this number as it creates the best results when visualizing the point cloud
				//This number makes the z axis component of each pixel 1500 units closer to the origin of the visualizer
            cv::Vec3b bgr(input.at<cv::Vec3b>(R, C));
			p.r = bgr[2];
			p.g = bgr[1];
			p.b = bgr[0];
			pc->push_back(p);
		}
	}

	pcl::io::savePCDFileASCII("point_cloud.pcd", *pc);

return 0;
}

void process (const char* file_1,const char* file_2) {
/*
Copyright 2011. All rights reserved.
Institute of Measurement and Control Systems
Karlsruhe Institute of Technology, Germany

This file is part of libelas.
Authors: Andreas Geiger

libelas is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation; either version 3 of the License, or any later version.

libelas is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
libelas; if not, write to the Free Software Foundation, Inc., 51 Franklin
Street, Fifth Floor, Boston, MA 02110-1301, USA 
*/
  cout << "Processing: " << file_1 << ", " << file_2 << endl;

  // load images
  image<uchar> *I1,*I2;
  I1 = loadPGM(file_1);
  I2 = loadPGM(file_2);

  // check for correct size
  if (I1->width()<=0 || I1->height() <=0 || I2->width()<=0 || I2->height() <=0 ||
      I1->width()!=I2->width() || I1->height()!=I2->height()) {
    cout << "ERROR: Images must be of same size, but" << endl;
    cout << "       I1: " << I1->width() <<  " x " << I1->height() << 
                 ", I2: " << I2->width() <<  " x " << I2->height() << endl;
    delete I1;
    delete I2;
    return;    
  }

  // get image width and height
  int32_t width  = I1->width();
  int32_t height = I1->height();

  // allocate memory for disparity images
  const int32_t dims[3] = {width,height,width}; // bytes per line = width
  float* D1_data = (float*)malloc(width*height*sizeof(float));
  float* D2_data = (float*)malloc(width*height*sizeof(float));

  // process
  Elas::parameters param;
  param.postprocess_only_left = false;
  Elas elas(param);
  elas.process(I1->data,I2->data,D1_data,D2_data,dims);

  // find maximum disparity for scaling output disparity images to [0..255]
  float disp_max = 0;
  for (int32_t i=0; i<width*height; i++) {
    if (D1_data[i]>disp_max) disp_max = D1_data[i];
    if (D2_data[i]>disp_max) disp_max = D2_data[i];
  }

  // copy float to uchar
  image<uchar> *D1 = new image<uchar>(width,height);
  image<uchar> *D2 = new image<uchar>(width,height);
  for (int32_t i=0; i<width*height; i++) {
    D1->data[i] = (uint8_t)max(255.0*D1_data[i]/disp_max,0.0);
    D2->data[i] = (uint8_t)max(255.0*D2_data[i]/disp_max,0.0);
  }

  // save disparity images
  char output_1[1024];
  char output_2[1024];
  strncpy(output_1,file_1,strlen(file_1)-4);
  strncpy(output_2,file_2,strlen(file_2)-4);
  output_1[strlen(file_1)-4] = '\0';
  output_2[strlen(file_2)-4] = '\0';
  strcat(output_1,"_disp.pgm");
  strcat(output_2,"_disp.pgm");
  savePGM(D1,output_1);
  savePGM(D2,output_2);

  // free memory
  delete I1;
  delete I2;
  delete D1;
  delete D2;
  free(D1_data);
  free(D2_data);
}

//allows colorized point cloud to be viewed: default PCL function
boost::shared_ptr<pcl::visualization::PCLVisualizer> rgbVis (pcl::PointCloud<pcl::PointXYZRGB>::ConstPtr cloud)
{
  // --------------------------------------------
  // -----Open 3D viewer and add point cloud-----
  // --------------------------------------------
  boost::shared_ptr<pcl::visualization::PCLVisualizer> viewer (new pcl::visualization::PCLVisualizer ("3D Viewer"));
  viewer->setBackgroundColor (0, 0, 0);
  pcl::visualization::PointCloudColorHandlerRGBField<pcl::PointXYZRGB> rgb(cloud);
  viewer->addPointCloud<pcl::PointXYZRGB> (cloud, rgb, "sample cloud");
  viewer->setPointCloudRenderingProperties (pcl::visualization::PCL_VISUALIZER_POINT_SIZE, 3, "sample cloud");
  viewer->addCoordinateSystem (1.0);
  viewer->initCameraParameters ();
  return (viewer);
}


//checks to see if keyboard was clicked: default PCL function
unsigned int text_id = 0;
void keyboardEventOccurred (const pcl::visualization::KeyboardEvent &event,
                            void* viewer_void)
{
  boost::shared_ptr<pcl::visualization::PCLVisualizer> viewer = *static_cast<boost::shared_ptr<pcl::visualization::PCLVisualizer> *> (viewer_void);
  if (event.getKeySym () == "r" && event.keyDown ())
  {
    std::cout << "r was pressed => removing all text" << std::endl;

    char str[512];
    for (unsigned int i = 0; i < text_id; ++i)
    {
      sprintf (str, "text#%03d", i);
      viewer->removeShape (str);
    }
    text_id = 0;
  }
}
//checks to see if mouse was clicked: default PCL function
void mouseEventOccurred (const pcl::visualization::MouseEvent &event,
                         void* viewer_void)
{
  boost::shared_ptr<pcl::visualization::PCLVisualizer> viewer = *static_cast<boost::shared_ptr<pcl::visualization::PCLVisualizer> *> (viewer_void);
  if (event.getButton () == pcl::visualization::MouseEvent::LeftButton &&
      event.getType () == pcl::visualization::MouseEvent::MouseButtonRelease)
  {
    std::cout << "Left mouse button released at position (" << event.getX () << ", " << event.getY () << ")" << std::endl;

    char str[512];
    sprintf (str, "text#%03d", text_id ++);
    viewer->addText ("clicked here", event.getX (), event.getY (), str);
  }
}



int main(int argc, char **argv){
    char function = argv[1][0];
/*Example for how to add your function, argument for function cannot begin with p,d, or v
   if (function == 'a'){                  
        yourFunction(argc, argv);
    }
*/
    
   if (function == 'p'){
        populate(argc, argv);
    }

    if (function == 'd'){
        process(argv[2], argv[3]);
    }
    
    if (function == 'v'){
        std::cout << "RGB colour visualisation example\n";


  // ------------------------------------
  // -----Create example point cloud-----
  // ------------------------------------
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr point_cloud_ptr (new pcl::PointCloud<pcl::PointXYZRGB>);
    pcl::io::loadPCDFile (argv[2], *point_cloud_ptr);

  boost::shared_ptr<pcl::visualization::PCLVisualizer> viewer;

    viewer = rgbVis(point_cloud_ptr);

  //--------------------
  // -----Main loop-----
  //--------------------
  while (!viewer->wasStopped ())
  {
    viewer->spinOnce (100);
    boost::this_thread::sleep (boost::posix_time::microseconds (100000));
  }
  }
}

