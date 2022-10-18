import os
import cv2 as cv
import numpy as np

def video2frame(vp, target_dir):
    ''' 
    trans video(.mp4 and so on) frame to image(.jpg and so on)

    :vp: video path
    :target_dir: the frames generated will be put in target_dir
    '''
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)
    vidcap = cv.VideoCapture(vp)
    global fps_
    fps_ = vidcap.get(5)
    success, image = vidcap.read()
    count = 0
    while success:
        count += 1
        print("\rprocessing video2frame now:%d"%count, end='', flush=True)
        cv.imencode('.jpg', image)[1].tofile(target_dir + '%d.jpg'%count)
        success, image = vidcap.read()
    print("\ntotal frame number:%d"%count)
    return fps_

def frame2video(op, source_dir):
    '''
    trans image(.jpg) to video(.avi) frame

    :op: the path of output video
    :source_dir: path of the source frames to make video
    '''
    print("transforming frames to video...")
    frame_list = os.listdir(source_dir)
    frame_list.sort(key=lambda x:int(x.split('.')[0]))
    img_example = cv.imread(source_dir + frame_list[0])
    img_size = img_example.size
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    videoWriter = cv.VideoWriter(op, fourcc, fps_, img_size)
    for i in frame_list:
        path_ = os.path.join(source_dir+i)
        frame = cv.imdecode(np.fromfile(path_, dtype=np.uint8), -1)
        videoWriter.write(frame)
    videoWriter.release()