# Import required packages 
import cv2 
import pytesseract 
import matplotlib.pyplot as plt
  
# Read image from which text needs to be extracted 
# img = cv2.imread("image_cap/36.jpg")

def feedback(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    img =img[400:,:,:]
    # Convert the image to gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # Performing OTSU threshold 
    ret, thresh1 = cv2.threshold(gray, 250, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 

    # Appplying dilation on the threshold image 
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 

    # Finding contours 
    _,contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 
    # Creating a copy of image 
    im2 = img.copy() 
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt) 
        res = w*h
        # Drawing a rectangle on copied image 
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        # Cropping the text block for giving input to OCR 
        cropped = im2[y:y + h, x:x + w] 
        # Apply OCR on the cropped image 
        text = pytesseract.image_to_string(cropped) 
        if len(text.strip())>3:
            if 'P' in (text.strip()):
                val = 0
            else:
                try:
                    val = float(text.strip())
                except:
                    val = 280
    try:
        print('current game experiment loss is {}'.format(100-val))
    except:
        val =200
        print('current game experiment loss is {}'.format(100-val))
    return(val)