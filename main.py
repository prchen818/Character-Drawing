import os
import cv2
import img

from config import *

if __name__ == "__main__":

    # 清除旧的输出视频
    if(os.path.exists(output_video)):
        os.remove(output_video)

    # 读取源视频
    vidcap = cv2.VideoCapture(src_video)
    fps_ = vidcap.get(5)    # 获取帧率

    # 设置输出视频
    fourcc = cv2.VideoWriter_fourcc(*'XVID')    # 输出格式应为avi
    videoWriter = cv2.VideoWriter(output_video, fourcc, fps_, img_size)

    # 逐帧读取，逐帧处理
    success, image = vidcap.read()
    count = 0
    while success:
        count += 1
        print("\rprocessing no.%d frame now"%count, end='', flush=True)
        chars = img.equalize(image, dSize)
        frame = img.draw_chars(chars)
        videoWriter.write(frame)

        success, image = vidcap.read()
    videoWriter.release()

