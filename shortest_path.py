# -*- coding: utf-8 -*-
"""
Dijkstra and Ford
Dijkstra和Ford算法求解最短路问题

Created on Tue Dec 29 14:57:34 2020

@author: Charles Lee
"""

import numpy as np
import time

class shortest_path:
    def __init__(self,d,beginning=0,ending='a'):
        self.d = d
        self.beginning = beginning
        self.ending = ending
        if ending == 'a':
            self.ending = len(d)-1
            
    # Dijkstra
    def Dijkstra(self):
        d = self.d
        beginning = self.beginning
        ending = self.ending
        
        start1 = time.time()
        points = np.array(range(len(d)))
        pi = beginning
        F = np.array([i for i in points if i != pi])
        df = np.array([float('inf')]*len(d))
        df[0] = 0
        front_point = [0]*len(d)
        while 1:
            for p in F:
                dfx = d[pi][p] + df[pi]
                if dfx < df[p]:
                    df[p] = dfx
                    front_point[p] = pi
            try:
                fi = F[np.argmin(d[pi,F])]
                F = np.delete(F,np.argmin(d[pi,F]))
            except:
                break
            #print([pi,fi],',',df,',',F)
            pi = fi
            
        route = [ending]
        pi = ending
        while 1:
            pi = front_point[pi]
            route.insert(0,pi)
            if pi == beginning:
                break
            
        print('1.Dijkstra\n最短路程：',df[ending],'\n最短路径：',route)
        end1 = time.time()
        print('运行时间：',end1-start1)
    
    # Ford
    def Ford(self):
        d = self.d
        beginning = self.beginning
        ending = self.ending
        
        start2 = time.time()
        points = np.array(range(len(d)))
        for i in points:
            p2 = [a for a in points if a != i]
            for j in p2:
                p3 = [a for a in p2 if a != j]
                for k in p3:
                    if d[i,k]+d[k,j] < d[i,j]:
                        d[i,j] = d[i,k]+d[k,j]
        print('1.Ford\n最短路程：',d[beginning,ending])
        end2 = time.time()
        print('运行时间：',end2-start2)
            
if __name__ == "__main__":
    # 数据来源：p206 例9.8
    dd = np.array([[float('inf')]*7]*7)
    dd[0,1] = 2;dd[0,2] = 5;dd[1,2] = 2
    dd[1,4] = 3;dd[1,3] = 4;dd[2,3] = 1
    dd[3,4] = 5;dd[3,5] = 6;dd[4,5] = 7
    dd[6,2] = 3;dd[6,3] = 8;dd[6,5] = 2
    route = shortest_path(dd,ending=5)
    route.Dijkstra()
    route.Ford()