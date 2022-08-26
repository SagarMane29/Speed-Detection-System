# Speed Detection System

<p align="center">
  <img src="others/thumbnail.jpg" />
</p>

## Why suffer when we can develop a system that can automatically detect overspeeding vehicles

https://user-images.githubusercontent.com/90572543/186978270-a99cfdf3-9df5-420a-87c6-977dbe1a69f4.mp4

## Why do we need a speed detection system ?

Speed control on highways and accident prone areas has been a challenging conundrum for government on a global scale. According to reports there are approximately 4 lakh crashes each year causing upto 1 lakh deaths all over the world. A majority of them are caused by overspeeding vehicles which can be controlled by implementing a proper monitoring system that is able to detect overspeeding vehilces.

## Overview

The idea was to develop a vehicle speed detection system using video streaming. This
system requires a video stream which consists of components like vehicles which are in state
of motion, starting point and ending point. The system is designed to detect and track the
vehicles to calculate the speed of each vehicle. This project is an implementation of Speed
Detection System (SDS) which can be used as an alternative for radar and other existing
systems. SDS uses several image processing techniques on video stream captured from
camera, which makes SDS capable of calculating the speed of moving objects avoiding the
traditional radar problems.

## Methodology

SDS process is divided into four phases; first phase is the object detection in which
the vehicles that are passing through the road would be detected successfully by using image
processing methods. After completion of object detection phase the next step consists of
object tracking in which the detected vehicle having assigned ID is tracked over frames by
using Euclidean distance formula. Finally from distance and traveled time of detected vehicle,
speed of that vehicle is determined by using speed function formula.
Lastly, images of each individual vehicle would be captured and stored in desired
location. At the end, data visualization and file methods would be used to store and represent
all the data that has been collected from object detection, object tracking and speed estimation
phase. 

## Flowchart

<p align="center">
  <img src="others/flowchart.jpeg" />
</p>

## Implementation 

  There are four main stages of implementation:
  - Vehicle detection using image prcessing techniques such as opening, closing and erosion to identify multiple vehicles in the frame.
  - Vehicle tracking using euclidean distance formula to track multiple vehicles across the frame and assign them unique IDs.
  - Speed estimation using speed formula to identify over-speeding vehicles.
  - Data representation for info gathering and visualization.

## Block Diagram 

<p align="center">
  <img src="others/blockdiagram.png" />
</p>

## Software 

- OS Windows 10
- Python Programming Language
- Python Libraries (openCv, matplotlib, numpy, dateandtime etc)

## Requirements 

- Install latest version of python from here: <a href="https://www.python.org/downloads/" target="_blank">Download</a> 📥	

- Install respective python modules by using following commands:

  ```bash
    pip install opencv-python
  ```
  
  ```bash
    pip install matplotlib
  ```
  
  ```bash
    pip install numpy
  ```
  
## Deployment

- To deploy this project create a `SDS` folder :file_folder: inside your `E drive`.

  <img src="others/directorysetup1.PNG" />

- Create a `resources` folder :file_folder: inside `SDS` folder :file_folder: and place `traffic` file 📋 inside. Dwnload traffic.mp4 file from here: <a href="https://drive.google.com/drive/folders/1d22cp2Fw9vk3DxcUdtWovjdlWmGkNiQz?usp=sharing">Download</a> 📥	

  <img src="others/directorysetup2.PNG" />

- Create a `TrafficRecord` folder :file_folder: inside `SDS` folder :file_folder: and create a `exceeded` folder :file_folder: inside it.

  <img src="others/directorysetup3.PNG" />

- This is how your project directory `SDS` :file_folder: must look.
 
  <img src="others/directorysetup4.PNG" />

## Execution

- Run this command in your terminal

  ```bash
    python main.py
  ```

## Results

- ### Vehicle detection and tracking

  <p>
    <img src="others/outputwindow.png" />
  </p>

- ### Storing vehicle images and data

  <p>
    <img src="others/outputdirectory.png" />
  </p>

- ### Data report

  <p>
    <img src="others/outputreport.png" />
  </p>

- ### Graphical representation

  <p>
    <img src="others/outputgraph.png" />
  </p>

## Conclusion

Speed detection system focuses to detect speed of every vehicle and can monitor as
well as reduce the road accidents due to over speeding with proper accuracy and efficiency.
As compared to the existing systems speed detection system is easy to handle with less
physical effort and is completely automated.
Since the cost of this system is many times less than the existing system making it efficicent cost wise. This system also helps to count number of vehicles that pass over the
road so that government gets an idea about the maintenance time period of that road. This video-based speed detection system works as good alternative to the
existing system. It can also be expanded to various fields
of security measures and can be further improved by adding features such as number plate extraction and many more. 

### Thanks For Visiting My Repo :blush:
#### Regards Sagar Mane :heart:
