---
date: '2017-05-01'
draft: false
title: Python 爬虫笔记（三）——对于Lambda的认识
url: /05/09/Python-爬虫笔记（三）——对于Lambda的认识/
---

序
-

在一些Python优秀项目中总是能看到Lambda的影子，但自己在实际编程过程中并没有用到过，所以决定学习一下。

Anonymous
---------

> The Python lambda statement is an anonymous or unbound function and a pretty limited function at that.

首先来说，lambda函数通常被称之为匿名函数，那么大家估计对于lambda的基本用法就有了一个大致轮廓。

通常是在需要一个只用一次的函数，又不想费神去命名一个函数的场合下使用，这也是大多数人认为lambda是一个语法糖的原因。

举个例子，将一个`list`里的每个元素都进行平方：

|  |  |
| --- | --- |
| ```  1 ``` | ```  map（lambda x:x*x, [y for y in range(10)] ``` |

可以看出，`lambda x:x*x`实际上是：

|  |  |
| --- | --- |
| ```  1  2 ``` | ```  def f(x):  return x*x ``` |

然而，和其他很多语言相比，Python 的 lambda 限制多多，最严重的当属它只能由一条表达式组成。这个限制主要是为了防止滥用，因为当人们发觉 lambda 很方便，就比较容易滥用，可是用多了会让程序看起来不那么清晰，毕竟每个人对于抽象层级的忍耐 / 理解程度都有所不同。

Closure
-------

> A closure—unlike a plain function pointer —allows a function to access those non-local variables even when invoked outside of its immediate lexical scope.

闭包是指将当前作用域中的变量通过值或者引用的方式封装到lambda表达式当中，成为表达式的一部分，它使你的lambda表达式从一个普通的函数变成了一个带隐藏参数的函数。

我们可以粗暴地理解为**闭包就是一个定义在函数内部的函数**，闭包使得变量即脱离了该函数作用域范围也依然能被访问到。

例如：

|  |  |
| --- | --- |
| ```  1  2  3  4  5 ``` | ```  def f(n):  return lambda x:x+n    f_1 = f(1)  print(f_1(2)) ``` |

得到结果为`3`

附
-

对于Python来说，省名字和写到一行是次要的，重点在于嵌入到表达式里面。

lambda的使用大量简化了代码，使代码简练清晰。但是值得注意的是，这会在一定程度上降低代码的可读性。

lambda 并不会带来程序运行效率的提高，只会使代码更简洁。

如果使用lambda，lambda内不要包含循环，如果有，为了使代码获得可重用性和更好的可读性，还是应该选择自定义函数。