#取所需要的内网IP
server_ip=$( ifconfig -a | grep inet | grep -v inet6 | grep -v 127.0.0.1 | awk '{print $2}')
echo server_ip
#取内存总值，单位为G，四舍五入
memory=$(free -m|awk '/Mem/ {printf ("%.f\n",$2/1024)}')
echo memory
#内存使用率
memory_usage=
#取CPU核数
# shellcheck disable=SC2126
Cpu_num=$(grep processor /proc/cpuinfo|wc -l)
#CPU使用率
cpu_usage=$(top -n 1 | grep Cpu |awk '{print $2}'| awk '{print int($0)}')
#取服务器运行时间
Uptime=$(uptime|awk '{print $3$4}')
#取负载
Load=$(uptime|awk '{print $11$12$13}')
#取磁盘大于80%的磁盘目录
Disk=$(df -h|awk '{a=+$(NF-1);if(a>=80)print $NF}')
#swap分区总值，单位为G，四舍五入
Swap=$(free -m|awk '/Swap/ {printf ("%.f\n",$2/1024)}')
#swap分区
Swap_free = $(free -m|awk '/Swap/ {printf "%.f\n",$4/1024}')
