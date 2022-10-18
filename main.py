import os
import cv2
import video
import img

src_video = "./nilou.mp4"
output_video = "./output.avi"
src_f = "./src_f/"
dSize = (240, 135)
img_size = (1920, 1080)

if __name__ == "__main__":
    # fps_ = video.video2frame(src_video, src_f)
    fps_ = 30
    if(os.path.exists(output_video)):
        os.remove(output_video)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoWriter = cv2.VideoWriter(output_video, fourcc, fps_, img_size)
    frame_list = os.listdir(src_f)
    frame_list.sort(key=lambda x:int(x.split('.')[0]))
    for frame in frame_list:
        print("\rprocessing video2frame now:%s"%frame, end='', flush=True)
        src = cv2.imread(src_f + frame)
        chars = img.equalize(src, dSize)
        frame = img.draw_chars(chars)
        videoWriter.write(frame)
    videoWriter.release()
