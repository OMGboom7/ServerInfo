# Saltstack部署

+ `Salt`使用`server-agent`通信模型，服务端组件被称为`Salt master`，`agent`被称为`Salt minion`

+ `Salt master`主要负责向`Salt minions`发送命令，然后聚合并显示这些命令的结果。一个`Salt master`可以管理多个`minion`系统

+ `Salt server`与`Salt minion`通信的连接由`Salt minion`发起，这也意味着`Salt minion`上不需要打开任何传入端口

+ `Salt server`使用端口`4505`和`4506`，必须打开端口才能接收到访问连接

  