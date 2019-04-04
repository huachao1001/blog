 
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>                   
#include   <stdlib.h>   
#define DLLEXPORT extern "C" __declspec(dllexport)

using namespace cv;

DLLEXPORT  uchar* cpp_canny(int height, int width, uchar* data) {
	cv::Mat src(height, width, CV_8UC1, data);
	cv::Mat dst; 
	Canny(src, dst, 100, 200);

	uchar* buffer = (uchar*)malloc(sizeof(uchar)*height*width);
	memcpy(buffer, dst.data, height*width);
	return buffer;

}
DLLEXPORT void release(uchar* data) {
	free(data);
}
