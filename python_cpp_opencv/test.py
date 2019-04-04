import cv2
from numpy.ctypeslib import ndpointer
import ctypes
import numpy as np

dll=ctypes.WinDLL('MyDLL.dll') 

def cpp_canny(input):
    if len(img.shape)>=3 and img.shape[-1]>1:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    h,w=gray.shape[0],gray.shape[1] 
    
    # 获取numpy对象的数据指针
    frame_data = np.asarray(gray, dtype=np.uint8)
    frame_data = frame_data.ctypes.data_as(ctypes.c_char_p)  
    
    # 设置输出数据类型为uint8的指针
    dll.cpp_canny.restype = ctypes.POINTER(ctypes.c_uint8)
     
    # 调用dll里的cpp_canny函数
    pointer = dll.cpp_canny(h,w,frame_data)  
     
    # 从指针指向的地址中读取数据，并转为numpy array
    np_canny =  np.array(np.fromiter(pointer, dtype=np.uint8, count=h*w)) 
    
    return pointer,np_canny.reshape((h,w))

img=cv2.imread('input.png')
ptr,canny=cpp_canny(img)
cv2.imshow('canny',canny)
cv2.waitKey(2000)
#将内存释放
dll.release(ptr)