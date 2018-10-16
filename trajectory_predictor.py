import numpy as np

"""
d - array of (x,y) coordinates of temporal windows
v - array of (vx, vy) velocities of window centers
a - array of (ax, ay) accelerations of window centers
j - array of (jx, jy) jerks of window centers
"""

def get_search_space(d):
    # get R from d and find maximum enclosing rect
    # not sure how to do
    return ss

def estimate_d(d, v, a, j):
    
    # we don't divide my dt because
    # when using the values we are going to multiply by dt again

    if len(d) > 1:
        velocity = d[-1] - d[-2]
        v.append(velocity)
        if len(v) > 1:
            acceleration = v[-1] - v[-2]
            a.append(acceleration)
            if len(a) > 1:
                jerk = a[-1] - a[-2]
                j.append(jerk)
                
                a_new = a[-1] + j[-1]
            v_new = v[-1] + a_new
        d_new = d[-1] + v_new

    return d_new