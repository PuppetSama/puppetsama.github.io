---
date: '2017-04-01'
draft: false
title: Python 爬虫笔记（二）——编码转换与错误处理
url: /04/11/Python-爬虫笔记（二）——编码转换与错误处理/
---

序
-

在日常的Python学习中总是会遇到关于编码转换的问题。

Python 文件中的编码
-------------

Python 默认脚本文件都是 `ANSSII` 编码的，当文件中有非 `ANSSII` 编码范围内的字符是要在第一行或第二行指定编码声明： `# -*- coding=utf-8 -*-` 或者 `#coding=utf-8`，其他编码如：gbk、gb2312也可以；否则会出现

> SyntaxError: Non-ASCII character ‘\xe4’ in file test.py on line 3, but no encoding declared; see <http://www.python.org/peps/pep-0263.html> for details

Python 2.X 的字符编码设计逻辑
--------------------

Python 2.X 中字符串类型主要有两大类： `str` 和 `unicode`, 他们都是 basestring 的派生类；

* str 是某种编码（UTF-8，GBK等）类型的字符串
* unicode 是Unicode类型的字符串

在str的文档中有这样的一句话：

> The string data type is also used to represent arrays of bytes, e.g., to hold data read from a file.

也就是说在读取一个文件的内容，或者从网络上读取到内容时，保持的对象为str类型；如果想把一个str转换成特定编码类型，需要把str转为Unicode,然后从unicode转为特定的编码类型如：utf-8、gb2312等。

python 编码转换函数
-------------

通过Python的官方手册我们能够找到：

### str.decode 函数：

> str.decode([encoding[, errors]])
>
> Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding. errors may be given to set a different error handling scheme. The default is ‘strict’, meaning that encoding errors raise UnicodeError. Other possible values are ‘ignore’, ‘replace’ and any other name registered via codecs.register\_error(), see section Codec Base Classes.
>
> New in version 2.2.
>
> Changed in version 2.3: Support for other error handling schemes added.
>
> Changed in version 2.7: Support for keyword arguments added.

### str.encode 函数：

> str.encode([encoding[, errors]])
>
> Return an encoded version of the string. Default encoding is the current default string encoding. errors may be given to set a different error handling scheme. The default for errors is ‘strict’, meaning that encoding errors raise a UnicodeError. Other possible values are ‘ignore’, ‘replace’, ‘xmlcharrefreplace’, ‘backslashreplace’ and any other name registered via codecs.register\_error(), see section Codec Base Classes. For a list of possible encodings, see section Standard Encodings.
>
> New in version 2.0.
>
> Changed in version 2.3: Support for ‘xmlcharrefreplace’ and ‘backslashreplace’ and other error handling schemes added.
>
> Changed in version 2.7: Support for keyword arguments added.

在实际开发中，我们常常会遇到这种问题：

> UnicodeDecodeError: ‘gbk’ codec can’t decode bytes in position 30664-30665: illegal multibyte sequence

此类问题中，虽然已经获得了正确的unicode字符串了，但是由于此unicode字符串中包含了一个特殊字符。而此特殊字符，GBK字符集中没有，不存在，所以无法将对应的Unicode字符，编码为对应的GBK字符，所以出现UnicodeEncodeError，更无法打印出来。

如果对于这些特殊字符，你不是很关心，即使不显示也无所谓，但是希望剩下的，其他大多数的正常的字符都能显示。

即，忽略掉特殊字符，显示哪些能显示的字符， 那么可以改为：  
`s.decode('gbk', ‘ignore').encode('utf-8′)`

如上面的函数说明，因为decode的函数原型是 `decode([encoding], [errors=’strict’])`，可以用第二个参数控制错误处理的策略，默认的参数就是strict，代表遇到非法字符时抛出异常；

* 如果设置为ignore，则会忽略非法字符；
* 如果设置为replace，则会用?取代非法字符；
* 如果设置为xmlcharrefreplace，则使用XML的字符引用。

Python编码检测
----------

在使用Python抓取网页并进行分析时出现这个错误:

> UnicodeDecodeError: ‘utf8’ codec can’t decode byte 0xd6

原因是部分中文网站编码不是utf8, 因此需要进行编码判断

在引入编码自动识别前, 我们有两种途径获取网页的编码信息:

其一、通过服务器返回的 header 里的 charset 变量获取

其二、通过页面里的 meta 信息获取

正常情况下, 如果服务器或者页面有提供这两个参数, 而且参数是正确的, 那我们抓取网页时就不存在编码的问题了.

但是现实总是会难为我们这些程序员, 抓取网页时, 经常会出现以下几种情况:

1. 这两个参数缺失了
2. 这两个参数虽然都提供了，但是不一致
3. 这两个参数提供了，但是与网页实际的编码不一致

为了尽可能的自动的获取所有网页的编码，所以引入了编码自动识别

使用 `chardet` 可以很方便的实现字符串/文件的编码检测,例子如下:  

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7 ``` | ```  url = 'https://mm.taobao.com/json/request_top_list.htm?page=1'  headers = {  'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',  }  request = urllib2.Request(url, headers = headers)  response = urllib2.urlopen(request)  print(chardet.detect(response.read())) ``` |

运行结果：

```
{'confidence': 0.99, 'encoding': 'GB2312'}
```

其他中文乱码问题
--------

有时候，文本成功显示，但中文部分乱码，一般有两种可能：

### decode转码问题

目标文件或者目标网站的编码格式是否为自己输入的编码格式？另，如果gb2312的编码，使用decode转时出错，可以使用decode(‘gbk’)这个字符集来解决

### encode转码问题

将`unicode`转码成 ‘utf-8’格式时，在dos命令行中，会出现中文乱码情况，是因为dos命令行的编码格式为’gb2312’，此时将`unicode`转码成’gbk’格式即可。

参考于：

> <http://www.jianshu.com/p/53bb448fe85b#>  
> <http://www.crifan.com/summary_python_2_x_common_string_encode_decode_error_reason_and_solution/>  
> <http://zoeyyoung.github.io/python-chardet.html>