import numpy as np
import os
# import matplotlib.pyplot as plt
#函数表达式
fun = lambda x:x[0]**2 + x[1]**2 - x[0]*x[1] - 10*x[0] - 4*x[1] + 60

#梯度向量
gfun = lambda x:np.array([2*x[0] - x[1] -10, 2*x[1] - x[0] - 4], dtype=np.float64)

#Hessian矩阵
hess = lambda x:np.array([[2, -1],[-1, 2]])

def dfp(fun,gfun,hess,x0):
    #功能：用DFP算法求解无约束问题：min fun(x)
    #输入：x0式初始点，fun,gfun，hess分别是目标函数和梯度,Hessian矩阵格式
    #输出：x,val分别是近似最优点，最优解，k是迭代次数
    maxk = 1e5
    rho = 0.05
    sigma = 0.4
    epsilon = 1e-5 #迭代停止条件
    k = 0
    n = np.shape(x0)[0]
    #将Hessian矩阵初始化为单位矩阵
    Hk = np.linalg.inv(hess(x0))

    while k < maxk:
        gk = gfun(x0)
        if np.linalg.norm(gk) < epsilon:
            break
        dk = -1.0*np.dot(Hk,gk)
#         print dk

        m = 0;
        mk = 0
        while m < 20:#用Armijo搜索步长
            if fun(x0 + rho**m*dk) < fun(x0) + sigma*rho**m*np.dot(gk,dk):
                mk = m
                break
            m += 1
        #print mk
        #DFP校正
        x = x0 + rho**mk*dk
        # print ("第" + %d + "次的迭代结果为：%s", %(k, str(x)))
        print ("迭代次数：", k)
        print ("迭代结果：", x)
        sk = x - x0
        yk = gfun(x) - gk

        if np.dot(sk,yk) > 0:
            Hy = np.dot(Hk,yk)
            # print Hy
            sy = np.dot(sk,yk) #向量的点积
            yHy = np.dot(np.dot(yk,Hk),yk) #yHy是标量
            Hk = Hk - 1.0*Hy.reshape((n,1))*Hy/yHy + 1.0*sk.reshape((n,1))*sk/sy

        k += 1
        x0 = x
    return x0.astype(float), fun(x0), k  #分别是最优点坐标，最优值，迭代次数

x0 ,fun0 ,k = dfp(fun,gfun,hess,np.array([0,0]))
print (x0,fun0,k)
# n = 50
# x = y = np.linspace(-10,10,n)
# xx,yy = np.meshgrid(x,y)
# data = [[xx[i][j],yy[i][j]] for i in range(n) for j in range(n)]
# iters = []
# # for i in range(np.shape[0]):
# for i in range(np.shape(data)[0]):
#     rt = dfp(fun,gfun,hess,np.array([0,0]))
#     # rt = dfp(fun,gfun,hess,np.array(data[i]))
#     if rt[2] <=200: # 提出迭代次数过大的
#         iters.append(rt[2])
#     if i%100 == 0:
#         print (i,rt[2])

# plt.hist(iters,bins=50)
# plt.title(u'DFP迭代次数分布',{'fontname':'STFangsong','fontsize':18})
# plt.xlabel(u'迭代次数',{'fontname':'STFangsong','fontsize':18})
# plt.ylabel(u'频率分布',{'fontname':'STFangsong','fontsize':18})