import sys
import numpy
import math
from MergeByIndex import *

def main():
  with open(sys.argv[1], 'r') as file:
    points = [[int(x) for x in line.split()] for line in file]

  p_x = MergeSort(points, 0)
  p_y = MergeSort(points, 1)

  pair = ClosestPair(p_x, p_y)

  print("Closest pairs are: ")
  print pair


def ClosestPair(p_x, p_y):
  if(len(p_x) == 2):
    return (p_x[0], p_x[1])
  elif(len(p_x) == 3):
    return closestFromThreePairs(p_x)
  
  mid = len(p_x) / 2
  q_x = p_x[0:mid]
  q_y = p_y[0:mid]
  r_x = p_x[mid:len(p_x)]
  r_y = p_y[mid:len(p_y)]

  (p1, q1) = ClosestPair(q_x, q_y)
  (p2, q2) = ClosestPair(r_x, r_y)
  delta = min(dist(p1,q1), dist(p2,q2))
  (p3, q3) = ClosestSplitPair(p_x, p_y, delta)

  return  [(p1,q1),(p2,q2),(p3,q3)][numpy.argmin([dist(p1,q1), dist(p2,q2), dist(p3,q3)])]

def ClosestSplitPair(p_x, p_y, delta):
  mid = len(p_x) / 2
  xbar = p_x[mid-1][0]
  s_y = list()

  for point in p_y:
    if(point[0] <= xbar + delta and point[0] >= xbar - delta):
      s_y.append(point)

  bestdist = delta
  bestpair = (None,None)

  for i in range(len(s_y)):
    for j in range(1,min(7, len(s_y)-i)):
      p = s_y[i]
      q = s_y[i+j]
      if(dist(p,q) < bestdist):
        bestdist = dist(p,q)
        bestpair = (p,q)

  
  return bestpair



def dist(A,B):
  if(A is None and B is None):
    return float("inf")

  total = 0
  for i in range(len(A)):
    total += (A[i] - B[i])**2
  return math.sqrt(total)

def closestFromThreePairs(A):
  bestdist = float("inf")
  for i in range(len(A)):
    for j in range(i+1, len(A)):
      if dist(A[i], A[j]) < bestdist:
        bestdist = dist(A[i], A[j])
        bestpair = (A[i], A[j])

  return bestpair

main()
