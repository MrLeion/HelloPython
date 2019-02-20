# Python 3.x 学习笔记总结.md
## 基础知识

### 程序编码














## 工具篇

### Anaconda

- [Anaconda 下载地址](https://www.anaconda.com/download/#macos)
- [miniconda 下载地址](https://conda.io/miniconda.html)
 
 
>	我们都知道 Python3 有自己的包管理器 pip3,并且会支持创建 virtualenv。那么为什么还需要 conda 来做包和环境的管理器呢，Anaconda 存在的价值是什么？

> 	Anaconda 是数据分析而生的工具，之所以使用 conda 是因为在下载实处就已经内部集成了 150+ 个第三方库及其依赖项。pip3 是面向所有开发者的，只得一个一个去安装。
>	Anaconda 内部集成的科学报具体可以从 
```
conda list
```

>	进行查看。如果不想要 集成包但是想体验 conda 的话，可以下载minconda 。

OK,下面介绍下 conda 的两大功能(包和环境管理)：

> Tips:一般了解功能先从最基础的增删改查以及协同操作的角度考虑

#### 包管理

> 增加包：

```
conda install pandas
```

> 删除包：

```
conda remove pandas
```

> 更新包：

```
conda update pandas
```

> 查询包：

```
conda search pandas
```

> 查看所有包

```
conda list
```
#### 虚拟环境管理

由于在开发过程中每个应用程序所依赖的开发环境可能不同，所以我们需要将每个应用程序的运行环境隔离开来，虚拟环境即 virtualEnv 则应运而生。


> 增加虚拟环境：

```
conda env create -n my_env numpy

```

> 删除虚拟环境：

```
conda remove -n my_env numpy

```

> 更新虚拟环境：

```

```

> 查询虚拟环境：

```
conda env list
```


> 进入虚拟环境：

```
source activate myenv
```




> 退出虚拟环境：

```
source deactivate myenv
```

##### 系统操作：共享环境 
> 导出当前环境 

 ```
 conda export env 文件名称.yaml
 ```
 
 
> 别人拿到环境文件，根据文件创建环境

```
conda create -f 文件名称.yaml

```

详情参考：[Anaconda多环境多版本python配置指导](https://www.jianshu.com/p/d2e15200ee9b)



### Jupter notebook

第一眼看到这玩意感觉和 markDown 没啥区别啊。后来看到了她可以运行代码才觉得屌爆了。其实早在 2015 年的时候 Github 就对Jup亚特r notebook 进行了支持。现在随便建立一个 Gist 保存后就可以看到 
由 (nbviewer)[https://nbviewer.jupyter.org/]渲染的页面。

这里给个 demo:
[HelloJupyter.ipynb](https://gist.github.com/MrLeion/73fbb5f2a72481676e3dca9ce2f27c69)

