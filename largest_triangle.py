import math
import itertools


def raw_input():
  return '-21,59,-93 -4,91,-2 1,61,2, 0,44,1'




def get_size(point_a, point_b):
  a_x,a_y,a_z = point_a
  b_x,b_y,b_z = point_b

  x = a_x + b_x
  y = a_y + b_y
  z = a_z + b_z

  s = (x + y + z)/2
  heron = s*(s-x)*(s-y)*(s-z)
  print(heron)
  A = math.sqrt(heron)
  return A
  


# points is a list of 3D points
# ie: [[2, 9, -15], [0, 33, -20], ...]
def FindLargestTriangleArea(points):
  largest = 0
  for a, b in itertools.combinations(points, 2):
    size = get_size(a,b)
    if size > largest:
      largest = size
  return largest

# Reading space delimited points from stdin
# and building list of 3D points
points_data = raw_input()
points = []
for point in points_data.split(' '):
  point_xyz = point.split(',')
  points.append([int(point_xyz[0]), int(point_xyz[1]), int(point_xyz[2])])

# Compute Largest Triangle and Print Area rounded to nearest whole number
area = FindLargestTriangleArea(points)
print(int(round(area)))
