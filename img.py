import cv2
import numpy

mapper_ = ['.', '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+', '_', '-', '?', ']', '1', ')', '(', '|', '\\', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']

def mapper(e):
    return mapper_[e]

def equalize(img, dSize):
    '''
    trans BGR to gray and to given size and do equalization
    '''

    # 将BGR转为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 调整分辨率为字符画的大小
    img_gray = cv2.resize(img_gray, dsize = dSize)

    # 直方图均衡化
    img_equ = cv2.equalizeHist(img_gray)

    # 映射为字符表
    img_equ = img_equ//4
    v_mapper = numpy.vectorize(mapper)
    chars = v_mapper(img_equ)
    return chars

def draw_chars(chars):
    img_new = numpy.full([1080,1920,3], 0, dtype=numpy.uint8)
    h, w = chars.shape
    font_h = 1080//h
    font_w = 1920//w
    for i in range(h):
        for j in range(w):
            cv2.putText(img_new, chars[i,j], (j*font_w, (i+1)*font_h), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(255,255,255))
    return img_new
        


if __name__ == "__main__":
    src = cv2.imread("./test.jpg")
    tar = equalize(src, (192, 108))
    # print(str(tar))
    img = draw_chars(tar)
    cv2.imshow("test", img)
    cv2.waitKey(0)