#include <assert.h>
#include <iostream>
#include <pcl/visualization/cloud_viewer.h>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <stdio.h>
#include <stdlib.h>
#include <pcl/common/common_headers.h>
#include <pcl/features/normal_3d.h>
#include <iostream>
#include <pcl/visualization/pcl_visualizer.h>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
using namespace std;
int main(int argc, char **argv){
	cv::Mat input = cv::imread(argv[1]);
	cv::Mat disp = cv::imread(argv[2], CV_LOAD_IMAGE_GRAYSCALE);
	pcl::PointCloud<pcl::PointXYZRGB>::Ptr pc(new pcl::PointCloud<pcl::PointXYZRGB>);

	if(argc < 7){
		fprintf(stderr, "Enter all required parameters in order: Focal Length, Baseline, Principle point x, Principle Point y\n");
		return 0;
	}
	
	double focal;
        double baseline;
        double cu;
        double cv;
	focal = atof(argv[3]);
	baseline = atof(argv[4]);
	cu = atof(argv[5]);
	cv = atof(argv[6]);
        for(double R = 0; R< input.rows; R++){
		for(double C = 0; C < input.cols; C++)
		{
			double d = disp.at<uchar>(R, C);
			//cout << d << endl;
                        //if(d < 100) continue;
			pcl::PointXYZRGB p;
                        if ( d < 3)
                            continue;
                        p.x = (-1*(C - cu )*baseline/ d);
			p.y = (-1*(R - cv)*baseline/d);
                        //cout << 'x'<< p.x << endl;
                        //cout << 'y' << p.y << endl;
			//p.z =  ((954.48426 +  1839.23599)/2) * 50/d; //25
			
			p.z = (focal *baseline /d) - 1500;
                        //cout << focal * baseline /d << endl; 
                        cv::Vec3b bgr(input.at<cv::Vec3b>(R, C));
			p.r = bgr[2];
			p.g = bgr[1];
			p.b = bgr[0];
			pc->push_back(p);
		}
	}

	pcl::io::savePCDFileASCII("point_cloud.pcd", *pc);
  return (0);
}
