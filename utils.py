from __future__ import division
import numpy as np

"""
Converts a bounding box label
x - x coordinate of bbox center
y - x coordinate of bbox center
w - width of bbox
h - height of bbox
grid - the 2D cross section of the final layer of YOLOv2
resolution - the networks input image dimensions
"""

def convert_to_yolo_output(x, y, w, h, grid=(60, 33), resolution=(1920, 1056)):
    
    yolo_output = np.zeros((grid[0], grid[1], 10))
    
    # deciding which anchor
    aspect_ratio = w/h
    if aspect_ratio <= 1: anchor = 0
    else: anchor = 1
    
    # deciding which cell
    num_pixels_per_col = resolution[0] / grid[0]
    num_pixels_per_row = resolution[1] / grid[1]

    row = int(y / num_pixels_per_row)
    col = int(x / num_pixels_per_col)
    
    if anchor == 0: yolo_output[row, col, 0:5] = [x, y, w, h, 1]
    elif anchor == 1: yolo_output[row, col, 5:] = [x, y, w, h, 1]

    return yolo_output
    
    

    