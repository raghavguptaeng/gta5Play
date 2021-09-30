import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey,W,A,S,D,ReleaseKey
# time.sleep(5)
def draw_lines(img,lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)
    except:
        pass

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    vertices = np.array([[3,1072],[666,437],[1279,436],[1911,1075],[1311,1062],[1107,678],[752,672],[506,1052]], np.int32)
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)
    # processed_img = roi(processed_img, [vertices])
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180,      20,         15)
    draw_lines(processed_img,lines)
    return processed_img

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