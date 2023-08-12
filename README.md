# PV_AreaEstimator
This script is designed to perform detection and segmentation of photovoltaic installations in aerial images using trained YOLO models to estimate the surface area of the detected photovoltaic installations.

## 1. How to Use:
```
git clone https://github.com/mattdepaolis/PV_AreaEstimator.git
cd PV_AreaEstimator
````

Then download the folders containing the pre-trained classification model and segmentation model for the photovoltaic installation detection and segmentation task and move them to the folder PV_AreaEstimator.

YOLOv8 detection model.:
```
https://drive.google.com/drive/folders/1UqNQo_xdwcFoGRyhjUd2u7WKBXekeez9?usp=drive_link
```

YOLOv8 segmentation model:
```
https://drive.google.com/drive/folders/1oAWPxvSTWwVshLgfIpz4gQoA-hhGQg6G?usp=drive_link
```

Install the required packages:
```
pip install -r requirements.txt
```

## 2. Command Line Execution:
```
python _PV_AreaEstimator.py --folder-path <path_to_images> --detection-model <path_to_detection_model> --segmentation-model <path_to_segmentation_model> [optional arguments]
```
## 3. Arguments:
--folder-path: Path to the folder containing the aerial images for processing.<br>
--detection-model: Path to the trained detection YOLO model.<br>
--segmentation-model: Path to the trained segmentation YOLO model.<br>
--confidence-detection: Confidence threshold for the detection model (default: 0.1).<br>
--confidence-segmentation: Confidence threshold for the segmentation model (default: 0.25).<br>
--img-size: Size for image resizing (default: 640).<br>
--tilt-angle: Tilt angle of the photovoltaic installation in degrees (default: 30).<br>

## 4. Outputs:
The script will visualize the aerial images, the prediction masks, and the estimated photovoltaic installation surface areas in square meters for each image.

## Notes:
Ensure you have the necessary models and input images in place before running the script.
