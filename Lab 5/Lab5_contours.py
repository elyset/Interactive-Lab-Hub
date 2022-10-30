'''
Based on:  https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.h$

Edited by : David Goedicke

'''

#Editied again by Elyse Toder

import numpy as np
import cv2
import sys

img=None
webCam = False
if(len(sys.argv)>1):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      print("Please screenshot the contour that you would like to draw")
      print("Press q to quit")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      img = cv2.imread("../data/test.jpg")
      print("Using default image.")

while(True):

   if webCam:
      ret, img = cap.read()

   imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   ret,thresh = cv2.threshold(imgray,127,255,0)

   contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   img_c = cv2.drawContours(img, contours, -1, (0,255,0), 3)

 #define the screen resulation
   screen_res = 500, 500
   scale_width = screen_res[0] / img.shape[1]
   scale_height = screen_res[1] / img.shape[0]
   scale = min(scale_width, scale_height)
    #resized window width and height
   window_width = int(img.shape[1] * scale)
   window_height = int(img.shape[0] * scale)
    #cv2.WINDOW_NORMAL makes the output window resizealbe
   cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
    #resize the window according to the screen resolution
   #cv2.resizeWindow('Resized Window', window_width, window_height)

   if webCam:
      cv2.resizeWindow('Resized Window', window_width, window_height)     
      #cv2.resize(img_c, (960,540))
      
      cv2.imshow('Resized Window',img_c)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         cap.release()
         break
   else:
      break


#cv2.imshow('Resized Window', img_c)
cv2.imwrite('contour_out.jpg',img_c)
cv2.destroyAllWindows()
