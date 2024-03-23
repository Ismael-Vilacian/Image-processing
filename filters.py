import os
import cv2
import numpy as np

folder = "processed-image"
file_name = 'image-2.png'

def low_pass():
    image = cv2.imread("images\image-1.png")
    filter_low_pass = cv2.blur(image, ksize=(15, 15))

    cv2.imshow("janela", filter_low_pass)
    cv2.imwrite(os.path.join(folder, "low_pass_" + file_name), filter_low_pass)
    cv2.waitKey()

def high_pass():
    image=cv2.imread("images\image-1.png")
    kernel = np.array([[ 0, -1,  0],
                       [-1,  5, -1],
                       [ 0, -2,  1]])
    filter_high_pass = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    
    cv2.imwrite(os.path.join(folder, "high_pass_" + file_name), filter_high_pass)
    cv2.imshow("janela",filter_high_pass)
    cv2.waitKey()
    
high_pass()
low_pass()