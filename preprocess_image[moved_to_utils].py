import cv2
import numpy as np

def preprocess(img):
    w, h, _ = img.shape
    nx, ny = w // 32, h // 32
    cx, cy = w // 2, h // 2
    return img[cx-(nx*16):cx+(nx*16), cy-(ny*16):cy+(ny*16)]