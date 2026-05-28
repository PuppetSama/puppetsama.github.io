---
date: '2017-03-01'
draft: false
title: Android爬坑问题集合
url: /03/19/Android爬坑问题集合/
---

序
-

本文用于一些常见奇葩问题，致力于记录在 Android 开发过程中出现的各类问题。

---

### 1. Installation failed with message Failed to establish session

小米手机在用 Android Studio 运行程序时报错，错误信息为

> “Installation failed with message Failed to establish session”

仅需在开发者选项中将 MIUI 优化 关掉即可。

### 2. 无法成功实例化 NavigationView 中的 MenuItem 问题

在开发过程中，我需要在侧栏显示位置信息，结果 setTittle() 方法一直失效，最后发现是没有成功实例化目标 MenuItem。目标 Item 的实例化不应该采用以下形式

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7 ``` | ```  @Override  public boolean onCreateOptionsMenu(Menu menu) {  // Inflate the menu; this adds items to the action bar if it is present.  getMenuInflater().inflate(R.menu.drawer, menu);  mSelectSchool = menu.findItem(R.id.university_choose);  return true;  } ``` |

而应该是

|  |  |
| --- | --- |
| ```  1  2 ``` | ```  NavigationView mNavigationView = (NavigationView) findViewById(R.id.navigation_view);  mSelectSchool = mNavigationView.getMenu().findItem(R.id.university_choose); ``` |