#应用ffmpeg
import os,numpy,sys
#将图片化成同一尺寸
os.system("ffmpeg -f image2 -framerate 12 -i foo-%03d.jpeg -s WxH foo.avi")



#应用openCV
import cv2
import glob

fps = 10

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter('saveVideo.avi', fourcc, fps, (480, 360))  # the last parameters are size of the picture
imgs = glob.glob('D:/experiment/ViBE/image_to_video/val/*.png')
for imgname in imgs:
    frame = cv2.imread(imgname)
    videoWriter.write(frame)
videoWriter.release()