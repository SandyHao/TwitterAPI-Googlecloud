import os,sys,ffmpeg
os.system("ffmpeg -r 1 -f image2 -i %3d.jpg -s 1200x800 models.mp4")
#"-r 1" one frames per second
#"-f image2" the format 
#"%3d" ex.003
#"-s 1200x800" size of the video 
