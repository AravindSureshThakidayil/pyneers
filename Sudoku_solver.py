import numpy as np
import random
import sys


def unsolved_spots(problem):
    n=0
    for i in problem:
        for j in i:
            if (j==0):
                n=n+1
    return n

def row_check(problem,x,y,n):
    for j in range(9):
        if problem[x][j]==n:
            return False
    return True
def column_check(problem,x,y,n):
    for i in range(9):
        if (problem[i][y]==n):
            return False
    return True

def square_check(problem,x,y,n):
    index=0
    if (x<3 and y<3):
        index=1
    elif ((x<6 and x>=3) and y<3):
        index=2
    elif((x<9 and x>=6) and y<3):
        index=3
    elif((x<3 and (y>=3 and y<6))):
        index=4 
    elif ((x<6 and x>=3) and (y>=3 and y<6)):
        index=5
    elif (x<3 and (y>=6 and y<9)):
        index=7
    elif((x<6 and x>=3) and (y>=6 and y<9)):
        index=8
    elif((x<9 and x>=3)and (y>=6 and y<9)):
        index=9
    if (index==1 or index==4 or index==7):
        for i in range(index-1,(index-1)+3):
            for j in range(3):
                if ((i==x) and j==y):
                    continue
                if(n==problem[i][j]):
                    return False
        return True
    elif (index==2 or index==5 or index==8):
        for i in range(index-2,(index-2)+3):
            for j in range(3):
                if ((i==x) and j==y):
                    continue
                if(n==problem[i][j]):
                    return False
        return True
    elif (index==3 or index==6  or index==9):
        for i in range(index-3,(index-3)+3):
            for j in range(3):
                if ((i==x) and j==y):
                    continue
                if(n==problem[i][j]):
                    return False
        return True
                

inserted_indexes=[]

""" def Problem_solver(problem):   #a is 2d array 

    n=unsolved_spots(problem)
    print(n)
    if n<=20:
        print(problem)
        return
    for i in range(9):
        for j in range(9):
            if problem[i][j]==0:
                for N in range(1,10):
                    if (row_check(problem,i,j,N) and column_check(problem,i,j,N) and square_check(problem,i,j,N)):
                        problem[i][j]=N
                        inserted_indexes.append([N,i,j])
                        break
                    else:
                        continue
            elif ([i,j]in inserted_indexes[1:3]):
                N=random.randint(1,9)
                if N==inserted_indexes[0]:
                    continue
                if (row_check(problem,i,j,N) and column_check(problem,i,j,N) and square_check(problem,i,j,N)):
                    problem[i][j]=N
                else:
                    continue

            else:
                continue

    solution=Problem_solver(problem)
 """
def test(problem,i,j,N):
    if (row_check(problem,i,j,N) and column_check(problem,i,j,N) and square_check(problem,i,j,N)):
        return True
    return False

def next_pos(problem):
    for i in range(9):
        for j in range(9):
            if problem[i][j]==0:
                
                return i,j
    return None
def backtrack(problem):

    position=next_pos(problem)
    if not position:
        return True
    i,j=position
    for N in range(1,10):
        if test(problem,i,j,N):
            problem[i][j]=N
            if backtrack(problem):
                return True
            problem[i][j]=0
    return False
dimension=3
def print_puzzle(puzzle):
    for i in range(len(puzzle)):
        if i % dimension == 0 and i != 0:
            print('')

        for j in range(len(puzzle[0])):
            if j % dimension == 0 and j != 0:
                print('  ', end='')
            print(str(puzzle[i][j] or '_'), end=' ')
            if j % (dimension * dimension - 1) == 0 and j != 0:
                print('')

test_1=[[0,7,0,0,0,0,0,0,9],
        [5,1,0,4,2,0,6,0,0],
        [0,8,0,3,0,0,7,0,0],
        [0,0,8,0,0,1,3,7,0],
        [0,2,3,0,8,0,0,4,0],
        [4,0,0,9,0,0,1,0,0],
        [9,6,2,8,0,0,0,3,0],
        [0,0,0,0,1,0,4,0,0],
        [7,0,0,2,0,3,0,9,6]]
backtrack(test_1)
print_puzzle(test_1)

