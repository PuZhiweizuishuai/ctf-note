# 简单逆向步骤

先 ExeInfope 查看软件版本，是32位还是64位

然后选择相应版本IDA

之后在 IDA 的 IDA View-A 页面搜索 flag


# Android 反编译基础

## 第一步：apk反编译得到程序的源代码、图片、XML配置、语言资源等文件

```bash
apktool d -f <安卓文件> -o output
```

## Apk反编译得到Java源代码

先将原来的apk文件解压得到 classes.dex 文件

之后使用 dex2jar 执行

```bash
d2j-dex2jar classes.dex
```

## 使用 jd-gui.exe 打开得到的 classes-dex2jar.jar 文件 
