# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:51:12 2016

@author: Vipul Munot
"""

import math
import operator
def euclidean_distance(data1,data2):
    result = 0.0
    for val in range(len(data2)-1):
        result += (data1[val]-data2[val])**2
    return math.sqrt(result)

#data1 = [2, 2, 2, 'a']
#data2 = [4, 4, 4]
#print(euclidean_distance(data1,data2))


def knn(train,test,k):
    dist,neighbors = [],[]
    for i in range(len(train)):
        distance= euclidean_distance(train[i],test)
        dist.append((train[i],distance))
        dist.sort(key=operator.itemgetter(1))
    for i in range(k):
        neighbors.append(dist[i][0])
    return neighbors

#train= [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
#test= [5, 5, 5]
#neighbors = knn(train, test, 2)
#print(neighbors)



def majorityVote(neighbors):
    vote = {}
    for i in range(len(neighbors)):
        lst = neighbors[i][-1]
        if lst in vote:
            vote[lst]+=1
        else:
            vote[lst]=1
    majority = max(vote.items(), key=operator.itemgetter(1))[0]
    return majority
#train= [[2, 2, 2, 'a'], [4, 4, 4, 'b'],[1,1,1,'a'], [3,3,3,'b']]
#test= [5, 5, 5]
#neighbors = knn(train, test, 2)
#print(majorityVote(neighbors))


def accuracy(test,predictions):
    result = 0
    for i in range(len(test)):
        if test[i][-1] == predictions[i]: result+=1
    print(result)
    return ((result/float(len(test)))*100)

def main():
    import random
    data = []
    for line in open('E:/IUB/AML/HW/iris.data'):
        x1,v1,x2,v2,e = line.strip().split(',')
        row = [float(x1),float(v1),float(x2),float(v2),e]
        data.append(row)

    k = int(input("Please enter value of k:\t"))
    split = int(input("Please enter the percentage split:\t"))
    split = (split/100)
    train,test = [],[]
    predictions=[]
    for x in range(len(data)-1):
        for y in range(4):
            data[x][y] = float(data[x][y])
        if random.random() < split:
            train.append(data[x])
        else:
            test.append(data[x])
    print ('Train set: ' + repr(len(train)))
    print ('Test set: ' + repr(len(test)))
    for i in range(len(test)):
        neighbors = knn(train,test[i],k)
        responses = majorityVote(neighbors)
        predictions.append(responses)
        print('predicted=' + repr(responses) + ', actual=' + repr(test[i][-1]))


    acc = accuracy(test, predictions)
    print('Accuracy: ' + repr(acc) + '%')


if __name__ == '__main__':
	main()

