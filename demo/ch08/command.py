__author__ = 'sunbeansoft'

import regression as reg
import matplotlib.pyplot as plt
from numpy import *

xArr, yArr = reg.loadDataSet('ex0.txt')
# wx = reg.standRegres(xArr, yArr)
# print wx
#
# xMat = mat(xArr)
# yMat = mat(yArr)
#
# yHat = xMat * wx
# corrcoef(yHat.H, yMat)
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
# xCopy = xMat.copy()
# xCopy.sort(0)
# yHat = xCopy * wx
# ax.plot(xCopy[:, 1], yHat)
# plt.show()

print reg.lwlr(xArr[0], xArr, yArr, 1.0)
print reg.lwlr(xArr[0], xArr, yArr, 0.001)

yHat = reg.lwlrTest(xArr, xArr, yArr, 0.003)
xMat = mat(xArr)
srtInd = xMat[:, 1].argsort(0)
xSort = xMat[srtInd][:, 0, :]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xSort[:, 1], yHat[srtInd])
ax.scatter(xMat[:, 1].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c='red')
plt.show();
