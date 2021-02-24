from PIL import ImageGrab
import pyautogui
import time 
import cv2
import numpy as np
from input_feedback import feedback

def run_exp(timedelay):
    time.sleep(2)
    pyautogui.click(x=40,y=50)
    time.sleep(timedelay)
    pyautogui.click(x=282, y=558)
    time.sleep(10)
    img = np.array(ImageGrab.grab(bbox=(0,0,930,590)))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    color1 = (40,40,200) 
    color2 = (255,255,255) 
    boundaries = [([color1[0], color1[1], color1[2]], [color2[0], color2[1], color2[2]])]
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(img, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)
    points = cv2.findNonZero(mask)
    avg = (np.median(points, axis=0)[0]+[18,18]).astype(int)
    ### calling on feedback
    screen = np.array(ImageGrab.grab(bbox=(0,40,930,590)))
    out_y = feedback(screen)
    time.sleep(3)
    pyautogui.moveTo(avg[0],avg[1]) 
    time.sleep(1)
    pyautogui.click(avg[0],avg[1])
    time.sleep(2)
    return(out_y)
    