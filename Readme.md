# Python Codes for Operations Research

## 1 代码包内容

#### （1） 线性规划求解库 simplex_method.py

组合了一般单纯形法、大M法、对偶单纯形法及整数规划中的割平面法，经验证**（附有测试程序simplex_test.py）**基本能够求解1~5章的所有习题。

其中有simplex类，其方法主要有：run()一般单纯形法，M_run()大M法单纯形法，anti_run()对偶单纯形法，int_programming()割平面法、show()结果输出方法。

**库的使用：**

非整数线性规划问题只需要输入对应C、A、b参量创建simplex类，并统一调用M_run()方法即可进行运算，程序将自动判别是否使用对偶单纯形法与一般单纯形法。

而整数规划问题则在输入C、A、b参量创建simplex以后，调用int_programming()函数后即可运算出结果。

注：当问题为无界解、无可行解、多重解时程序也会给出提示。

#### （2）动态规划问题求解 dynamic_planning.py 、knapsack_problem.py

dynamic_planning.py 对书上的例题8.4（一维离散动态规划）进行建模并求解结果，还编写了枚举法函数解同一问题并进行求解时间的对比；

knapsack_problem.py 对背包问题进行建模，分别建立一维、二维背包问题模型，并求解出结果。

#### （3）最短路问题 shortest_path.py

复现Dijkstra算法和Ford算法对最短路问题进行求解，并进行求解时间的对比。

#### （4）粒子群算法 particle_swarm_optimization

学习粒子群算法并理解后进行的代码复现
