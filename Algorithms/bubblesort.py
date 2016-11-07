# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:03:29 2016

@author: Vipul Munot
"""

def bubblesort(array):
    no_of_pass = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[j] < array[i]:
                array[j],array[i] = array[i],array[j]
                no_of_pass +=1
    return (no_of_pass,array)
def main():
    lst = [54,26,93,17,77,31,44,55,20]
    total,array = bubblesort(lst)
    print("Total Passes:\t",total)
    print("\nSorted Array:\t",array)

if __name__ == '__main__':
	main()    