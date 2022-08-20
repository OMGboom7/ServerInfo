### Grafana安装

Prometheus UI 提供了快速验证 PromQL 以及临时可视化支持的能力，但其可视化能力却比较弱。一般情况下，我们都用 Grafana 来实现对 Prometheus 的可视化

从 [官网](https://grafana.com/grafana/download) 下载对应系统的安装包，方便起见，这里用rpm包进行安装，下载安装后用命令启动

```shell
wget https://dl.grafana.com/enterprise/release/grafana-enterprise-9.1.0-1.x86_64.rpm
yum install grafana-enterprise-9.1.0-1.x86_64.rpm -y
systemctl start grafana-server.service
```

Grafana 默认使用 3000 端口启动，我们访问：[http://192.168.136.129:3000](http://192.168.136.129:3000/) 查看对应页面

![image-20220820191307107](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201913930.png)

默认的账号密码是 admin/admin，首次登陆需要修改默认密码，登陆后界面

![image-20220820191422906](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201914842.png)

### 配置数据源

去设置菜单添加 Prometheus 数据源

![image-20220820191506981](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201915908.png)

![image-20220820191613629](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201916020.png)

![image-20220820191632264](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201916353.png)

填写Prometheus地址，然后保存

![image-20220820191701401](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201917591.png)

![image-20220820191755602](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201917081.png)

提示保存成功

![image-20220820191818754](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201918633.png)

### 配置面板

在 Grafana 中有`Dashboard`和`Panel`的概念，`Dashboard `可以理解成`看板`，而 `Panel` 可以理解成`图表`，一个看板中包含了无数个图表

对于线上监控来讲，如果我们每个面板都需要自己从零开始，那么就太累了。事实上，我们用到的许多监控信息都是类似的。因此 [Grafana官网 - Dashboards 模块](https://grafana.com/grafana/dashboards) 提供了下载 Dashboard 模板的功能

![image-20220820192218181](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201922952.png)

Dashboards 里有许多各种类型的 Dashboard 面板，例如 JVM 监控、MySQL 数据库监控等。你只需找到合适自己的监控面板，之后根据 ID 添加即可，例如下图，外网环境下可以复制ID，内网环境下，可以下载json文件，然后导入![image-20220820192418672](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201924491.png)

+ 复制它的 ID 并使用 Grafana 的 import 功能导入

  ![image-20220820192547271](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201925192.png)

  ![image-20220820192656511](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201926765.png)

  数据源选择Prometheus，然后导入

  ![image-20220820192731793](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201927999.png)

  导入后即可显示服务器数据

  ![image-20220820192852617](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201928105.png)



+ 下载json导入

  ![image-20220820193027950](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201930298.png)

  复制json文件内容到导入面板中，加载后导入即可

  ![image-20220820193148266](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201931748.png)

### 推荐面板

[Linux主机详情](https://grafana.com/grafana/dashboards/12633-linux/)

![image-20220820193512467](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201935446.png)

![image-20220820193553293](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201935572.png)

 [1 Node Exporter for Prometheus Dashboard CN v20200628](https://grafana.com/grafana/dashboards/12884-1-node-exporter-for-prometheus-dashboard-cn-v20200628/)

![image-20220820193928827](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201939890.png)

![image-20220820193935282](https://raw.githubusercontent.com/OMGboom7/picbed/master/202208201939383.png)