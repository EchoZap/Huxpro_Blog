![DockerCheatSheet.png](https://imgs-dx3.pages.dev/blog_imgs/docker_command.png)

# 启动docker

```
sudo service docker start
```

# 授予 docker sudo 权限

在执行完上面的步骤后使用 docker 命令，可能遇到以下警告：

```bash
$ docker images

permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied
```

这是因为 docker 没有 root 的权限，通过以下命令授权即可解决：

```
sudo usermod -aG docker $USER
```

# 列出所有已下载镜像

```shell
docker images
```

# 列出当前所有容器

```shell
docker ps -a
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

# 进入正在运行的容器

```shell
docker exec -it <container_ID> /bin/bash
```

# 忘记运行容器时的挂载路径

在运行容器时通过 -v 指定了本机的目录，但是时间久远，记不清当时指定的挂载路径是哪里。

要找出已经运行的 Docker 容器的挂载卷（`-v` 指定的路径），你可以使用以下步骤：

运行以下命令来获取容器的详细信息，包括挂载卷的路径：

```bash
docker inspect <container_name_or_id>
```

# 在运行容器时分配内存

```bash
docker run --memory=<2g 或者 4g 可自行分配大小> <images_name_or_id>
```
