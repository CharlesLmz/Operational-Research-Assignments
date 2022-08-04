# -*- coding: utf-8 -*-
"""
int programming
依据simplex_method自建库计算整数规划问题

Created on Fri Dec 25 22:09:52 2020

@author: Charles Lee
"""
import simplex_method as sim
import numpy as np

C = [3,2,0,0]
A = [[2,3,1,0],[2,1,0,1]]
b = [14,9]
simplex = sim.simplex(C,A,b)
xb0,bt0,At0= simplex.M_run()
xb = xb0.copy()
bt = bt0.copy()
At = At0.copy()

step = 1
while 1:
    bt = bt.round(3)
    frac = (bt - np.floor(bt)).tolist()
    mfrac = max(frac)
    
    if mfrac[0] > 0.0001:
        mi = frac.index(mfrac)
        At_frac = (At - np.floor(At))[mi,:]
        bt_frac = (bt - np.floor(bt))[mi]
        lvector = np.mat([0]*len(bt)+[-1]).T
        simplex.C = np.hstack((simplex.C,[0]))
        simplex.A = np.hstack((np.vstack((At,At_frac)),lvector))
        simplex.b = np.vstack((bt,bt_frac)).T
        step += 1
        
    else:
        break
    if step > 5:
        print("整数规划无限循环")
        break
    
    xb = np.hstack((xb,At.shape[1]))
    #print('C=',simplex.C,'\nA=',simplex.A.round(3),'\nb=',simplex.b,'\n',xb)
    xb,bt,At= simplex.run(xb)
    
simplex.show()
