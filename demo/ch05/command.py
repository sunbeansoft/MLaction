__author__ = 'sunbeansoft'

import logRegres as lr
from numpy import *

dataArr, labelMat = lr.loadDataSet()
weight = lr.gradAscent(dataArr, labelMat)
lr.plotBestFit(weight.getA())
weight = lr.stocGradAscent0(array(dataArr), labelMat)
lr.plotBestFit(weight)
weight = lr.stocGradAscent1(array(dataArr), labelMat)
lr.plotBestFit(weight)

lr.multiTest()
