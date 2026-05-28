---
date: '2017-08-01'
draft: false
title: 国内携程一日航线Python实现
url: /08/01/国内携程一日航线Python实现/
---

项目介绍
----

这是一个简单的小项目，可以用一句话来简单概括：

**爬取携程**当日航班信息**绘制**在**国内地图**上。

爬取信息
----

这里我采用的是Scrapy框架+Selenium动态爬取。

并没有什么可以需要注意的地方，不过有一点需要提醒一下。当使用chromedriver时，若是报错

> chromedriver executable needs to be in PATH

可以采用以下三种方法解决：

* 在环境变量中加入chromedriver位置
* 将代码改为

`driver = webdriver.Chrome('C:/path/to/chromedriver.exe')`

* 将chromedriver放置于目标位置，Linux为`/usr/bin/`，Windows为`PythonXX/Scripts/`

绘制地图
----

绘制地图使用的是Basemap包，而Basemap基于2.7，即正常情况下无法使用。  
通过[Python Extension Packages for Windows](http://www.lfd.uci.edu/~gohlke/pythonlibs/)可得到基于Py3的Basemap Package。

为了得到中国省份边界，可以通过[GADM](http://www.gadm.org/)获取数据，然后通过readshapefile()方法加载数据。

绘制航线
----

将地点与经纬度以字典方式传入`{'city'，[lon， lat]}`,根据获得数据用drawgreatcircle()进行绘制。

最后得到目标图片：

![AirLine](http://omjz7so35.bkt.clouddn.com/OF_FFSB%295%5DTK$E34%602S6%29FU.png)