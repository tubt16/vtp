# Tạo Template theo yêu cầu

Thực hiện tạo một Item khác trong Template ở part 1, ở phần này mục tiêu cần tìm ra giới hạn số openfile của mỗi process và trả về process có tỉ lệ openfile/limit cao nhất 

Tạo một script có tên `checklim.sh` và cấp quyền thực thi cho file

```sh
touch checklim.sh

chmod +x checklim.sh
```

Thêm nội dung vào file `checklim.sh`

Nội dung của file như sau `checklim.sh`

```sh
#!/bin/bash
  
for pid in `ps --ppid 2 -p 2 --deselect | awk '{print $1}'`
do
        echo "$(sudo ls -l /proc/$pid/fd/ 2>/dev/null | wc -l ) for PID: $pid"
done
echo "--------------------------------------------------------"
echo "--------------------------------------------------------"

temp=$(
for pid in `ps --ppid 2 -p 2 --deselect | awk '{print $1}'`
do
        echo "$(cat /proc/$pid/limits 2>/dev/null | grep "Max open files" | awk '{print $4}') $(sudo ls -l /proc/$pid/fd/ 2>/dev/null | wc -l ) $pid $(awk "BEGIN {print $(sudo ls -l /proc/$pid/fd/ 2>/dev/null | wc -l )/$(cat /proc/$pid/limits 2>/dev/null | grep "Max open files" | awk '{print $4}')*100}" 2>/dev/null)"

done | sort -k 4 | tail -n 1)

maxLimitFile=$(echo $temp | awk '{print $1}')
openFile=$(echo $temp | awk '{print $2}')
processID=$(echo $temp | awk '{print $3}')
maxPersent=$(echo $temp | awk '{print $4}')
echo "Max limit file is: $maxLimitFile"
echo "Open file is: $openFile"
echo "Process ID: $processID"
echo "Process Name: $(ps -p $processID | awk '{print $4}' | tail -n 1)" 
echo "Max persent: $maxPersent %"
```

Chạy file `checklim.sh` để kiểm tra kết quả

**Output:**

```sh
root@buitu:/tmp# ./checklim.sh 
0 for PID: PID
73 for PID: 1
35 for PID: 168
14 for PID: 206
8 for PID: 321
21 for PID: 439
16 for PID: 443
9 for PID: 556
21 for PID: 575
10 for PID: 590
8 for PID: 601
11 for PID: 603
14 for PID: 607
5 for PID: 612
8 for PID: 754
11 for PID: 844
11 for PID: 859
5 for PID: 867
5 for PID: 873
24 for PID: 878
6 for PID: 885
9 for PID: 1376
2 for PID: 1377
6 for PID: 1580
13 for PID: 17793
30 for PID: 17797
8 for PID: 17798
5 for PID: 17895
7 for PID: 29281
7 for PID: 29282
7 for PID: 29283
7 for PID: 29284
7 for PID: 29285
7 for PID: 29286
37 for PID: 53969
13 for PID: 55794
5 for PID: 55893
13 for PID: 73636
5 for PID: 73732
6 for PID: 74898
0 for PID: 74899
0 for PID: 74900
0 for PID: 74901
--------------------------------------------------------
--------------------------------------------------------
Max limit file is: 1024
Open file is: 21
Process ID: 439
Process Name: systemd-network
Max persent: 2.05078
root@buitu:/tmp# vi checklim.sh 
root@buitu:/tmp# ./checklim.sh 
0 for PID: PID
73 for PID: 1
35 for PID: 168
14 for PID: 206
8 for PID: 321
21 for PID: 439
16 for PID: 443
9 for PID: 556
21 for PID: 575
10 for PID: 590
8 for PID: 601
11 for PID: 603
14 for PID: 607
5 for PID: 612
8 for PID: 754
11 for PID: 844
11 for PID: 859
5 for PID: 867
5 for PID: 873
24 for PID: 878
6 for PID: 885
9 for PID: 1376
2 for PID: 1377
6 for PID: 1580
13 for PID: 17793
30 for PID: 17797
8 for PID: 17798
5 for PID: 17895
7 for PID: 29281
7 for PID: 29282
7 for PID: 29283
7 for PID: 29284
7 for PID: 29285
7 for PID: 29286
37 for PID: 53969
13 for PID: 55794
5 for PID: 55893
13 for PID: 73636
5 for PID: 73732
6 for PID: 75972
0 for PID: 75973
0 for PID: 75974
0 for PID: 75975
--------------------------------------------------------
--------------------------------------------------------
Max limit file is: 1024
Open file is: 21
Process ID: 439
Process Name: systemd-network
Max persent: 2.05078 %
```

