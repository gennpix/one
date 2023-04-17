# Redis

## 常用命令

```shell

# 连接数据库，默认连接 db 0
redis-cli
# 指定主机
redis-cli -h <hostname>
# 指定端口
redis-cli -p <port>
# 指定 db，比如 0 | 1 | 2 | ...
redis-cli -n <db>

# 查看所有键
127.0.0.1:6379> keys *
# 模糊查询
127.0.0.1:6379> keys *setting*
# 精确查询
127.0.0.1:6379> keys setting_sum
# 查看值：”get key
127.0.0.1:6379> get setting_sum
# 修改值：set key value [EX seconds|PX milliseconds] [NX|XX] [KEEPTTL]
127.0.0.1:6379> set setting_sum 123
# 删除： del key [key ...]
127.0.0.1:6379> del key1 key2 key3

# 查看连接数
127.0.0.1:6379> info clients
## Clients
# connected_clients:682
# client_recent_max_input_buffer:4
# client_recent_max_output_buffer:0
# blocked_clients:5
# tracking_clients:0
# clients_in_timeout_table:4

# 查询最大连接数
127.0.0.1:6379>CONFIG GET maxclients
# 1) "maxclients"
# 2) "10000"

# 查看所有连接
127.0.0.1:6379> CLIENT LIST
# 指定类型查看：normal|master|replica|pubsub
127.0.0.1:6379> CLIENT LIST TYPE replica
# id=20 addr=10.42.4.243:59420 fd=13 name= age=7897 idle=0 flags=S db=0 sub=0 psub=0 multi=-1 qbuf=0 qbuf-free=0 obl=0 oll=0 omem=0 events=r cmd=replconf user=default

# 杀死指定连接：CLIENT KILL ip:port
127.0.0.1:6379> CLIENT KILL 10.42.4.243:59420

# 执行命令(比如 info clients)后自动退出
redis-cli info clients
```
