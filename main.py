#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 数据导入
import numpy as np


def loadDataSet():
   postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
   classVec = [0, 1, 0, 1, 0, 1]
   return postingList, classVec

# 数据去重复处理
# print(b,c)


def createVocabList(dataSet):
  vocabSet = set([])
  for item in dataSet:
   vocabSet = vocabSet | set(item)
  return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
  returnVec = [0]*len(vocabList)
  for word in inputSet:
    if word in vocabList:
       returnVec[vocabList.index(word)] = 1
    else: print("%s is not in this set", word)
  return returnVec


def trainNbo(trainMtrix, trainCategory):
  numTrainDocs = len(trainMtrix)  # 文档数量
  numWords = len(trainMtrix[0])  # 单词数量
  paBusive = sum(trainCategory)/float(numTrainDocs)  # 侮辱性文档概率
  p0num = np.zeros(numWords)
  p0Demo = 0.0
  p1num = np.zeros(numWords)
  p1Demo = 0.0
  for i in range(numTrainDocs):
     if trainCategory[i] == 1:
        p1num += trainMtrix[i]
        p1Demo += sum(trainMtrix[i])
     else: 
        p0num +=trainMtrix[i]
        p0Demo +=sum(trainMtrix[i])

  print(p1num,p1Demo)
  print(p0num,p0Demo)
  p1Vect = p1num /p1Demo
  p0Vect = p0num / p0Demo
  return p1Vect,p0Vect,paBusive
  
listOpsts,listClasses= loadDataSet()
myvocabList = createVocabList(listOpsts)
#print(listOpsts)
#print(listClasses)
#print(myvocabList)
tarinMat=[]
for postinDoc in listOpsts:
 tarinMat.append(setOfWords2Vec(myvocabList,postinDoc))
# print(tarinMat)

a=  trainNbo(tarinMat,listClasses)

print(a)



