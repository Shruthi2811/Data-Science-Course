# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:38:03 2016

@author: Vipul Munot
"""
tennis=[line.strip().split(',') for line in open('tennis.txt')]
test_tennis=[line.strip().split(',') for line in open('test-tennis.txt')]
data=[['slashdot','USA','yes',18,'None'],
        ['google','France','yes',23,'Premium'],
        ['digg','USA','yes',24,'Basic'],
        ['kiwitobes','France','yes',23,'Basic'],
        ['google','UK','no',21,'Premium'],
        ['(direct)','New Zealand','no',12,'None'],
        ['(direct)','UK','no',21,'Basic'],
        ['google','USA','no',24,'Premium'],
        ['slashdot','France','yes',19,'None'],
        ['digg','USA','no',18,'None'],
        ['google','UK','no',18,'None'],
        ['kiwitobes','UK','no',19,'None'],
        ['digg','New Zealand','yes',12,'Basic'],
        ['slashdot','UK','no',21,'None'],
        ['google','UK','yes',18,'Basic'],
        ['kiwitobes','France','yes',19,'Basic']]

class node:
    def __init__(self,col=-1,value=None,results=None,left=None,right=None):
        self.col=col
        self.value = value
        self.results=results # Stores Predicted Output (None: for non leaf nodes)
        self.left=left # True values
        self.right=right # False values

def split_data(data,column,value):
    split = None
    if isinstance(value,int) or isinstance(value,float):
        split = lambda item:item[column]>=value
    else:
        split = lambda item:item[column]==value
    subset1 = [item for item in data if split(item)]
    subset2 = [item for item in data if not split(item)]
    return (subset1,subset2)

r1,r2 = split_data(data,2,'yes')
#print ("\nSubset 1: ",r1)    
#print ("\nSubset 2: ",r2)    

def frequency(data):
    result ={}
    for value in data:
        cols = value[len(value)-1]
        if cols not in result: result[cols]=0
        result[cols]+=1
    return result
    
def entropy(data):
    result =0.0
    freq = frequency(data)
    for val in freq.keys():
        import math
        prob = float(freq[val])/len(data)
        result = result - prob*math.log2(prob)
    return result
#print ("\nEntropy: ",entropy(data))
#print ("\nEntropy: ",entropy(r1))    

def build_tree(rows):
  if len(rows)==0: return node()
  currentScore=entropy(rows)

  best_gain=0.0
  best_criteria=None
  best_sets=None
  
  column_count=len(rows[0])-1
  for col in range(0,column_count):

    column_values={}
    for row in rows:
       column_values[row[col]]=1
    for value in column_values.keys():
      (set1,set2)=split_data(rows,col,value)

      p=float(len(set1))/len(rows)
      gain=currentScore-p*entropy(set1)-(1-p)*entropy(set2)
      if gain>best_gain and len(set1)>0 and len(set2)>0:
        best_gain=gain
        best_criteria=(col,value)
        best_sets=(set1,set2)
  
  if best_gain>0:
    trueBranch=build_tree(best_sets[0])
    falseBranch=build_tree(best_sets[1])
    return node(col=best_criteria[0],value=best_criteria[1],
                        left=trueBranch,right=falseBranch)
  else:
    return node(results=frequency(rows))
tree = build_tree(data) 
tennis_tree = build_tree(tennis) 
def print_tree(tree,indent = ' '):
    if tree.results!= None:
        print (str(tree.results))
    else:
        print (str(tree.col)+':'+str(tree.value))
        print (indent+ 'Left ->',print_tree(tree.left,indent+' '))
        print (indent+ 'Right ->',print_tree(tree.right,indent+' '))

print (print_tree(tree))        
print ("\nTennis:\n")
print (print_tree(tennis_tree))        

def classify(observation,tree):
    if tree.results!=None: return tree.results
    else:
        val = observation[tree.col]
        branch = None
        if isinstance(val,int)or isinstance(val,float):
            if val >=tree.value: branch= tree.left
            else: branch = tree.right
        else:
            if val == tree.value: branch=tree.left
            else: branch = tree.right
    return classify(observation,branch)

print ("\nClasificaton: ",classify(['(direct)','USA','yes',5],tree))    
for values in test_tennis:
    print ("\n",values,"\tClasificaton: ",classify(values,tennis_tree))