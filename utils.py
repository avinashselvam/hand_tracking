from __future__ import division
import numpy as np
import cv2

"""
Converts many bounding box labels
bbox_coords - list of xywh for many hands in the image
x - x coordinate of bbox center
y - x coordinate of bbox center
w - width of bbox
h - height of bbox
grid - the 2D cross section of the final layer of YOLOv2
resolution - the networks input image dimensions
"""

def convert_to_yolo_output(bbox_of_all_hands, resolution=(1920, 1056)):
    
    grid = resolution[0] / 32, resolution[1] / 32
    yolo_output = np.zeros((grid[0], grid[1], 10))
    
    for each_hand in bbox_of_all_hands:
        x, y, w, h = each_hand
        
        # deciding which anchor
        aspect_ratio = w/h
        if aspect_ratio <= 1: anchor = 0
        else: anchor = 1
        
        # deciding which cell
        row = y // 32
        col = x // 32
        
        if anchor == 0: yolo_output[row, col, 0:5] = [x, y, w, h, 1]
        elif anchor == 1: yolo_output[row, col, 5:] = [x, y, w, h, 1]

    return yolo_output

"""
Converts image of any dimension to the nearest mutiple of 32X32
img - input image read as a numpy array
"""

def preprocess(img):
    w, h, _ = img.shape
    nx, ny = w // 32, h // 32
    cx, cy = w // 2, h // 2
    return img[cx - (nx * 16):cx + (nx * 16), cy - (ny * 16):cy + (ny * 16)]
    
"""
Converts a rotated box to a bounding box with edges parallel to images edges
rotated_box - 4 corners of the original box
"""

def get_bbox(rotated_box):
    a, b, c, d = rotated_box
    
    x_min = np.min(a[0], b[0], c[0], d[0])
    x_max = np.max(a[0], b[0], c[0], d[0])
    y_min = np.min(a[1], b[1], c[1], d[1])
    y_max = np.max(a[1], b[1], c[1], d[1])

    x_mid = (x_min + x_max) / 2
    y_mid = (y_min + y_max) / 2
    height = y_max - y_min
    width = x_max - x_min

    bbox = [x_mid, y_mid, width, height]

    return bbox
    
    

    
