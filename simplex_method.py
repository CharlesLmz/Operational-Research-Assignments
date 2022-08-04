# -*- coding: utf-8 -*-
"""
Simplex method 3.0
原单纯形法 + 大M法 + 对偶单纯形法 + 整数规划方法（割平面法）

Created on Fri Dec 11 09:50:49 2020

@author: Charles Lee
"""
import numpy as np

class simplex:
     
    def __init__(self, C, A, b):
        self.C = np.array(C)
        self.A = np.mat(A)
        self.b = np.array(b,float) 
        self.M = 1000
        self.step = 1
        self.flag = 1                                              ## flag代表是否有结果，如果无可行解、无界解则不输出结果
    
    # 原单纯形法
    def run(self,xb=None): ### 一般被其他函数调用，直接调用条件：假设初始基矩阵B0为单位矩阵（否则大M），且b不含负数（否则对偶）
        A = self.A
        C = self.C
        b = self.b
        M = self.M
        
        num_B, num_BN = np.shape(A)
        range_BN = np.arange(num_BN)                               ## 获取初始基变量/非基变量序号
        try:
            xn = np.array([i for i in range_BN if not i in xb])
        except:
            xb = range_BN[num_BN-num_B:].copy()
            xn = np.array([i for i in range_BN if not i in xb])
       
        # 获取基矩阵、计算检验数、确定换入变量
        B = A[:,xb].copy()                                         ## 获取基矩阵并求逆
        B_inv = np.linalg.inv(B)
        b = np.array(B_inv*np.mat(b).T)
        A = B_inv*A
        if (b < 0).any():
            #print('***转入对偶单纯形***')
            return self.anti_run(xb)
        
        Z = np.zeros(num_BN)                                       ## 计算检验数check，即Cj-Zj
        check = np.zeros(num_BN)
        for j in xn:                                            
            Z[j] = float(sum(np.multiply(A[:,j], np.matrix(C[xb]).T)))
        for j in xb:
            Z[j] = C[j]
        for j in range_BN:
            check[j] = C[j] - Z[j]
            
        x_in = np.argmax(check)                                    ## 依最大检验数选换入变量
        # print(self.step,' :',xb,C,Z,check)
        if check[x_in] <= 0:                                       ## 若最大检验数小于零，则已最优
            if sum(check==0) > num_B:                        
                print("该问题有多重解")                             ## 若最优解时，有非基检验数为0，则为多重最优解
            X = np.zeros(num_BN)
            j = 0
            for i in xb:
                X[i] = b[j]
                j += 1
                
            self.X = X
            self.A = A
            self.b = b
            return xb,b,A
        
    # 计算theta
        theta_a = A[:,x_in].copy()                                  ## 计算theta的分母，即换入变量对应列的价格系数a
        self.flag = 0
        for i in range(num_B):                                      ## 排除为非正数的theta_a
            if theta_a[i] <= 0:
                theta_a[i] = 1/M
                continue
            self.flag = 1  
            
        if self.flag == 0:                   
            print("该问题有无界解")                                  ## 如果theta_a都为非正数，则为无界解
            return
    
        theta = b/theta_a                                           ## theta计算公式
    
        for i in range(len(theta)):                                 ## 若出现退化解情况，即b为0，则该项theta也需排除
            if theta[i]<=1/M and theta_a[i]<=1/M:
                theta[i]=M
                
    # 确定换出变量
        x_out = xb[np.argmin(theta)]
        xb[xb==x_out] = x_in
        xn[xn==x_in] = x_out
        self.step += 1
        if self.step > 100:
            print("程序无限循环")
            self.flag = 0
            return
        
        return self.run(xb)
            
    # 对偶单纯形法
    def anti_run(self,xb=None): ### 当run()发现b中含有负数时，转入anti_run()
        A = self.A
        C = self.C
        b = self.b
        M = self.M
        num_B, num_BN = np.shape(A)
                                                                   
        range_BN = np.arange(num_BN)                                ## 获取初始基变量/非基变量序号
        try:
            xn = np.array([i for i in range_BN if not i in xb])
        except:
            xb = range_BN[num_BN-num_B:].copy()
            xn = np.array([i for i in range_BN if not i in xb])
       
        # 获取基矩阵、计算检验数、确定换入变量
        B = A[:,xb].copy()                                          ## 获取基矩阵并求逆
        B_inv = np.linalg.inv(B)
        b = np.array(B_inv*np.mat(b).T)
        A = B_inv*A
        
        if (b >= 0).all():                                          ## 判断是否还有负值基变量，若无则转入一般单纯形
            return self.run(xb)
        
        outi = np.argmin(b)                                         ## 选取最大负值项为换出变量
        x_out = xb[outi]
        
        Z = np.zeros(num_BN)                                        ## 计算检验数check，即Cj-Zj
        check = np.zeros(num_BN)
        for j in xn:                                            
            Z[j] = float(sum(np.multiply(A[:,j], np.matrix(C[xb]).T)))
        for j in xb:
            Z[j] = C[j]
        for j in range_BN:
            check[j] = C[j] - Z[j]
        
        theta_a = A[outi,:].copy()
        flag = 0
        for i in range(num_BN):                                     ## 排除为非正数的theta_a
            if theta_a[0,i] >= 0:
                theta_a[0,i] = -1/M
                continue
            flag = 1  
        if flag == 0:                   
            print("该问题有无界解")                                  ## 如果theta_a都为非正数，则为无界解
            return
        
        theta = check/theta_a
        for i in range(num_BN):                                     ## 若出现退化解情况，即b为0，则该项theta也需排除
            if theta[0,i]<=1/M:
                theta[0,i]=M
                
        x_in = np.argmin(theta)
        
        xb[xb==x_out] = x_in
        xn[xn==x_in] = x_out
        
        #print(self.step,':',b,check,theta_a,theta,xb)
        self.step += 1
        if self.step > 100:
            print("程序无限循环")
            return
        return self.anti_run(xb)
    
    # 大M法（默认）
    def M_run(self):  ### 默认用大M法求解各类线性规划问题
        # 数据预处理       
        M = self.M
        num_B, num_BN = np.shape(self.A)
                                                                    
        cm = np.array([-M for i in range(num_B)])                   ## 添加人工变量
        am = np.identity(num_B)
        self.A = np.hstack((self.A,am))
        self.C = np.hstack((self.C,cm))
        
        try:                                                        ## 若self.run()输出异常，此时不继续输出结果
            xb,b,A = self.run()
        except:
            return
    
        M_x = self.X[-1:-num_B:-1]
        if max(M_x) != 0:
            print("该问题无可行解")
            self.flag = 0
            return
        self.X = self.X[:num_BN]
        self.C = self.C[:num_BN]
        self.A = self.A[:,:num_BN]

        return xb,b,self.A
    
    # 整数规划
    def int_programming(self):  ### 有整数要求的线性规划问题用该方法求解
        
        xb0,bt0,At0= self.M_run()
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
                self.C = np.hstack((self.C,[0]))
                self.A = np.hstack((np.vstack((At,At_frac)),lvector))
                self.b = np.vstack((bt,bt_frac)).T
                step += 1
                
            else:
                break
            if step > 5:
                print("整数规划无限循环")
                self.flag = 0
                break
            
            xb = np.hstack((xb,At.shape[1]))
            #print('C=',simplex.C,'\nA=',simplex.A.round(3),'\nb=',simplex.b,'\n',xb)
            xb,bt,At= self.run(xb)
    
    # 模型输出：
    def show(self):
        if self.flag == 1:
            X = self.X
            A = self.A
            C = self.C
            num_B, num_BN = np.shape(A)
            Zmax = round(sum(C*X),3)
            print('计算结果：\nX = ', X,'\nZmax = ', Zmax)


if __name__ == "__main__":
    C = [-6,-3,-2,0,0,0]                                          ## 输入C,A,b，数据来源：p52 3.10
    A = [[1,1,1,-1,0,0],[2,2,1,0,-1,0],[2,1,1,0,0,-1]]            ## 注：输入数据中约束条件式都为等式，且右式为正
    b = [20,24,10]
    simplex1 = simplex(C,A,b)
    simplex1.anti_run()
    simplex1.show()
    