Kết quả trả về process `systemd-network`, process này chiếm `2.0.5078 %` số openfile trên tổng số limit file

Sau khi kiểm tra script đã chạy thành công, ta tiến hành tạo `Item`

Tạo một file chứa config khác

```sh
root@buitu:/tmp# cat /etc/zabbix/zabbix_agentd.conf | grep "Include"
### Option: Include
# Include=
Include=/etc/zabbix/zabbix_agentd.d/*.conf
# Include=/usr/local/etc/zabbix_agentd.userparams.conf
# Include=/usr/local/etc/zabbix_agentd.conf.d/
# Include=/usr/local/etc/zabbix_agentd.conf.d/*.conf
```

Chúng ta có thể tạo file bất kỳ với đuôi `.conf` trong đường dẫn `/etc/zabbix/zabbix_agentd.d/` để lưu config mà không cần phải chỉnh sửa trong file gốc của zabbix_agent 

```sh
vi /etc/zabbix/zabbix_agentd.d/tubt.conf
```

Tiến hành tạo User Parameter bằng cách thêm dòng sau vào file `tubt.conf` vừa tạo

```sh
root@buitu:/tmp# cat /etc/zabbix/zabbix_agentd.d/tubt.conf | grep UserParam
UserParameter=maxopenfile.per.maxlimitfile,/tmp/checklim.sh
```

Sau khi tạo xong User Parameter ta cần restart zabbix-agent để nhận config

```sh
systemctl restart zabbix-agent
```

Login Zabbix-server để kiểm tra

Chạy lệnh zabbix_get sau để kiểm tra

```sh
zabbix_get -s 34.125.127.154 -p 10050 -k "maxopenfile.per.maxlimitfile"
```

Trong đó:

- `-s`: Chỉ định hostname hoăc IP của zabbix-agent

- `-p`: Chỉ định port chạy Zabbix-agent (Mặc định là 10050)

- `-k`: Chỉ định `key-item` để lấy command

**Output:**

```sh
[root@centos7-zabbix ~]# zabbix_get -s 34.125.127.154 -p 10050 -k "maxopenfile.per.maxlimitfile"
0 for PID: PID
73 for PID: 1
35 for PID: 168
14 for PID: 206
8 for PID: 321
21 for PID: 439
16 for PID: 443
9 for PID: 556
21 for PID: 575
10 for PID: 590
8 for PID: 601
11 for PID: 603
14 for PID: 607
5 for PID: 612
8 for PID: 754
11 for PID: 844
11 for PID: 859
5 for PID: 867
5 for PID: 873
24 for PID: 878
6 for PID: 885
9 for PID: 1376
2 for PID: 1377
6 for PID: 1580
13 for PID: 17793
30 for PID: 17797
8 for PID: 17798
5 for PID: 17895
37 for PID: 53969
13 for PID: 55794
5 for PID: 55893
13 for PID: 73636
5 for PID: 73732
7 for PID: 77203
7 for PID: 77204
7 for PID: 77205
9 for PID: 77206
7 for PID: 77207
7 for PID: 77208
5 for PID: 78298
7 for PID: 78299
0 for PID: 78300
0 for PID: 78301
0 for PID: 78302
--------------------------------------------------------
--------------------------------------------------------
Max limit file is: 1024
Open file is: 21
Process ID: 439
Process Name: systemd-network
Max persent: 2.05078 %
```