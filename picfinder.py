import numpy as np
import cv2 as cv
import pandas as pd


def mse(im1, im2):
    e = np.sum(np.sum((im1 - im2) ** 2))
    e = e/(im1.shape[0] * im1.shape[1])
    return e
    

source = cv.imread('source.jpeg')
# add path to the target image(to find) here
target = cv.imread('target.jpg')
target = cv.resize(target, (32,32), interpolation=cv.INTER_AREA)

l = []

(m, n, d) = source.shape
m = m//32
n = n//32

min_e = -1
idx = (0,0)

for i in range(m):
    y1 = 32*i
    y2 = 32*(i+1)
    for j in range(n):
        x1 = 32*j
        x2 = 32*(j+1)
        e = mse(source[y1:y2, x1:x2], target)
        l.append(e)
        if(min_e == -1 or e < min_e):
            min_e = e
            idx = (i,j)

x, y = idx
# print(x, y)

# cv.imshow("source", source)
cv.imshow("source", source[32*x:32*(x+1), 32*y:32*(y+1)])
cv.rectangle(source, (32*y, 32*x), (32*(y+1),32*(x+1)), (0,0,255), thickness=5)
cv.arrowedLine(source, (0,0), (32*y, 32*x), (0,255,0), thickness=10)
cv.imwrite('res.jpeg', source)
cv.waitKey(0)

# df = pd.DataFrame(l)
# df.to_csv('mse.csv')