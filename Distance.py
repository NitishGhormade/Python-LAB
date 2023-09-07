# Q2 WAP to calculate Distance Between Two Points A(x1,y1) and B(x2,y2) = |x1 - x2| + |y1 - y2|

import math
ls1 = []
ls2 = []
print("Enter x and y coordinates of First List: ")
for i in range(0,2):
    num = int(input())
    ls1.append(num)

print("Enter x and y coordinates of Second List: ")
for i in range(0,2):
    num = int(input())
    ls2.append(num)

distance = math.sqrt(((ls1[0] - ls2[0])**2) + ((ls1[1] - ls2[1])**2))

print("Distance: ",distance)
