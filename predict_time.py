# from keras.layers import Input
from PIL import Image
from timeit import default_timer as timer
from yolo import YOLO

yolo = YOLO()

while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        start = timer()
        r_image = yolo.detect_image(image)
        end = timer()
        r_image.save("img.jpg")
        r_image.show()
        print("检测时间：",end-start,"s")
yolo.close_session()
