import math

class Node(object):
    def __init__(self,columnIndex,columnName):
        self.columnIndex = columnIndex
        self.columnName = columnName
        self.children = {}


    def __repr__(self):
        result = "[Node:" + self.columnName + "], child = {"
        for name, value in self.children.items():
            result += name+ "=" + repr(value) + ", "
        return result + "}]"

def cal_frequency(feature):
    freq = {}
    for val in feature:
        if val not in freq:
            freq[val] = 0
        freq[val] +=1
    return freq

def cal_entropy(output):
    freq = cal_frequency(output)
    result = 0.0
    for val in freq.values():
        prob = float(val)/len(output)
        result -= prob * math.log(prob,2)
    return result

def filter_data(feature,output,index,value):
    new_features = []
    new_output = []
    for i in range(len(feature)):
        if feature[i][index] == value:
            new_features.append(feature[i])
            new_output.append(output[i])
    return new_features, new_output

def get_columns(features,index):
    result = []
    for row in features:
        result.append(row[index])
    return result

def drop_column(features,index):
    result = []
    for row in features:
        new_row = []
        for i in range(len(row)):
            if i !=index:
                new_row.append(row[i])
        result.append(new_row)
    return result

def information_gain(features,output,index):
    column = get_columns(features,index)
    freq = cal_frequency(column)
    unique_val = set(column)
    result = 0.0
    for value in unique_val:
        new_features,new_output = filter_data(features,output,index,value)
        new_features = drop_column(new_features,index)
        entropy = cal_entropy(new_output)
        pi = freq[value] / float(len(output))
        result += pi * entropy
    return cal_entropy(output) - result

def best_attribute(features,output,columns):
    maxInfoGain = -1.0
    best_feature = -1
    best_feature_index = -1
    for i in range(len(features[0])):
        gain = information_gain(features,output,i)
        if gain>maxInfoGain:
            maxInfoGain=gain
            best_feature_index=i
            best_feature = columns[i]
    return best_feature_index,best_feature

import operator
def max_prob(feature):

    result = {}
    for item in feature:
        if item not in result.keys():
            result[item] = 0
        result[item] +=1
    sortedClassCount=sorted(result.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount

def new_columns(columns,attr):
    result = []
    result = columns[:attr]
    result.extend(columns[attr+1:])
    return result

def build_tree(features,output,columns):
    if output.count(output[0])==len(output):
        return output[0]
    if len(features[0])==1:
        return max_prob(output)
    attr,attr_name = best_attribute(features,output,columns)
    root = Node(attr,attr_name)
    for value in set(get_columns(features,attr)):
        new_features, new_output = filter_data(features, output, attr, value)
        new_cols = new_columns(columns,attr)
        new_features = drop_column(new_features,attr)
        root.children[value] = build_tree(new_features,new_output,new_cols)
    return root

def grow_tree(features, output, columns):
    if output.count(output[0]) == len(output):
        return output[0]
    if len(features[0])==1:
        return max_prob(output)
    attr, attr_name = best_attribute(features, output, columns)
    attr_output = columns[attr]

    DecisionTree = {attr_output: {}}
    del (columns[attr])
    featureValues = [item[attr] for item in features]

    unique_value = set(featureValues)
    for value in unique_value:
        new_features, new_output = filter_data(features, output, attr, value)
        new_features = drop_column(new_features, attr)

        DecisionTree[attr_output][value] = build_tree(new_features, new_output, columns)
    return DecisionTree


def predict_class(Dtree,features,columns):

    for i in range((len(columns)-1)):
        if columns[i]== Dtree.columnName:
            for name, value in Dtree.children.items():
                if features[i]== name:
                    if  hasattr(Dtree,'children'):
                        new_features = new_columns(features,i)
                        new_cols = new_columns(columns,i)
                        #print tree.children['Sunny'].children.values()
                        return predict_class(value,new_features,new_cols)
                    else:
                        return value
               # print "child:",name, value, features[i]
        #print columns[i]
    #print tree.columnName
    #print tree.children

def children(value):
    for name, item in value:
        return name, item
'''
def predict_class(tree,features,columns):
    for i in range((len(columns)-1)):
        if columns[i]== tree.columnName:
            continue
        for name, value in tree.children.iteritems():
            if features[i] == name:
                #new_features = new_columns(features, i)
                #new_cols = new_columns(columns, i)
                print "child:", name, value, features[i]
                i +=1
'''

def main():
    data=[line.strip().split(',') for line in open('tennis.txt')]
    features = [item[:-1] for item in data]
    output = [item[-1] for item in data]
    columns = ['Outlook', 'Temperature', 'Humidity', 'Windy', 'PlayTennis']
    monk = [line.strip().split(' ') for line in open('monks-1.csv')]
    monk_features = [item[1:-1] for item in monk]
    monk_output = [item[0] for item in monk]
    monk_columns = ["a1","a2","a3","a4","a5","a6"]
   # print cal_entropy(output)
    #print filter_data(features,output,0,'Rain')

    #print information_gain(features,output,0)
    #print get_columns(features,0)
    #print drop_column(features, 2)

    #print best_attribute(features,output,columns)
    print build_tree(features,output,columns)
    #print cal_entropy(monk_output)
    # print filter_data(features,output,0,'Rain')
    # print information_gain(features,output,0)
    # print get_columns(features,0)
    # print drop_column(features, 2)
    tree = build_tree(features,output,columns)
    predict_data = [line.strip().split(',') for line in open('test-tennis.txt')]
    predict = [item for item in predict_data]
    for i in range(len(predict)):
        print predict[i]
        print predict_class(tree,predict[i],columns)
    #print predict_class(tree,predict,columns)
    #print build_tree(monk_features,monk_output,monk_columns)
   # print "using Dictionary: ",grow_tree(monk_features,monk_output,monk_columns)
    #print "using Dictionary: ",grow_tree(features, output, columns)

main()