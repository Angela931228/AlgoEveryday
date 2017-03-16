#!/usr/bin/python
"""
Find maximum subarray

Notes: 

python range from large to small range(10,0,-1)

"""
A = []
def findMaximumSubarray(low, high):
	if low == high :
		return low,high, A[low];
	else:
		mid = (low+high)/2
		
		left_low, left_high, left_sum = findMaximumSubarray(low,mid)
		right_low, right_high, right_sum = findMaximumSubarray(mid+1,high)
		crossing_low, crossing_high, crossing_sum = findMaximumCrossingSubarray(low,mid,high)

		if left_sum >= right_sum & left_sum >= crossing_sum:
			return left_low,left_high,left_sum;
		elif right_sum >= left_sum & right_sum >= crossing_sum:
			return right_low, right_high, right_sum;
		else:
			return crossing_low, crossing_high, crossing_sum;

def findMaximumCrossingSubarray( low, mid, high):
	max_left_sum = -9999;
	left_sum = 0;
	max_idx = mid; 
	for i in range(mid, low-1,-1):
		left_sum = left_sum + A[i];
		if left_sum > max_left_sum:
			max_left_sum = left_sum;
			max_idx = i;
	
	max_right_sum = -9999;
	right_sum = 0;
	max_r_idx = mid; 
	for i in range(mid+1, high+1):
		right_sum = right_sum + A[i];
		if right_sum > max_right_sum:
			max_right_sum = right_sum;
			max_r_idx = i;

	return max_idx, max_r_idx,(max_left_sum+max_right_sum)		

A = [2,-1,3,5,-1,7,-8,4,1]
print findMaximumSubarray(0,(len(A)-1))

