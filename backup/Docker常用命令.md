![DockerCheatSheet.png](https://wowpb.pages.dev/file/38386b215292115008331.png)

# 列出所有已下载镜像
```shell
❯ docker images
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
ubuntu            latest    ffb64c9b7e8b   3 weeks ago     101MB
b3log/siyuan      latest    caf98195a3c3   3 weeks ago     220MB
soulteary/flare   latest    843d799dc8b2   2 months ago    12.8MB
hello-world       latest    ee301c921b8a   14 months ago   9.14kB
``` 

# 列出当前所有容器
```shell
❯ docker ps -a
CONTAINER ID   IMAGE     COMMAND                   CREATED              STATUS      
2295f62c584b   ubuntu    "/bin/sh -c 'while t…"   1 minute ago   Up About a minute
526462e8b92d   ubuntu    "/bin/bash"               44 minutes ago       Exited (0) 
``` 

输出详情介绍：
- **CONTAINER ID:**  容器 ID。
- **IMAGE:**  使用的镜像。
- **COMMAND:**  启动容器时运行的命令。
- **CREATED:**  容器的创建时间。
- **STATUS:**  容器状态。

状态有7种：
* created（已创建）
* restarting（重启中）
* running 或 Up（运行中）
* removing（迁移中）
* paused（暂停）
* exited（停止）
* dead（死亡）

**PORTS:**  容器的端口信息和使用的连接类型（tcp\udp）。
**NAMES:**  自动分配的容器名称。
