import cv2                                                                                                                                                               
import os, sys                                                                                                                                                           
import numpy as np                                                                                                                                                       
                                                                                                                                                                         
                                                                                                                                                                         
v_cap = cv2.VideoCapture(sys.argv[1])                                                                                                                                    
v_len = int(v_cap.get(cv2.CAP_PROP_FRAME_COUNT))                                                                                                                         
for i in range(v_len):                                                                                                                                                   
    ret, frame = v_cap.read()                                                                                                                                            
    th = cv2.inRange(frame, (9, 13, 104), (98, 143, 255))                                                                                                                
    points = np.where(th>0)                                                                                                                                              
    p2 = zip(points[0], points[1])                                                                                                                                       
    p2 = [p for p in p2]                                                                                                                                                 
    rect = cv2.boundingRect(np.float32(p2))                                                                                                                              
    cv2.rectangle(th, (rect[1], rect[0]), (rect[1]+rect[3], rect[0]+rect[2]), 255)                                                                                       
    cv2.imshow("t", th)                                                                                                                                                  
    cv2.waitKey(10)
