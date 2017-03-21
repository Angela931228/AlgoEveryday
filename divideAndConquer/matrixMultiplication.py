#!/usr/bin/python
"""
Matrix multiplication
Notes:

"""
# 3x3 matrix
X = [[1,7,3],
    [4 ,2,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,3,1,0],
    [4,5,2,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

def mmBruteForce():
	for i in range(0,len(X)):
		for j in range(0, len(Y[0])):
			for k in range(0, len(X[0])):
				result[i][j] = result[i][j] + X[i][k]*Y[k][j];

mmBruteForce()
print result
