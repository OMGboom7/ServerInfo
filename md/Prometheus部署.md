### 服务器信息

| IP              | 系统版本                      | CPU  | 内存 |
| --------------- | ----------------------------- | ---- | ---- |
| 192.168.136.129 | CentOS Linux release 7.9.2009 | 1    | 1    |
| 192.168.136.130 | CentOS Linux release 7.9.2009 | 1    | 1    |
| 192.168.136.131 | CentOS Linux release 7.9.2009 | 1    | 1    |

关闭服务器防火墙，禁用防火墙

```shell
systemctl stop firewalld.service
systemctl disable firewalld.service
```

### 安装运行 Prometheus 服务端（监控机）

从 [官网](https://prometheus.io/download/) 找到稳定版本的Prometheus Sevrer软件包

![image-20220820180837915](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201808183.png)

通过命令下载并解压，在内网环境下需手动下载后手动上传到服务器

```shell
wget https://github.com/prometheus/prometheus/releases/download/v2.37.0/prometheus-2.37.0.linux-amd64.tar.gz
tar xf prometheus-2.37.0.linux-amd64.tar.gz
```

解压后目录如下

![image-20220820183055053](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201830755.png)

后台启动命令，输入 `http://localhost:9090/graph` ，这个是 Prometheus 自带的监控管理界面

```shell
nohup ./prometheus &
```

![image-20220820183657913](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201836050.png)

### 安装运行 NodeExporter 客户端数据源（所有被监控机）

从 [官网](https://prometheus.io/download/) 找到稳定版本的NodeExporter软件包

NodeExporter 是 Prometheus 提供的一个可以采集到主机信息的应用程序，它能采集到机器的 CPU、内存、磁盘等信息

![image-20220820183913912](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201839297.png)

通过命令下载并解压运行，在内网环境下需手动下载后手动上传到服务器

```shell
wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz
tar xf node_exporter-1.3.1.linux-amd64.tar.gz
# 后台运行
nohup ./node_exporter &
# 后台运行并指定端口(IP、端口自行更换)
nohup ./node_exporter --web.listen-address 192.168.3.129:5050 &
```

访问`http://192.168.3.129:5050`

![image-20220820184920253](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201849496.png)

访问`http://192.168.136.129:5050/metrics`，可以看到当前 node exporter 获取到的当前主机的所有监控数据

![image-20220820184948684](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201849839.png)

### 配置 Prometheus 的监控数据源

现在运行了 Prometheus 服务器，也运行了业务数据源 NodeExporter。但此时 Prometheus 还获取不到任何数据，还需要配置下 prometheus.yml 文件，让其去拉取 Node Exporter 的数据

配置一下 Prometheus 的配置文件，让 Prometheus 服务器定时去业务数据源拉取数据。编辑prometheus.yml 并在 scrape_configs 节点下添加以下内容，然后重启服务

![image-20220820185857499](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201858749.png)

然后在网页中检查是否获取到所有节点信息，节点状态显示为`UP`即连接正常

![image-20220820190032225](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201900740.png)

![image-20220820190054027](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201900982.png)

接下来，就可以查看 NodeExporter 节点所在机器各项信息，例如 CPU 1 分钟的负载情况，输入 `node_load1` ，点击`Execute`即可

![image-20220820190607650](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201906537.png)