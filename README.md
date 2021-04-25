# 这个代码参考包含了我《组合优化与凸优化》第2次作业的答案（代码+运行结果）
## 第1题
![](/img/problem-1(1).jpg)
![](/img/problem-1(2).jpg)

## 第2题
### (a)
#### 黄金分割法
![](/img/problem-2(a)-黄金分割.png)
#### 斐波拉契法
![](/img/problem-2(a)-斐波拉契.png)
#### 二分法
![](/img/problem-2(a)-二分法.png)
#### Dichotomous
![](/img/problem-2(a)-dichotomous.png)
### (b)
#### 黄金分割法
![](/img/problem-2(b)-黄金分割.png)
#### 斐波拉契法
![](/img/problem-2(b)-斐波拉契.png)
#### 二分法
![](/img/problem-2(b)-二分法.png)
#### Dichotomous
![](/img/problem-2(b)-dichotomous.png)

## 第3题
### Goldstein
![](/img/problem-3-goldstein.jpg)
### Wolfe-Powell
![](/img/problem-3-WolfePowell.jpg)

## 第4题
![](/img/problem-4.png)

## 第5题
![](/img/problem-5.jpg)

## 第6题
![](/img/problem-6.jpg)

## 第7题
### (1)
![](/img/problem-7.1.jpg)

### (2)
![](/img/problem-7.2.png)

### (3)
![](/img/problem-7.3.jpg)

## 第8题
![](/img/problem-8.png)

## 第9题
![](/img/problem-9.png)

## 第10题
![](/img/problem-10.jpg)

## 第11题
华为发表在NIPS2020的工作：《A Simple and Efficient Smoothing Method for Faster Optimization and Local Exploration》
华为诺亚方舟实验室在 NIPS2020 上提出了一种基于已有的随机平滑化（RS） 和 Moreau envelope （ME）的平滑化方法，Bend, Mix and Release (BMR)，BMR 在 RS 的计算简洁和 ME 的近似效果之间进行了折中。主要通过 Bend 操作改变 函数的取值范围，使其趋近于目标函数的低值趋于，然后通过 Mix 操作逼近高斯分布，最后使用 Bend 的逆函数 Release 函数。

## 第12题
共轭函数和对偶性的联系：
（1）	、无论函数是否为凸函数，其共轭函数总是闭的凸函数。同样的，对偶函数一定是凹函数，函数的对偶问题也一定是凸问题。
（2）	原函数的对偶函数和共轭函数之间存在着联系，但原函数不同，对应的关系也不同。对偶函数和共轭函数之间的转化很重要的“转换点”是sub和inf的转换。
