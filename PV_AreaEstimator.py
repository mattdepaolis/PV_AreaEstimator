import os
import glob
import torch
import argparse
import numpy as np
from math import exp, cos, radians
from PIL import Image
import torchvision.transforms as T
import matplotlib.pyplot as plt
from ultralytics import YOLO

def load_model(model_path):
    """Function to load YOLO model."""
    return YOLO(model_path)

def perform_prediction(model, img, confidence):
    """Function for prediction with the YOLO model."""
    return model.predict(img, save=True, imgsz=args.img_size, conf=confidence, verbose=False, save_txt=True,
                         show_labels=True, show_conf=True, save_conf=True, save_crop=True)

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Photovoltaic Installation Detection and Segmentation")
    parser.add_argument('--folder-path', required=True, help="Folder containing images for processing")
    parser.add_argument('--detection-model', required=True, help="Path to the trained detection model")
    parser.add_argument('--segmentation-model', required=True, help="Path to the trained segmentation model")
    parser.add_argument('--confidence-detection', type=float, default=0.1,
                        help="Confidence threshold for detection model")
    parser.add_argument('--confidence-segmentation', type=float, default=0.25,
                        help="Confidence threshold for segmentation model")
    parser.add_argument('--img-size', type=int, default=640, help="Size for image resizing")
    parser.add_argument('--tilt-angle', type=int, default=30, help="Tilt angle of the photovoltaic installation in degrees")
    return parser.parse_args()


def calculate_photovoltaic_installation_surface(mask, tilt_angle, IMG_SIZE):
    """Function to calculate photovoltaic installation surface aere in square meters."""
    number_of_ones = torch.sum(mask != 0).item()
    total_coverage_px = number_of_ones * exp(1250 / IMG_SIZE)
    total_coverage_sq_cm = total_coverage_px * 5
    total_coverage_sq_m = total_coverage_sq_cm / 10000  # projected area
    real_area_sq_m = total_coverage_sq_m / cos(radians(tilt_angle))  # actual area
    return real_area_sq_m

def show_data(mask, image, sqrm, IMG_SIZE):
    """Function to display the image, mask and photovoltaic installation surface area."""
    with Image.open(image) as im:
        im.thumbnail((IMG_SIZE,IMG_SIZE), resample=Image.LANCZOS)
    mask_max = torch.max(mask, dim=0)[0]
    mask_image = T.ToPILImage()(mask_max)
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].imshow(im)
    axs[0].set_title('Aerial Image')
    axs[0].axis('off')
    axs[1].imshow(mask_image, cmap='gray')
    axs[1].set_title('Prediction')
    axs[1].axis('off')
    axs[2].text(0.5, 0.5, r'Total estimated photovoltaic installation surface area: '
                + '\n' + r'$\bf{' + f'{sqrm:.2f}' + '}$' + ' square meters',
                horizontalalignment='center', verticalalignment='center',
                fontsize=12, transform=axs[2].transAxes)
    axs[2].axis('off')
    plt.show()

def main(args):
    detection_model = load_model(args.detection_model)
    segmentation_model = load_model(args.segmentation_model)
    IMG_SIZE = args.img_size

    image_paths = glob.glob(os.path.join(args.folder_path, "*.jpg"))
    if not image_paths:
        print("No images found in provided folder.")
        return

    print(f"Found {len(image_paths)} images. Starting detection process...")
    results = [perform_prediction(detection_model, img, args.confidence_detection) for img in image_paths]

    result = results[0][0]
    image_paths = [os.path.join(args.folder_path, f'{x[:-3]}jpg') for x in os.listdir(
        os.path.join('/', result.save_dir, 'labels'))]

    print('Starting semantic segmentation...')
    for img in image_paths:
        perform_prediction(segmentation_model, img, args.confidence_segmentation)

    results = list(segmentation_model(image_paths, conf=args.confidence_segmentation))

    for result, img in zip(results, image_paths):
        if result.masks is not None:
            sqrm = calculate_photovoltaic_installation_surface(result.masks.data, args.tilt_angle, IMG_SIZE)
            show_data(result.masks.data, img, sqrm, IMG_SIZE)
        else:
            print(f"No masks found for image: {img}")


if __name__ == "__main__":
    args = parse_args()
    main(args)