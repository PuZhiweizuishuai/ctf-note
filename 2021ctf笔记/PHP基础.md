# PHP includ文件包含协议类型


php://filter与包含函数结合时，php://filter流会被当作php文件执行。所以我们一般对其进行编码，阻止其不执行。从而导致任意文件读取。

php://filter 伪协议文件包含读取源代码，加上read=convert.base64-encode，用base64编码输出，不然会直接当做php代码执行，看不到源代码内容。

?file=php://filter/read=convert.base64-encode/resource=flag.php


### php://

php://input 伪协议 + POST发送PHP代码 （不行）


### php://input

php:// — 访问各个输入/输出流（I/O streams）


### php://output

只写的数据流

php://output允许你以 print 和 echo 一样的方式 写入到输出缓冲区。


### php://filter

重点来了，php://filter 是一种元封装器， 设计用于数据流打开时的筛选过滤应用。

我们先看看它的语法：

```
resource=<要过滤的数据流>   //这个参数是必须的。它指定了你要筛选过滤的数据流。
read=<读链的筛选列表>       //该参数可选。可以设定一个或多个过滤器名称，以管道符（|）分隔。
write=<写链的筛选列表>      //该参数可选。可以设定一个或多个过滤器名称，以管道符（|）分隔。
<；两个链的筛选列表>        //任何没有以 read= 或 write= 作前缀 的筛选器列表会视情况应用于读或写链。
```

我们平时是这样利用它来读取任意文件的：

```
php://filter/read=convert.base64-encode/resource=flag.php
```

在这个payload里，convert.base64-encode就是一个过滤器,而flag.php就是要过滤的数据流，也就是要读取的文件。

转换过滤器 convert.*

convert.* 是PHP 5.0.0 添加的，作用顾名思义就是转换==

base64

convert.base64-encode和 convert.base64-decode使用这两个过滤器等同于分别用 base64_encode()和 base64_decode()函数处理所有的流数据。

字符串过滤器 string.*

这个过滤器的作用是对字符串进行各种转换。

有加密的，转换大小写的等等。


# PHP 对查询参数的处理


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


