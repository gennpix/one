# 账户管理
##  创建用户

##  修改用户

##  删除用户

##  授权

### GRANT
```sql
grant all privileges on *.* to root@'localhost' identified by 'password';
grant all privileges on *.* to root@'192.168.1.100' identified by 'password';
grant all privileges on *.* to root@'192.168.1.%' identified by 'password';
grant all privileges on *.* to root@'%' identified by 'password';
-- 可以授权给别的用户
grant all privileges on *.* to root@'%' identified by 'password' with grant option;
--  指定db
grant all privileges on db.* to dbuser@'%' identified by 'password';
-- 添加权限
GRANT Insert ON db.* TO dbuser@'%';
-- 刷新权限（使生效）
flush privileges;
-- 只读用户
GRANT SELECT ON dbname.* TO 'username'@'%' IDENTIFIED BY "password";
```

grant all privileges on nacos_sync.* to nacos@'127.0.0.1' identified by 'nacos';
grant all privileges on nacos_sync.* to nacos@'localhost' identified by 'nacos';
grant all privileges on nacos_sync.* to nacos@'%' identified by 'nacos';
flush privileges;

### SHOW GRANTS
```sql
-- 查看当前用户下的所有权限
show grants;
-- 查看指定用户下的所有权限
show grants for root@'%';
show grants for root@'192.168.1.%';
-- 查全部
select user,host from mysql.user;
```

##  用户重命名

##  取消授权
```sql
revoke all privileges on *.* from 'root'@'%';
revoke usage on *.* from 'root'@'%';
flush privileges;
select user,host from mysql.user;
```

##  设置密码




## 参考文档
> [官方文档](https://dev.mysql.com/doc/refman/5.7/en/account-management-statements.html)