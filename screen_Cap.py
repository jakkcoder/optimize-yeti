import numpy as np 
from PIL import ImageGrab
import cv2,time
time_start = time.time()
count =0
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,930,590)))
    print('\n',time.time()- time_start,'\n')
    screen = cv2.cvtColor(np.array(screen),cv2.COLOR_BGR2RGB)
    cv2.imshow('window',screen)
    cv2.imwrite(r'C:\Users\BHATTJ\Desktop\Work-bench\you-tube-projects\penguin-game\image_cap'+'/'+str(count)+'.jpg',screen)
    time_start = time.time()
    count+=1
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break