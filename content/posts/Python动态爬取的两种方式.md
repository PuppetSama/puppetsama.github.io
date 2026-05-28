---
date: '2017-10-01'
draft: false
title: Python动态爬取的两种方式
url: /10/20/Python动态爬取的两种方式/
---

在不断爬取网站的同时，我们会发现有一些页面是动态生成的，无法简单的通过之前的做法获取的所需要的信息。所以我们需要新的爬取解析方式，目前流行的两大思路是**模拟浏览器行为爬取**和**动态页面逆向分析爬取**。

模拟浏览器行为爬取
---------

模拟浏览器行为爬取是最简单的方法，适用性也最广。

### Selenium与webdriver方式

这是最广泛的动态爬取方式之一，原因是简单无脑，然而效率感人，非常慢。其中webdriver主要使用PhantomJS，这是基于Webkit的无界面浏览器，能够在不可见的情况下完成浏览器的常用功能。

在使用过程中，如非熟练操作，请认真查阅[Selenium文档](http://selenium-python-zh.readthedocs.io/en/latest/index.html)和[PhantomJS文档](http://phantomjs.org/)。个人并不建议这种方式，不过如果是小范围的数据爬取可以尝试，比如爬取Instagram特定人物的图片或者[爬取携程一日航班信息](http://puppetkant.cn/2017/08/01/%E5%9B%BD%E5%86%85%E6%90%BA%E7%A8%8B%E4%B8%80%E6%97%A5%E8%88%AA%E7%BA%BFPython%E5%AE%9E%E7%8E%B0/)。

### 其他方式

除了以上所说的Selenium方式，还有Splash、PyV8、Ghost、execjs等，用法大同小异，只是写法有差异而已，参考查阅官方文档都可以简单应有，这里就不过多复述了。

动态页面逆向分析爬取
----------

> 任何动态产生的内容，要么是本地计算，要么是从服务器获取的。
>
> 前者看js，后者抓包。

爬虫爬取动态页面效率最高的是分析出请求数据的URL~~熟练运用F12便可以解决~~，在这里推荐一下网站分析工具[Charles](https://www.charlesproxy.com/)。

推荐大家可以以[简书的搜索页面](http://www.jianshu.com/search?q=%E6%89%8B%E5%B8%90&page=1&type=note)和[BiliBili的视频信息页面](https://www.bilibili.com/video/av15512174/)入手，十分简单易上手。具体代码就不贴了。~~才不是因为懒~~