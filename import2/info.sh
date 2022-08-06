#取所需要的内网IP
Int_ip=`ifconfig|awk '/inet addr/ {gsub(/:/," ");print $3}'|egrep "^192.168.18"|head -1`
#取除该内网ip以及127.0.0.1之外的所有ip
Out_ip_list=`ifconfig|awk '/inet addr/ {gsub(/:/," ");print $3}'|grep -v $Int_ip|grep -v 127.0.0.1`
#取内存总值，单位为G，四舍五入
Memory=`free -m|awk '/Mem/ {printf ("%.f\n",$2/1024)}'`
#取内存fr
ee值，从系统角度看，取的是第一行的free
Memory_free=`free -m|awk '/Mem/ {printf "%.f\n",$4/1024}'`
#取CPU核数
Cpu_num=`grep processor /proc/cpuinfo|wc -l`
#取服务器运行时间
Uptime=`uptime|awk '{print $3}'`
#取最近15分的负载
Load=`uptime|awk '{print $12}'`
#取磁盘大于80%的磁盘目录
Disk=`df -h|awk '{a=+$(NF-1);if(a>=80)print $NF}'`
#swap分区总值，单位为G，四舍五入
Swap=`free -m|awk '/Swap/ {printf ("%.f\n",$2/1024)}'`
#swap分区
Swap_free = `free -m|awk '/Swap/ {printf "%.f\n",$4/1024}'`
