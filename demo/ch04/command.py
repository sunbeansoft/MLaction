__author__ = 'shangbin.sb'
import bayes
from numpy import *

import feedparser

listOPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
print bayes.setOfWords2Vec(myVocabList, listOPosts[0])

trainMat = []
for postinDoc in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
print trainMat
p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)
print p0V
print p1V
print pAb

bayes.testingNB()

bayes.spamTest()

ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
vocabList, pSF, pNY = bayes.localWords(ny, sf)
vocabList, pSF, pNY = bayes.localWords(ny, sf)

bayes.getTopWords(ny, sf)
