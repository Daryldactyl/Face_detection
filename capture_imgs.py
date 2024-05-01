import os
import cv2
import uuid
import time

IMAGES_PATH = os.path.join('data', 'images')
number_images = 30

cap = cv2.VideoCapture(0)
for img in range(number_images):
    print(f'Collecting image {img}')
    ret, frame = cap.read()
    imgname = os.path.join(IMAGES_PATH, f'{str(uuid.uuid1())}.jpg')
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    time.sleep(0.5)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()