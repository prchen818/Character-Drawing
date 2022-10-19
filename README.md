# Character Drawing

## Version

### v1.2 
updated in 10.19.2022

## Introduction

这个程序实现了将一个视频转化为字符画

### Summary

通过OpenCV将视频转化为.jpg格式的帧，通过Pillow将原视频帧转为字符画，再通过OpenCV将帧合成为视频

## Requirements
- python 3.9
- opencv-python 4.6.0

## Update Logs
### v1.2 10.19.2022
- 进一步重构了代码，删去了video模块
- 代码逻辑优化，现在逐帧读取，并立即处理，不再使用jpg缓存
- 将一些配置单独抽出到config.py
- 处理速度相较v1.0提升大约20%，主要来自减少I/O和编解码时间

### v1.1 10.18.2022
- 帧转为字符画前进行直方图均衡化处理，提高对比度，优化观感
- 放弃使用Pillow库，转而完全使用OpenCV进行处理
- 对代码进行了部分模块化重构，将视频处理及帧处理函数单独抽象成模块
- 转换后的字符画帧不再开文件夹缓存，硬盘空间需求减半