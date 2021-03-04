import math
import copy
import numpy as np
import cv2
# A class to represent a Point in 2D plane

c = [(255,0,0),(0,255,0),(0,0,255),(255,255,255),(0,0,0),(255,255,0),(255,0,255)]

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# A utility function to find the
# distance between two points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))

# A Brute Force method to return the
# smallest distance between two points
# in different point lists
def bruteForce(P1, P2, n1, n2, h, h_inv, court):
    R = []
    T = []
    P1, P2 = imagePlane(P1, P2, n1, n2, h)
    if(n1<n2):
        n = n1
        x = n2
        T1 = P1
        T2 = P2
        ex = n2-n1
    else:
        n = n2
        x = n1
        T1 = P2
        T2 = P1
        ex = n1-n2
    for k in range(n):
        min_val = float('inf')
        for i in range(n):
            for j in range(x):
                if dist(T1[i], T2[j]) < min_val:
                    min_val = dist(T1[i], T2[j])
                    t1 = T1[i]
                    t2 = T2[j]
        T1.remove(t1)
        T2.remove(t2)
        t = (t1,t2)
        R.append(t)
        n = n-1
        x = x-1
    for i,t in enumerate(R):
        court = cv2.circle(court, (t[0].x, t[0].y), 3, c[i], -1)
        court = cv2.circle(court, (t[1].x, t[1].y), 3, c[i], -1)
    for i,t in enumerate(R):
        p1 = np.float32([[[t[0].x,t[0].y]]])
        p2 = np.float32([[[t[1].x,t[1].y]]])
        detransformed1 = cv2.perspectiveTransform(p1, h_inv)
        detransformed2 = cv2.perspectiveTransform(p2, h_inv)
        t1 = Point(np.round(detransformed1[0][0][0]).astype(int), np.round(detransformed1[0][0][1]).astype(int))
        t2 = Point(np.round(detransformed2[0][0][0]).astype(int), np.round(detransformed2[0][0][1]).astype(int))
        tot = (t1,t2)
        T.append(tot)
    return T, court

# project points onto homography
def WarpPoint(point,homography):
    """
    -point = (x,y)
    """
    point = np.array(point)
    x,y = point[:2].reshape(-1)
    p_homogenous_src = np.array([x,y,1.0])
    p_homogenous_dst = homography.dot(p_homogenous_src)
    p_cartesian_dst = p_homogenous_dst[:2]/p_homogenous_dst[-1]
    point_dst = tuple( np.round(p_cartesian_dst).astype(int) )

    return point_dst

def imagePlane(P1, P2, n1, n2, homography):
    T1 = []
    T2 = []
    for i in range(n1):
        p = P1[i]
        points = np.float32([[[p.x,p.y]]])
        transformed = cv2.perspectiveTransform(points, homography)
        temp = Point(transformed[0][0][0], transformed[0][0][1])
        T1.append(temp)
    for i in range(n2):
        p = P2[i]
        points = np.float32([[[p.x,p.y]]])
        transformed = cv2.perspectiveTransform(points, homography)
        temp = Point(transformed[0][0][0], transformed[0][0][1])
        T2.append(temp)

    return T1, T2
