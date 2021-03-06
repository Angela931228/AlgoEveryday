import numpy as np
import copy
import time
cur_pos = 'N' # N E S W 
status = 0 # 0 for empty 1 for carring rack
DIR_COST = 1
TURNING_COST = 3
A = np.array([[1, 1, 1, 1, 0, 0, 0],
              [1, 2, 2, 1, 0, 0, 0],
              [1, 2, 2, 1, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 2, 2, 1, 2, 2, 1],
              [1, 2, 2, 1, 2, 2, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 3, 3, 1, 0, 0, 0],
              [3, 0, 0, 3, 0, 0, 0]])

B = np.array([[{'S'}, {'W'}, {'W', 'S'}, {'W'}],
			  [{'S', 'E'}, {'N', 'E'}, {'E', 'S'}, {'N'}],
			  [{'S'}, {'N', 'W'}, {'S', 'W'}, {'N', 'W'}],
			  [{'S', 'E'}, {'N', 'E'}, {'S', 'E'}, {'N', 'E'}, {'E'}, {'E', 'S'}, {'S'}],
			  [{'S', 'E'}, {'N', 'E'}, {'S', 'E'}, {'N', 'E'}, {'E'}, {'E', 'S'}, {'S'}],
			  [{'S'}, {'N', 'W'}, {'S', 'W'}, {'N', 'W'}, {'W'}, {'W', 'S'}, {'W', 'S'}],
			  [{'S', 'E'}, {'N', 'E'}, {'S', 'E'}, {'N', 'E'}, {'E'}, {'E', 'S'}, {'S'}],
			  [{'S'}, {'N', 'W'}, {'S', 'W'}, {'N', 'W'}, {'N', 'W'}, {'W', 'S'}, {'W', 'S'}],
			  [{'S'}, {'N', 'W'}, {'S', 'W'}, {'N', 'W'}, {'N', 'W'}, {'W'}, {'W'}],
			  [{'E'}, {'N', 'E'}, {'E'}, {'N'}]])
#visited table
D = np.array([[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]])

def printBoard(board, y, x):
	tmp_board = copy.deepcopy(board)
	tmp_board[y][x] = 4
	print(tmp_board)

def getSuccessors(cur_pos, curDir, status):
	successors =  B[cur_pos[0]][cur_pos[1]]
	result =[]
	for successor  in successors:
		s_y, s_x = getSuccessorPosition(cur_pos, successor)
		if A[s_y][s_x]==2 and status ==1:
			continue
		if successor == curDir:
			result.append(((s_y, s_x),DIR_COST))
		else:
			result.append(((s_y, s_x), TURNING_COST+DIR_COST))
	return result


def getSuccessorPosition(cur_pos,s):
	if s == 'S':
		return cur_pos[0]+1, cur_pos[1]
	elif s == 'N':
		return cur_pos[0]-1, cur_pos[1]
	elif s == 'W':
		return cur_pos[0], cur_pos[1]-1
	elif s == 'E':
		return cur_pos[0], cur_pos[1]+1


def uniforCostSearch(start,end,status):
	y,x = start
	pQueue = []
	C = copy.deepcopy(D)
	pQueue.append((start,0,[start]))
	result = []
	while pQueue:
		cur = pQueue.pop(extractMin(pQueue)) #extract the minimum cost
		
		if cur[0]==end:
			return cur[2],cur[1] 
			#result.append((cur[2],cur[1]))
		else:
			C[cur[0][0]][cur[0][1]] = 1 #mark visited
			successors = getSuccessors(cur[0], 'W', status)
			for successor in successors:
				if C[successor[0][0]][successor[0][1]]!=1:
					path_tmp = copy.deepcopy(cur[2])
					path_tmp.append(successor[0])
					pQueue.append((successor[0],cur[1]+successor[1],path_tmp))
	return result

def extractMin(pQueue):
	min = 99999
	idx = 0
	for i in range(0,len(pQueue)):
		if pQueue[i][1] < min:
			idx = i
			min = pQueue[i][1]
	return idx

start = time.time()
print(uniforCostSearch((0,0),(3,1),0))
#print uniforCostSearch((0,0),(1,1),0)
print(uniforCostSearch((1,1),(9,1),1))

end = time.time()
print(end-start)
#printBoard(A,1,0)
#print getSuccessors(1,0,'W',1)