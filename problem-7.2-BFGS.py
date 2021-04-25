import numpy as np
import os
# import matplotlib.pyplot as plt
#函数表达式
fun = lambda x:x[0]**2 + x[1]**2 - x[0]*x[1] - 10*x[0] - 4*x[1] + 60

#梯度向量
gfun = lambda x:np.array([2*x[0] - x[1] -10, 2*x[1] - x[0] - 4], dtype=np.float64)

#Hessian矩阵
hess = lambda x:np.array([[2, -1],[-1, 2]])

def bfgs(fun,gfun,hess,x0):
    #功能：用BFGS族算法求解无约束问题：min fun(x)
    #输入：x0是初始点，fun,gfun分别是目标函数和梯度
    #输出：x,val分别是近似最优点和最优解,k是迭代次数  
    maxk = 1e5
    rho = 0.55
    sigma = 0.4
    epsilon = 1e-5
    k = 0
    n = np.shape(x0)[0]
    #海森矩阵可以初始化为单位矩阵
    Bk = np.linalg.inv(hess(x0)) #或者单位矩阵np.eye(n)

    while k < maxk:
        gk = gfun(x0)
        if np.linalg.norm(gk) < epsilon:
            break
        dk = -1.0*np.linalg.solve(Bk,gk)
        m = 0
        mk = 0
        while m < 20: # 用Armijo搜索求步长
            if fun(x0+rho**m*dk) < fun(x0)+sigma*rho**m*np.dot(gk,dk):
                mk = m
                break
            m += 1

        #BFGS校正
        x = x0 + rho**mk*dk
        print ("迭代次数：", k)
        print ("迭代结果：", x)
        sk = x - x0
        yk = gfun(x) - gk   

        if np.dot(sk,yk) > 0:    
            Bs = np.dot(Bk,sk)
            ys = np.dot(yk,sk)
            sBs = np.dot(np.dot(sk,Bk),sk) 

            Bk = Bk - 1.0*Bs.reshape((n,1))*Bs/sBs + 1.0*yk.reshape((n,1))*yk/ys

        k += 1
        x0 = x

    return x0,fun(x0),k#分别是最优点坐标，最优值，迭代次数 

x0 ,fun0 ,k = bfgs(fun,gfun,hess,np.array([0,0]))
print (x0,fun0,k)

# iters = []
# for i in xrange(np.shape(data)[0]):
#     rt = bfgs(fun,gfun,hess,np.array(data[i]))
#     if rt[2] <=200:
#         iters.append(rt[2])
#     if i%100 == 0:
#         print (i,rt[2])

# plt.hist(iters,bins=50)
# plt.title(u'BFGS迭代次数分布',{'fontname':'STFangsong','fontsize':18})
# plt.xlabel(u'迭代次数',{'fontname':'STFangsong','fontsize':18})
# plt.ylabel(u'频率分布',{'fontname':'STFangsong','fontsize':18})