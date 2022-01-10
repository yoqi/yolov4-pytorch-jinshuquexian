'''
predict.py有几个注意点
1、无法进行批量预测，如果想要批量预测，可以利用os.listdir()遍历文件夹，利用Image.open打开图片文件进行预测。
2、如果想要保存，利用r_image.save("img.jpg")即可保存。
3、如果想要获得框的坐标，可以进入detect_image函数，读取top,left,bottom,right这四个值。
4、如果想要截取下目标，可以利用获取到的top,left,bottom,right这四个值在原图上利用矩阵的方式进行截取。
'''
from PIL import Image
import os
from yolo import YOLO

yolo = YOLO()

path = 'img/101/'  # 原始图片位置
newpath = 'img/301/'  # 保存图片位置
c = 1 # 从1359开始
filelists = os.listdir(path)
for line in filelists:
    img = Image.open(path + '/' + line)
    try:
        #image = Image.open(img)
        image = Image.open(path + '/' + line)
    except:
        print('Open Error! Try again!')
        continue
    else:
        a = "0" * (5 - len(str(c)))  # 6 是命名的位数,可以修改
        out = a + str(c) + '.jpg'
        r_image = yolo.detect_image(image)
        r_image.save(newpath + out)
        c += 1
       # r_image.show()
