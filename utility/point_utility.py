import math
import copy
# A class to represent a Point in 2D plane

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
# in P[] of size n
# def bruteForce(P):
#     n = len(P)
#     R = []
#     for k in range(int(n/2)):
#         min_val = float('inf')
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if dist(P[i], P[j]) < min_val:
#                     min_val = dist(P[i], P[j])
#                     t1 = P[i]
#                     t2 = P[j]
#         P.remove(t1)
#         P.remove(t2)
#         t = (t1,t2)
#         R.append(t)
#         n = n-2
#
#
#     return R

# A Brute Force method to return the
# smallest distance between two points
# in different point lists
def bruteForce(P1, P2, n1, n2):
    R = []
    if(n1<n2):
        n = n1
        x = n2
        ex = n2-n1
    else:
        n = n2
        x = n1
        ex = n1-n2
    for k in range(n):
        min_val = float('inf')
        for i in range(n):
            for j in range(x):
                if dist(P1[i], P2[j]) < min_val:
                    min_val = dist(T1[i], T2[j])
                    t1 = P1[i]
                    t2 = P2[j]
        P1.remove(t1)
        P2.remove(t2)
        t = (t1,t2)
        R.append(t)
        n = n-1
        x = x-1
    return R
