#内建对象类型
数字、字符串、列表、元祖和字典

#内建函数/内置函数


#标准库
Python 标准库是大量强大编程工具的集合，可为你在 Python 中编程提供帮助。
从网络到数学统计，Python 标准库为一系列常见和专门任务提供新的对象类型和函数。
其他人已经编写了代码，并将其放入有用的“模块”（module）中，以供你在自己的代码中访问和使用。
使用 Python 标准库中的模块可轻松访问和使用现有代码，极大提升了你的编程能力！

#numpy（Numerical Python）
numpy是一个用python实现的科学计算包（NumPy系统是Python的一种开源的数值计算扩展）。包括：
1、一个强大的N维数组对象Array（这种工具可用来存储和处理大型矩阵，
比Python自身的嵌套列表（nested list structure）结构要高效的多（该结构也可以用来表示矩阵（matrix）））；
2、比较成熟的（广播）函数库；
3、用于整合C/C++和Fortran代码的工具包；
4、实用的线性代数、傅里叶变换和随机数生成函数。numpy和稀疏矩阵运算包scipy配合使用更加方便。
NumPy（Numeric Python）提供了许多高级的数值编程工具，如：矩阵数据类型、矢量处理，以及精密的运算库。
专为进行严格的数字处理而产生。多为很多大型金融公司使用，以及核心的科学计算组织如：
Lawrence Livermore，NASA用其处理一些本来使用C++，Fortran或Matlab等所做的任务。

#pandas（panel data data analysis）

**简介**
pandas是基于numopy的一种工具(同时也是python的一个数据分析包)，该工具是为了解决数据分析任务而创建的。
pandas纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。
pandas提供了大量能使我们快速便捷地处理数据的函数和方法。
你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一.

**数据结构**
Series：一维数组，与Numpy中的一维array类似。二者与Python基本的数据结构List也很相近，其区别是：List中的元素可以是不同的数据类型，而Array和Series中则只允许存储相同的数据类型，这样可以更有效的使用内存，提高运算效率。
Time- Series：以时间为索引的Series。
DataFrame：二维的表格型数据结构。很多功能与R中的data.frame类似。可以将DataFrame理解为Series的容器。以下的内容主要以DataFrame为主。
Panel ：三维的数组，可以理解为DataFrame的容器。

