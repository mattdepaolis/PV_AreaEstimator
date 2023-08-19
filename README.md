# PV_AreaEstimator
This script is designed to perform the detection and segmentation of photovoltaic installations in aerial images using trained YOLOv8 models to estimate the surface area of the detected photovoltaic installations. The training and validation set have been created using aerial images of the Canton of Zurich, Switzerland.

## How to Use
```
git clone https://github.com/mattdepaolis/PV_AreaEstimator.git
cd PV_AreaEstimator
```

Then download the folders containing the pre-trained classification model and segmentation model for the photovoltaic installation detection and segmentation task and move them to the folder PV_AreaEstimator.

YOLOv8 [detection model](https://drive.google.com/drive/folders/1UqNQo_xdwcFoGRyhjUd2u7WKBXekeez9?usp=drive_link)

YOLOv8 [segmentation model](https://drive.google.com/drive/folders/1oAWPxvSTWwVshLgfIpz4gQoA-hhGQg6G?usp=drive_link)
<br>
<br>
Install the required packages:
```
pip install -r requirements.txt
```

Command Line Execution:
```
python _PV_AreaEstimator.py --folder-path <path_to_images> --detection-model <path_to_detection_model> --segmentation-model <path_to_segmentation_model> [optional arguments]
```
Arguments:<br>
--folder-path: Path to the folder containing the aerial images for processing.<br>
--detection-model: Path to the trained detection YOLO model.<br>
--segmentation-model: Path to the trained segmentation YOLO model.<br>
--confidence-detection: Confidence threshold for the detection model (default: 0.1).<br>
--confidence-segmentation: Confidence threshold for the segmentation model (default: 0.25).<br>
--img-size: Size for image resizing (default: 640).<br>
--tilt-angle: Tilt angle of the photovoltaic installation in degrees (default: 30).<br>

Since the image was taken from a bird's eye view, it is necessary to specify the tilt angle of the installation to calculate the area of the solar installation. 
If the tilt angle is unknown, a tilt angle of 30 degrees is assumed. This corresponds to the optimal tilt angle based on the latitude of the given location. In the presented case it is 30 degrees. 

## Data
The training and validation sets used were created based on orthophotos of the Canton of Zurich and are available for download for further research at the following links:

[Training and Validation Set for PV Detection](https://drive.google.com/drive/folders/1_op6JCrr5PtL0Z6r1h6oUpVMOU_s6ewo?usp=drive_link)<br>
[Training and Validation Set for PV Segmentation](https://drive.google.com/drive/folders/1NDOf54O5t8VD2k37Nl_63CzUlY4-2kPc?usp=drive_link) 


## Output
The script will visualize the aerial images, the prediction masks, and the estimated photovoltaic installation surface areas in square meters for each image.<br>

Left: Original image. Center: YOLOv8 output. Right: Surface area estimation

![image](https://github.com/mattdepaolis/PV_AreaEstimator/assets/94449396/de828a4d-ed23-4b2f-abfa-dfb006fe6164)

![image](https://github.com/mattdepaolis/PV_AreaEstimator/assets/94449396/8039d6f1-1e2a-4ff7-9eeb-2ad9a6294bd2)

![image](https://github.com/mattdepaolis/PV_AreaEstimator/assets/94449396/2de913b2-1a8b-425b-a054-553cb2c0eb60)



