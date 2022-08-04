# -*- coding: utf-8 -*-
"""
test simplex method
依据simplex_method自建库计算教材各类练习题

Created on Fri Dec 25 14:44:31 2020

@author: Charles Lee
"""
from simplex_method import simplex as sim

# 数据来源：p30 2.7(1)~(4)；p46 例3.1；p66 例4.4
for sign in range(6):
    if sign == 0:
        # 2.7（1）
        C = [1,2,3,-1]
        A = [[1,2,3,0],[2,1,5,0],[1,2,1,1]]
        b = [15,20,10]
    elif sign == 1:
        # 2.7（2）
        C = [2,1,3,0,0,0]
        A = [[4,2,2,-1,0,0],[2,4,0,0,1,0],[4,8,2,0,0,1]]
        b = [4,20,16]
    elif sign == 2:
        # 2.7（3）
        C = [1,1,0,0,0]
        A = [[8,6,-1,0,0],[-4,-6,0,1,0],[0,2,0,0,-1]]
        b = [24,12,4]
    elif sign == 3:
        # 2.7（4）
        C = [4,5,1,0,0]
        A = [[3,2,1,-1,0],[2,1,0,0,1],[1,2,-1,0,0]]
        b = [18,4,5]
    elif sign == 4:
        # 对偶单纯形法
        C = [-6,-3,-2,0,0,0]                                          ## 输入C,A,b
        A = [[1,1,1,-1,0,0],[2,2,1,0,-1,0],[2,1,1,0,0,-1]]          ## 注：输入数据中约束条件都为等式，且右式为正
        b = [20,24,10]

    elif sign == 5:
        # 整数规划
        C = [3,2,0,0]
        A = [[2,3,1,0],[2,1,0,1]]
        b = [14,9]


    print('\n第{}题'.format(sign+1))
    simplex = sim(C,A,b)
    if sign in range(4):
        simplex.M_run()   # 前四题用大M法解
    elif sign == 4:
        simplex.anti_run()   # 第五题用对偶单纯形法解(也可用大M法)
    elif sign == 5:
        simplex.int_programming()   # 第六题用整数规划解
    simplex.show()
    print('迭代{}次'.format(simplex.step))