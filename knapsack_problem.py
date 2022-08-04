# -*- coding: utf-8 -*-
"""
knapsack problem 
一维、二维背包问题求解

Created on Tue Dec 22 08:20:10 2020

@author: Charles Lee
"""

import math
import time
import numpy as np
 
#背包容量B，重量列表c，价值列表p
def knapsack(B,c,p): # 一维背包
    start1 = time.time()
    stagen = len(c)
    flast = [0]*(B+1)
    St = [[0]*(B+1)]*stagen
    for idx in range(stagen):
        idx = stagen-1 -idx
        fmax = [0]*(B+1)
        nmax = fmax.copy()
        for S in range(B+1):
            D = math.floor(S/c[idx])                ## D 决策空间
            for nn in range(D+1):
                Slast = S - nn*c[idx]               ## S-Slast 状态转移方程
                f = p[idx]*nn + flast[Slast]   ## f-flast 指标递推方程
                if f > fmax[S]:
                    fmax[S] = f
                    nmax[S] = Slast
        St[idx] = nmax                              ## St 保存每次选择数据，便于后续计算最优选择
        flast = fmax
    slast = B
    choice = [0]*stagen
    for idx in range(stagen):                       ## choice 每一项代表每一个物品的决策数量
        choice[idx] = int((slast-St[idx][slast])/c[idx]) 
        slast = St[idx][slast]
    print("1.一维背包问题\n最优决策：",choice,"\n决策结果：",flast[B])
    end1 = time.time()
    print("运行时间：",end1-start1)


def mul_knap(R,S,w,v,p):  # 二维背包
    start1 = time.time()
    stagen = len(w)
    flast = np.zeros((R+1,S+1))
    St = np.zeros((stagen,R+1))
    for idx in range(stagen):
        idx = stagen-1 -idx
        fmax = np.zeros((R+1,S+1))
        nmax = np.zeros(R+1)
        for Sr in range(R+1):
            for Ss in range(S+1):
                D = min(math.floor(Sr/w[idx]), math.floor(Ss/v[idx]))             ## D 决策空间
                for nn in range(D+1):
                    Srlast = Sr - nn*w[idx]               ## Sr-Srlast 状态转移方程
                    Sslast = Ss - nn*v[idx]               ## Ss-Sslast 状态转移方程
                    f = p[idx]*nn + flast[Srlast,Sslast]  ## f-flast 指标递推方程
                    if f > fmax[Sr,Ss]:
                        fmax[Sr,Ss] = f
                        nmax[Sr] = Srlast
        St[idx] = nmax                                    ## St 保存每次选择数据，便于后续计算最优选择
        flast = fmax
    slast = R
    choice = [0]*stagen
    for idx in range(stagen):                             ## choice 每一项代表每一个物品的决策数量
        choice[idx] = int((slast-St[idx,slast])/w[idx]) 
        slast = int(St[idx,slast])
    print("2. 二维背包问题\n最优决策：",choice,"\n决策结果：",flast[R,S])
    end1 = time.time()
    print("运行时间：",end1-start1)

if __name__ == "__main__":
    
    bag = 13 # 一维背包问题
    weights=[1,2,5,6,7,9]
    price=[1,6,18,22,28,36]
    knapsack(bag,weights,price)
    
    R = 15 # p195 8.15（二维背包问题）
    S = 10
    w = [2,3,4,5]
    v = [2,2,2,3]
    p = [3000,4000,5000,6000]
    mul_knap(R, S, w, v, p)