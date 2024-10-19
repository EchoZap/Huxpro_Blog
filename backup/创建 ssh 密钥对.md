# 1.创建密钥对（此方法适用于从未创建过密钥对的本地主机）
在终端输入以下命令:

```
ssh-keygen
```

之后一路回车，不出意外的话，看到以下画面，密钥（包含私钥和公钥，公钥以 .pub 结尾）就创建成功了
![ssh-kegen](https://imgs.ronan.us.kg/ssh-keygen.png)

对于 linux 和类 linux 系统，该密钥存放于 `~/.ssh/` ，可以通过 `ls ～/.ssh` 查看。

# 2.创建多个密钥对
有时候可能会需要多个密钥对，但是又不想影响到之前已创建的密钥对

```
ssh-keygen -t ed25519 -C "这里写注释" -f ~/.ssh/id_ed25519_new_name
```

`ssh-keygen`：这是一个用于生成、管理和转换 SSH 密钥的命令行工具。  
`-t ed25519`：指定要生成的密钥类型为 ed25519。这种类型的密钥被认为更安全，并且通常生成更快。  
`-C "这里写注释"`：这是一个注释（通常使用邮箱，但是我不喜欢），用于标识这个密钥的用途。  
`-f ~/.ssh/id_ed25519_new_name`：指定生成的密钥文件的存储路径和名称。在这里，密钥会被保存为 ~/.ssh/id_ed25519_new_name，私钥为 id_ed25519_new_name，而公钥则为 id_ed25519_new_name.pub。

# 3. 配置 `~/.ssh/config` 文件（以 GitHub 为例）
为了方便管理不同的 SSH 密钥，可以在 `~/.ssh/config` 文件中为每个密钥配置别名。打开并编辑 `~/.ssh/config` 文件，添加如下内容：

```bash
# 默认 SSH 配置
Host github.com
	HostName ssh.github.com
	User git
	Port 443
	IdentityFile ~/.ssh/id_ed25519

# 为另一个服务或项目的 SSH 配置
Host github_new
	HostName ssh.github.com
	User git
	Port 443
	IdentityFile ~/.ssh/id_ed25519_new_name
```

在这个例子中，`github_new` 是自定义的别名，用于指定不同的 SSH 密钥。当你使用该别名连接 GitHub 时，会使用 `~/.ssh/id_rsa_new` 这个密钥。
