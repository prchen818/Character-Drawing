import cv2 as cv
import os
import numpy as np
from PIL import Image, ImageFont, ImageDraw

mapper = list('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft\|()1]?-_+~<>i!lI;:,\"^`.')

def myResize(image):
    w, h = image.size
    global t_w, t_h
    t_w = 200
    ratio = t_w/float(w)
    t_h = int(h*ratio)
    return image.resize((t_w, t_h))

def video2frame(vp):
    vidcap = cv.VideoCapture(vp)
    global fps_
    fps_ = vidcap.get(5)
    success, image = vidcap.read()
    count = 0
    while success:
        count += 1
        print("\rprocessing now:%d"%count, end='', flush=True)
        cv.imencode('.jpg', image)[1].tofile('./source_frame/%d.jpg'%count)
        success, image = vidcap.read()
    print("total frame number:%d"%count)

def frame2video():
    dir_path = './target_frame/'
    frame_list = os.listdir(dir_path)
    frame_list.sort(key=lambda x:int(x.split('.')[0]))
    img_example=Image.open(os.path.join(dir_path, frame_list[0]))
    img_size = img_example.size
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    videoWriter = cv.VideoWriter('./test.avi', fourcc, fps_, img_size)
    for i in frame_list:
        p = os.path.join(dir_path+i)
        frame = cv.imdecode(np.fromfile(p, dtype=np.uint8), -1)
        videoWriter.write(frame)
    videoWriter.release()

def img2asiic():
    src_list = os.listdir('./source_frame/')
    count = 0
    src_list.sort(key=lambda x:int(x.split('.')[0]))
    for i in src_list:
        count += 1
        print("\rprocessing now:"+i, end='', flush=True)
        source_img = Image.open(os.path.join('./source_frame/', i))
        new_img = myResize(source_img)
        gray_img = new_img.convert('L')
        pixels = gray_img.getdata()
        # for i in pixels:
        #     print(i, end=' ')
        new_pixels = []
        i = j = 0
        while i<len(pixels):
            while j<t_w:
                new_pixels.append(mapper[int(pixels[i]/4)])
                i+=1
                j+=1
            new_pixels.append('\n')
            j%=t_w
        font = ImageFont.load_default().font
        font_w, font_h = font.getsize(new_pixels[0])
        font_w *= 1.8
        target_img = Image.new("RGB", (int(t_w*font_w), int(t_h*font_h)))
        x = y = 0
        dr = ImageDraw.Draw(target_img)
        for k in new_pixels:
            if(k=='\n'):
                x+=font_h
                y=-font_w
            dr.text((y, x), k)
            y+=font_w
        # target_img.show()
        target_img.save(os.path.join("./target_frame/", "%d.jpg"%count))


if __name__ == "__main__":
    video_path = "./wushu.MP4"
    video2frame(video_path)
    img2asiic()
    frame2video()