# midprep-cloudphy

This repo is the codebase for The **Vital Extraction Challenge** from interiit techmeet 11.0.  

## Table of Contents
* [Introduction](#intro)
* [Acknowledgements](#ackn)
* [Tasks](#tasks)
* [Dataset](#dataset)
* [Methodology](#training)
* [Scripts](#run)

## Introduction <a name="intro"></a> 

Cloudphysician is a healthcare company focused on bringing quality critical care within reach of every patient, wherever they may be. Monitoring a patient's vitals, such as heart rate, blood pressure, and oxygen levels can provide valuable information about a patient's overall health and well-being and were the major task of the project. This project was part of the Inter-IIT tech meet held at IIT Kanpur. We needed to extract the above information from the healthcare monitor. We used a series of two YOLO v7 models to segment the monitor screen and also detect and localize the positions of vitals. The models were finetuned manually using the datasets provided in the problem statement. Finally, we attached CRAFT + LSTM-based OCR (EasyOCR) to the pipeline to extract text from the localized vitals. 

## Acknowledgements <a name="ackn"></a> 

This project was made possible with previous contributions referenced below: 
<ol>
  <li> https://github.com/WongKinYiu/yolov7 </li>
  <li> https://github.com/JaidedAI/EasyOCR </li>
</ol>

## Tasks <a name="tasks"></a>

We performed following tasks and also provide the code for the same : 

- [:heavy_check_mark:] [Segmentation : **Yolov7**](/)  
- [:heavy_check_mark:] [Classification : **Yolov7**](/)  
- [:heavy_check_mark:] [OCR : **EasyOCR**](/) 

## Dataset <a name="dataset"></a> 

There were 3 datasets provided during the challenge : 

- **Monitor Segmentation Dataset** - A dataset containing the segmentation boundaries
for the monitors in the image, a total of 2000 images.
- **Classification Dataset** - The monitors present in the images can be grouped into 4
types, based on some screen characteristics. This is a separate dataset with the
monitors classified into those 4 separate types, a total of 250 images per class,
accounting for 1000 images.
- **Unlabelled Dataset** - A total of 7000 unlabelled images.

## Methodology <a name="training"></a> 

The solution consists of three steps: 

<ol> 
<li> Screen Segmentation </li> 
<li> Vital Classification </li>  
<li> Optical Character Recognition (OCR) </li> 
</ol> 

In the screen segmentation step, we used a fine-tuned YOLOv7 model to isolate the region of interest (ROI) containing the vital values from the rest of the image. In the vital classification step, another fine-tuned YOLOv7 model is used to classify the vitals present in the ROI. Finally, for OCR we use EasyOCR to extract the text values of the vitals from the cropped images. The training of the YOLOv7 model involved using the monitor segmentation dataset and the classification dataset, and we chose EasyOCR because of its accuracy and efficiency in pre-processing and post-processing of input and output. 

The advantages of this solution include the fast and efficient processing of images in real-time with YOLOv7, the potential for improved accuracy through fine-tuning on specific datasets, and the robustness of EasyOCR. 

## Scripts <a name="run"></a> 


### Checkpoints 
We provide the weights for the finetuned YOLO model below. 

Checkpoint for screen segmentation :
```
gdown --id 1Ni_w3QCucfHI271ASUjk7k04GZseGJcz
```
Alternatively, the link to the same is given below:
```
https://drive.google.com/file/d/1Ni_w3QCucfHI271ASUjk7k04GZseGJcz/view?usp=sharing
```  
  
  
Checkpoint for vital classification :
```
gdown --id 1qXBtVeOpZjeY-AduqtyTtu22y6RytGeO
```
Alternatively, the link to the same is given below:
```
https://drive.google.com/file/d/1qXBtVeOpZjeY-AduqtyTtu22y6RytGeO/view?usp=sharing
```

### Inference 

We provide the notebook and functions for final inference in [this](/run.ipynb) notebook. 
