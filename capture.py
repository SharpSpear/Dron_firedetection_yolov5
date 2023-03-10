# import pyautogui
# import numpy as np
# import cv2
# import time

# # Obtaining the screen height and width
# screenWidth, screenHeight = pyautogui.size()
# screen_size = (screenWidth, screenHeight)
# print(screen_size)

from PIL import ImageGrab
import cv2
import numpy as np
img = ImageGrab.grab()
width, height = img.size
while True:
    screen = np.array(ImageGrab.grab(bbox=(0,0,width/2,height)))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    cv2.imshow('Python Window', screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break