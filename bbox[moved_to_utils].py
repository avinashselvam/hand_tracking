import numpy as np

def get_bbox(box):
    a, b, c, d = box
    
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
