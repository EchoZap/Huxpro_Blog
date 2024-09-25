---
layout: post
title: "vscode + stm32CubeMX + Makefile 开发环境解决(红色波浪线)路径包含以及宏定义问题"
author: "Ronan"
header-style: text
tags:
  - docs
  - bug
---

1.在 STM32CubeMX 配置好工程之后，选择 Makefile 导出。

![建立并导出工程](https://imgs-dx3.pages.dev/blog_imgs/cubemx_makefile_project.png)

2.使用 vscode 打开该工程目录，点开`./Core/Src/main.c`，你会发现：满是令人高血压的红色波浪线，难以忍受

![红色波浪线](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_makefile_config1.png)


---

解决方法：

1.在工程目录中按下(macos)`cmd+shift+p`，(windows)`ctrl+shift+p`，输入C/C++然后点击`Edit Configurrations(JSON)`选择

![创建 cpp_json](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_makefile_config2.png)

2.接下来 vscode 会在你的工程根目录下创建一个.vscode目录和一个 c_cpp_properties.json ，默认情况下你在 c_cpp_properties.json 会看到以下内容

![ cpp_json](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_makefile_config3.png)

3.打开工程根目录的`Makefile`，找到`#C defines`（也就是宏定义这部分），然后`复制绿色框里的内容`

![Makefile](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_makefile_config4.png)

4.回到`c_cpp_properties.json`，将上面复制的内容按以下格式粘贴到`"defines"`的中括号里，如果` includePath`选项没有默认创建，你也可以自行手动添加，就像下面这样：

![c_cpp_properties.json](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_makefile_config5.png)
