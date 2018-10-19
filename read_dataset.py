import os
import cv2
import numpy as np
from scipy.io import loadmat
from utils import preprocess, get_bbox, convert_to_yolo_output

"""
x - contains image data
y - contains label data
y.shape = [len of array, num of hands, 4 pts, x,y of each pt]
"""

def read_from_dir(PATH):
    
    x, y = [], []
    # PATH = "./test_dataset/test_data/"
    list_of_imgs = os.listdir(PATH + "images")

    for image in list_of_imgs:
        
        if image[-3:] != "jpg": continue
        
        img = cv2.imread(PATH + "images/" + image)
        img_32x32 = preprocess(img)
        resolution = img_32x32.shape[0:2]
        x.append(img_32x32)

        mat = loadmat(PATH+"annotations/"+image[:-3]+"mat")
        
        bbox_of_all_hands = []
        for hand in mat["boxes"][0]:
            a = hand[0,0][0][0]
            b = hand[0,0][1][0]
            c = hand[0,0][2][0]
            d = hand[0,0][3][0]
            rotated_box_coords = a, b, c, d
            bbox_coords = get_bbox(rotated_box_coords)
            bbox_of_all_hands.append(bbox_coords)
        yolo_op = convert_to_yolo_output(bbox_of_all_hands, resolution)
        y.append(yolo_op)
    
    x = np.array(x)
    y = np.array(y)
    return x, y