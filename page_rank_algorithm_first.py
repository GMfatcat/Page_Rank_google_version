# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:45:31 2021

@author: fatcat version
"""
import numpy as np
import random as r

def Create_Data( Number , alpha):
    
    G = np.zeros((Number,Number))
    
    for i in range(Number):
        
        for j in range(Number):
            
            if i == j:
                
                continue
            
            if r.random() > alpha: #隨機生成0-1之間的float,若超過0.5則代表: i節點有連結到j節點 => 輸入1
            
                G[i][j] = 1    
    
               
    return G 

#   G                  
#   到達-> A B C       
#       A  0 p p                
#   出  B  p 0 0        
#   發  C  p 0 0        

def Generate_Transfer_Matrix(G, Beta , Number):
    
    M = np.zeros(np.shape(G))
    
    for i in range(Number): 
        
        Row_i_sum = sum(G[i])
        
        if Row_i_sum == 0: #如果有一列總和都為0就直接到下一列
                continue
            
        for j in range(Number):
            M[i][j] = G[i][j]/Row_i_sum
        
        
    return M
    
# pagerank 演算法
def PageRank(M , Beta , eps , Itr_Max_Time , Number):
    R = np.ones(Number)
    teleport = np.ones(Number) / Number
    
    for time in range(Itr_Max_Time):
        R_new = Beta*np.dot(M, R) + (1-Beta)*teleport
        
        if np.linalg.norm(R_new - R) < eps: # np.linalg.norm 計算矩陣內所有元素平方和
        
            break
        
        R = R_new.copy()
           
    return R_new , time

# start here
alpha = 0.5
Beta = 0.80
Number = 50
eps  = 1e-3
Itr_Max_Time = 2000
Generate_Matrix = Create_Data(Number, alpha)
M = Generate_Transfer_Matrix(Generate_Matrix , Beta , Number)
Final_R , ItR_TIME = PageRank(M, Beta, eps, Itr_Max_Time, Number)

print("----------RESULT-------------")
print(Final_R)
print("Itreration time : ",ItR_TIME)




































