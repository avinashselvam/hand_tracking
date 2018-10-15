import os
import cv2
import numpy as np
from scipy.io import loadmat

"""
x - contains image data (not used in code yet)
y - contains label data
y.shape = [len of array, num of hands, 4 pts, x,y of each pt]
"""

def read_from_dir(PATH):
    
    x, y = [], []

    # PATH = "./test_dataset/test_data/"
    list_of_imgs = os.listdir(PATH + "images")

    for image in list_of_imgs:
        if image[-3:] != "jpg": continue
        
        img = cv2.imread(PATH+"images/"+image)
        mat = loadmat(PATH+"annotations/"+image[:-3]+"mat")
        
        hands_in_img = []
        
        for hand in mat["boxes"][0]:
            a = hand[0,0][0][0]
            b = hand[0,0][1][0]
            c = hand[0,0][2][0]
            d = hand[0,0][3][0]
            coords = [a, b, c, d]
            hands_in_img.append(coords)
        hands_in_img = np.array(hands_in_img)
        y.append(hands_in_img)

    y = np.array(y)
    return y