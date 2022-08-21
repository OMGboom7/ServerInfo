# 内网环境离线部署yum源

工作中系统通常都是部署在内网环境中，无法连接互联网，因此无法使用互联网上的YUM源。我们经常会遇到系统ISO镜像中软件包缺失，系统软件补丁无法升级，第三方软件包无法安装等情况。

+ 部署内网YUM源的目的主要是：
  1. 系统补丁升级
  2. 安装第三方软件包
  3. 安装额外的软件包

+ YUM源种类

  | 源名称  | 说明                                                         |
  | ------- | ------------------------------------------------------------ |
  | base    | 操作系统镜像源，包含了ISO镜像内的所有软件包                  |
  | updates | 包含了系统更新，升级的软件包                                 |
  | extras  | 扩充的软件包合集                                             |
  | epel    | EPEL (Extra Packages for Enterprise Linux)是基于Fedora的一个项目，为“红帽系”的操作系统提供额外的软件包，适用于RHEL、CentOS和Scientific Linux. |

+ 准备工作（以CentOs7为例，安装方式为带gnome桌面版本）

  1. 准备一台可以联网的Linux服务器

  2. 安装创建yum仓库的工具

     ```shell
     yum install createrepo yum-utils -y
     ```

  3. 移除其他镜像源

     ```shell
     mkdir /etc/yum.repos.d.bak
     mv /etc/yum.repos.d/* /etc/yum.repos.d.bak/
     ```

  4. 下载阿里云的repo文件

     ```shell
     wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
     wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
     ```

  5. 构建yum源缓存

     ```shell
     yum clean all
     yum makecache
     yum repolist
     ```

  6. 安装并启用httpd服务

     ```shell
     yum install httpd
     systemctl start httpd
     ```

+ 同步阿里云yum源到本地

  1. 在/var/www/html目录中创建一个yum目录，空间要足够大，本例中选择挂载一个独立的分区到/var/www/html/yum目录，镜像同步到本地，预计占用30G的空间。这里选择将目录存放在httpd服务的根目录（/var/www/html)，为后续搭建本地http yum仓库做准备。
  2. 同步镜像到本地目录

  ```shell
  #  #reposync根据之前下载的repo文件下载rpm包到指定文件夹
  cd /var/www/html/yum
  reposync -r base 
  reposync -r extras
  reposync -r updates
  reposync -r epel
  ```

+ 创建本地YUM仓库

  1. 为本地yum仓库，生成新的repo文件

     ```shell
     cd /var/www/html/yum/base
     createrepo ./
     cd /var/www/html/yum/extras
     createrepo ./
     cd /var/www/html/yum/updates
     createrepo ./
     cd /var/www/html/yum/epel
     createrepo ./
     ```

+ 更新YUM仓库

  到此本地YUM仓库搭建完成，如果在对应的仓库中加入新的软件包时，需要更新仓库

  ```shell
  createrepo --update /var/www/html/yum/epel
  ```

+ 离线YUM仓库的使用

  配置客户端主机的yum源配置文件，将YUM仓库指向该主机，即可正常使用该YUM仓库。客户端yum源配置文件如下：

  ```shell
  vim http.repo
  ###
  [base]
  name=RHEL- - Base - http
  baseurl=http://192.168.17.130/yum/base
  enabled=1
  gpgcheck=0
  
  [updates]
  name=RHEL- - updates - http
  baseurl=http://192.168.17.130/yum/updates
  enabled=1
  gpgcheck=0
  
  [epel]
  name=RHEL- - epel - http
  baseurl=http://192.168.17.130/yum/epel
  enabled=1
  gpgcheck=0
  
  [extras]
  name=RHEL- - extras - http
  baseurl=http://192.168.17.130/yum/extras
  enabled=1
  gpgcheck=0
  ###
  
  yum clean all
  yum makecache
  ```

