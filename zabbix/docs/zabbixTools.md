# Zabbix_get

`zabbix_get` là tiện ích dòng lệnh để lấy dữ liệu từ tác nhân Zabbix

# Options

- `-s`, `--host`: Chỉ định hostname hoặc địa chỉ IP của máy chủ

- `-p`, `--port`: Chỉ định port của Zabbix Agent trên máy chủ. Mặc định là 10050

- `-I`, `--source-address`: Chỉ định địa chỉ IP nguồn

- `-t`, `--timeout`: Chỉ định thời gian chờ. Phạm vi hợp lệ là 1 - 30 giây (Mặc định 30)

- `-k`, `--key`: Chỉ định `key-item`để lấy giá trị

- `--tls-connect`: Cách kết nối tới agent

**Ví dụ:**

```sh
zabbix_get -s 34.125.127.154 -p 10050 -k "computer.linux.usercount[1]"
```

**Output:**

```sh
[root@centos7-zabbix ~]# zabbix_get -s 34.125.127.154 -p 10050 -k "computer.linux.usercount[1]"
72
```

**Một vài ví dụ khác:**

```sh
zabbix_get -s 127.0.0.1 -p 10050 -k "system.cpu.load[all,avg1]"
zabbix_get -s 127.0.0.1 -p 10050 -k "net.tcp.listen[80]"
zabbix_get -s 127.0.0.1 -p 10050 -k "agent.ping"
zabbix_get -s 127.0.0.1 -p 10050 -k "agent.version"
. . .
. . .
```