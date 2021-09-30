import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey,W,A,S,D,ReleaseKey
# time.sleep(5)
def roi(img,vertices): ## used to crop the region which is of our interest
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,vertices,255)
    masked = cv2.bitwise_and(img,mask)
    return masked;
def process_img(orignal_image):
    processed_image = cv2.cvtColor(orignal_image,cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image,threshold1=200,threshold2=200)
    possible_vertices = [[3,1072],[666,437],[1279,436],[1911,1075],[1311,1062],[1107,678],[752,672],[506,1052]]
    verticies = np.array(possible_vertices)
    processed_image = roi(processed_image,vertices=[verticies])
    return processed_image;
def main():
    while (True):
        screen = np.array(ImageGrab.grab())
        new_screen = process_img(screen)
        # printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
        # .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
# //starting point
main()