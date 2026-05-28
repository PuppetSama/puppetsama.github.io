---
date: '2017-09-01'
draft: false
title: Python爬坑问题集合
url: /09/07/Python爬坑问题集合/
---

序
-

本文用于一些常见奇葩问题，致力于记录在 Python 开发过程中出现的各类问题。

---

### 1. Sublime Text 错误[Decode error - output not utf-8]

> 打开Python.sublime-build文件,并添加”encoding”:”cp936”这一行,保存即可

方法来源：<http://blog.csdn.net/wangtaoking1/article/details/41879187>

### 2. python3安装ssdb 错误importError: cannot import name ‘izip\_longest’

> itertools.izip在pyhton3中已被去掉了，zip成为内置的方法，返回的是迭代器 iterator， 而在python2 中返回的是列表 list。  
> 找到使用了 from itertools import izip\_longest 的文件，将 izip\_longest 改为 zip\_longest。

方法来源：<http://blog.csdn.net/a1368783069/article/details/51398625>