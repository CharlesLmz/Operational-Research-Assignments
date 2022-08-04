# -*- coding: utf-8 -*-
"""
dynamic planning
动态规划模型

Created on Tue Dec 29 08:34:00 2020

@author: Charles Lee
"""

import math
import time

# 动态规划求解
def dynamic(b,C,P):
    start1 = time.time()
    stagen = len(C)
    flast = [1]*(b+1)
    St = [[0]*(b+1)]*stagen
    for idx in range(stagen):
        idx = stagen-1 -idx
        fmax = [0]*(b+1)
        nmax = fmax.copy()
        for S in range(b+1):
            D = math.floor(S/C[idx])                ## D 决策空间
            for nn in range(D+1):
                Slast = S - nn*C[idx]               ## S-Slast 状态转移方程
                f = (1-(P[idx]**nn))*flast[Slast]   ## f-flast 指标递推方程
                if f > fmax[S]:
                    fmax[S] = f
                    nmax[S] = Slast
        St[idx] = nmax                              ## St 保存每次选择数据，便于后续计算最优选择
        flast = fmax
    slast = b
    choice = [0]*stagen
    for idx in range(stagen):                       ## choice 每一项代表每一个物品的决策数量
        choice[idx] = int((slast-St[idx][slast])/C[idx]) 
        slast = St[idx][slast]
    print("1.动态规划\n最优决策：",choice,"\n决策结果：",flast[b])
    end1 = time.time()
    print("运行时间：",end1-start1)


# 下面用枚举法求解同一问题
def enume(b,C,P):
    start2 = time.time()
    fmax = 0
    for c1 in range(1,math.floor(b/C[0])+1):
        last1 = b - c1*C[0]
        for c2 in range(1,math.floor(last1/C[1])+1):
            last2 = last1 - c2*C[1]
            c3 = math.floor(last2/C[2])
            f = (1-P[0]**c1)*(1-P[1]**c2)*(1-P[2]**c3)
            if f > fmax:
                fmax = f
                choice = [c1,c2,c3]
    print("\n2.枚举法\n最优决策：",choice,"\n决策结果：",fmax)
    end2 = time.time()
    print("运行时间：",end2-start2)

# 数据来源：p177 例8.4

if __name__ == "__main__":
    b = 10                    # b为总预算
    C = [2, 3, 1]             # C为各元件费用
    P = [0.3, 0.2, 0.4]       # P为原件异常概率
    dynamic(b,C,P)
    enume(b,C,P)