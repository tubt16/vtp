# pwd command in Linux

pwd là viết tắt của Print Working Directory. Nó in đường dẫn của thư mục làm việc, bắt đầu từ thư mục gốc. pwd là lệnh tích hợp shell (pwd). $PWD là biến môi trường lưu trữ đường dẫn của thư mục hiện tại. Lệnh này có hai cờ.

**Cú pháp của lệnh pwd trong Linux**

```sh
pwd [OPTIONS]
```

Lệnh này không có bất kỳ đối số hoặc tùy chọn nào nhưng nó có thể chấp nhận 1 số tùy chọn cho hành vi cụ thể

Một số option cho hành vi cụ thể trong lệnh `pwd`

- `-L`: Giải quyết các liên kết tượng trưng và in đường dẫn của thư mục đích

- Hành vi mặc định của `pwd` được tích hợp mặc định trong shell tương đương với việc sử dụng `pwd -L`

- `-P`: Hiển thị đường dẫn thực tế mà không giải quyết các liên kết tượng trưng

- Hành vi mặc định của nhị phân "/bin/pwd" giống như sử dụng `pwd -P`

```sh
#Prints the symbolic path. 
pwd -L

#Prints the actual path.
pwd -P
```