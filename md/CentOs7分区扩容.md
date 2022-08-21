# CentOs7分区扩容

+ 查看当前分区`fdisk -l`，这里已经使用VM对硬盘进行扩容

  ![image-20220821175559557](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208211756738.png)

+ 在扩展硬盘VM虚拟机中

  ![image-20220821175805586](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208211758553.png)

+ 新建分区并保存，重启虚拟机后生效，否则会提示找不到分区文件

  ```
  a :设置可引导标记
  b :修改bsd的磁盘标签
  c :设置DOS操作系统兼容标记
  d :删除一个分区
  l :显示已知的分区类型，其中82为Linux swap分区，83为Linux分区
  m :显示帮助信息
  n :增加一个新的分区
  o :创建一个新的空白的DOS分区表
  p :显示磁盘当前的分区表
  q :退出fdisk程序，不保存任何修改
  s :创建一个新的空白的Sun磁盘标签
  t :改变一个分区的系统号码（比如把Linux Swap分区改为Linux分区）
  u :改变显示记录单位
  v :对磁盘分区表进行验证
  w :保存修改结果并退出fdisk程序
  x :特殊功能
  ```

  ![image-20220821180004055](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208211800480.png)

+ 格式化分区

  ```shell
  mkfs -t ext3 /dev/sda4
  ```

+ 挂载分区

  ```shell
  # 创建分区挂载的文件夹
  mkdir /data
  # 将分区挂载到data目录下
  mount /dev/sda4 /data
  ```

+ 查看挂载情况，这个挂载只是临时的，重启服务器之后又需要重新挂载，通过修改/etc/fstab文件使挂载永久有效

  ![image-20220821180535135](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208211805324.png)

+ 永久挂载

  ![image-20220821180628696](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208211806937.png)

