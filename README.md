![alt full](https://i.ibb.co/WznjX1v/icon2.png)

## Description

It's a Software design with Python for analyzing video, face detection 
and recognition, pedestrian detection, and background video analyzing 
for development of a product for urban
security in zone of high stream of people and controlled
environment.

## Requirements

Are required this libraries in Python 3.7:


- numpy~=1.19.0
- future~=0.18.2
- icrawler~=0.6.3
- opencv-python~=4.2.0.34
- imutils~=0.5.3
- pillow~=7.2.0
- face_recognition_models
- face_recognition
- future~=0.18.2
- os
- cmake
- dlib

## Usage

Use the  [git clone] 

```
git clone https://github.com/AMIRANDA9112/Recognition
```

In the console execute the index

```
python Recognition.py
```
![alt empty](https://i.ibb.co/yQdj2fB/maininterfaz.png)

You can skip the outputs windows with SCAPE key

### Face Detection Module

![alt full](https://i.ibb.co/JjSjVZs/facemodule.png)

You can make analysis in a video .mp4 file, streaming WebCam or IpCam
with simple set of face images in format .png or .jpg

![alt full](https://i.ibb.co/LJvwx5H/imageset.png)


![alt full](https://i.ibb.co/9sStPr4/videofill.png)

You can adjust the quality of analysis video with the detail index
min 1 = 1x100 frames , max 10 = 1x10 frames

how output this return a collage report set, with 24 frames each report
with the face image localized in the frames in the face image directory


![alt full](https://i.ibb.co/7WxJTJ0/videooutput.png)


like this

![alt full](https://i.ibb.co/w6fJS94/analyze.png)


See the progress report in console

![alt](https://i.ibb.co/NLKJ06J/Estatusprogress.png)

For WebCam you'll only need the set face images folder

![alt](https://i.ibb.co/VpVPVhx/webcamface.png)

![alt](https://i.ibb.co/Dz1pwxT/webcamfaceliv.png)

For IpCam you'll need the set face images folder and the correct
Ip for the streaming video, this depend of each camera.

![alt](https://i.ibb.co/NpGpgsC/fillfaceip.png)


You can adjust the Resolution index in the input
process for best performance processing depending
of native processor capability.

![alt](https://i.ibb.co/FY5hwXm/ipfaceoutput.png)

### Pedestrian Detection Module

![alt](https://i.ibb.co/chJYjtc/pedestrianmodule.png)

You can detect pedestrian with WebCam and IpCam, the detail index is for
adjust the sensitive factor depending of resolution input, and perspective
and distance of the square objective, how a street or a indoor space.



![alt](https://i.ibb.co/Js5ds8Z/output2.png)


The model can't be confused by mascots


![alt](https://i.ibb.co/hFBbBP3/mascotprobe.png)

### Background Replacement Module

![alt](https://i.ibb.co/5jrh28f/bgmodule.png)

In a streaming video from a IpCam or WebCam you can replace the background
for a image or a video with this module.

![alt](https://i.ibb.co/PhLjxZR/bgsetfill.png)

Now you can look the video or image that you are select for the background
of video streaming, in the Ip options how in the other modules you can affect
the resolution of input.

![alt](https://i.ibb.co/8NzVPbF/noset.png)

Press the SPACE key for capture the background to replace in streaming video

![alt](https://i.ibb.co/V3PPsyr/set.png)

Now you can look how the perturbing of shadows, and movement and lights changes
make effect in the output video.

![alt](https://i.ibb.co/KsTSJ66/captureset.png)

The algorithm only replace the changes respect to the moment of capture with
the key SPACE, if you like reset, you can use the 'R' key for reset the background
and SPACE for set again.

![alt](https://i.ibb.co/GRr7wmK/ipbgnoset.png)

The IpCam Implementation is very funny

![alt](https://i.ibb.co/vjgMjtx/seresetbg.png)

The quality depend of resolution input, and correct lighting.

![alt](https://i.ibb.co/2Y7nFHK/mayaset.png)


### Tools Module

Here you have two simples tools for have set data for practice

![alt](https://i.ibb.co/rkVBdyd/toolsmodule.png)

- Download Video from Youtube

![alt](https://i.ibb.co/BGtrVpY/dwonloadyout.png)

you only need write the Url of a Youtube video, and the button will redirecting
to a correct page download for mp4 format.

- Search Face

![alt](https://i.ibb.co/qgHztkT/searche-face.png)

You only need write the name of a celebrity or famous person and in way automatic
the going to download the photo face with best match on internet, this option
need the directory of faces in the Face Detection Module.

### Resources


https://github.com/techwithtim/Face-Recognition


https://github.com/FaztWeb/python-tkinter-sqlite-crud


https://github.com/misbah4064/backgroundremoval


https://www.coursera.org/learn/analyzing-video-opencv-numpy




## Credits

Thanks to  HOLBERTON SCHOOL FORMATION

and I can build this project in base to this projects:

https://github.com/techwithtim/Face-Recognition

https://github.com/FaztWeb/python-tkinter-sqlite-crud

https://www.coursera.org/learn/analyzing-video-opencv-numpy


## Author

-   [Andres Miranda ](https://github.com/AMIRANDA9112) - andreselfm@gmail.com
