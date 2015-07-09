__author__ = 'sunbeansoft'

import adaboost as ad
from numpy import *

datMat, classLabels = ad.loadSimpData()

D = mat(ones((5, 1)))

print ad.buildStump(datMat, classLabels, D)
