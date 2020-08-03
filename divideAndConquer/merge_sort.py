#!/usr/bin/python
"""
Notes:

python array copy by value A = B[:]

two D array: deep copy 
	
"""


A = []

def mergeSort(start,end):
	if(start==end):
		return
	else:
		mid = (start+end)/2
		mergeSort(start,mid)
		mergeSort(mid+1,end)
		mergeLeftAndRight(start,mid,end)

def mergeLeftAndRight(start,mid,end):
	i = start
	j = mid+1
	p = i
	B = A[:]
	while i< mid+1 and  j<end+1:
		if A[i] < A[j]:
			B[p] = A[i]
			i=i+1
			p=p+1
		else:
			B[p] = A[j]
			j=j+1
			p=p+1
	while i < mid + 1:
		B[p]= A[i]
		i = i + 1
		p = p + 1
	while j < end + 1 :
		B[p] = A[j]
		j =  j + 1
		p = p + 1
	A[start:(end+1)] = B[start:(end+1)]
			
	
		
A = [2,3,5,7,6,4,1]
mergeSort(0,(len(A)-1))
print(A)
