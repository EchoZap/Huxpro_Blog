通过 STM32CubeMX 建立的 Makefile 工程，应该会有以下结构：

```shell
❯ tree test
test
├── Core
│   ├── Inc
│   └── Src
├── Drivers
│   ├── CMSIS
│   │   ├── Device
│   │   │   └── ST
│   │   │       └── STM32F1xx
│   │   │           ├── Include
│   │   │           ├── LICENSE.txt
│   │   │           └── Source
│   │   │               └── Templates
│   │   ├── Include
│   │   └── LICENSE.txt
│   └── STM32F1xx_HAL_Driver
│       ├── Inc
│       │   ├── Legacy
│       ├── LICENSE.txt
│       └── Src
├── Makefile
├── STM32F103C8Tx_FLASH.ld
├── build
├── startup_stm32f103xb.s
└── test.ioc
```

# 创建工程并去掉警告(红色波浪线)

> vscode 需要提前安装 C/C++ 插件

1.在 STM32CubeMX 配置好工程之后，选择 Makefile 导出。

![建立并导出工程](https://imgs-dx3.pages.dev/blog_imgs/cubemx_makefile_project.png)

2.使用 vscode 打开该工程目录，点开`./Core/Src/main.c`，你会发现：满是令人高血压的红色波浪线，难以忍受

![红色波浪线](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_makefile_config1.png)

---

解决方法：

1.在工程目录中按下(macos)`cmd+shift+p`，(windows)`ctrl+shift+p`，输入 `C/C++` 然后点击`Edit Configurrations(JSON)`选择

![创建 cpp_json](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_makefile_config2.png)

2.接下来 vscode 会在你的工程根目录下创建一个.vscode目录和一个 c_cpp_properties.json ，默认情况下你在 c_cpp_properties.json 会看到以下内容

![ cpp_json](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_makefile_config3.png)

3.打开工程根目录的`Makefile`，找到`#C defines`（也就是宏定义这部分），然后`复制绿色框里的内容`

![Makefile](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_makefile_config4.png)

4.回到`c_cpp_properties.json`，将上面复制的内容按以下格式粘贴到`"defines"`的中括号里，如果` includePath`选项没有默认创建，你也可以自行手动添加，就像下面这样：

![c_cpp_properties.json](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_makefile_config5.png)


# 工程调试
## 使用 openocd + stlink 调试

> 以stm32f103举例

1.在终端输入

```shell
openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg
```

2.**保持上面的终端不要退出，然后开启一个新的终端窗口**，输入以下命令就可以进入 gdb 调试：

```shell
❯ arm-none-eabi-gdb -q .../build/<your_project>.elf
Reading symbols from .../build/<your_project>.elf...
(gdb)
```

接着输入`target remote: 3333`，看见以下内容就可以开始调试了:

```zsh
❯ arm-none-eabi-gdb -q ./build/test.elf
Reading symbols from ./build/test.elf...
(gdb) target remote: 3333
Remote debugging using : 3333
```

## 使用 vscode 的 cortex-debug 插件调试

> 使用此方法，vscode 需要安装 cortex-debug 插件

先看效果;

![debug](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_debug.png)

实现方法：

在工程根目录下的`.vscode`目录（如果没有该目录可自行创建）中新建一个`launch.json`，其内容：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Cortex Debug",
            "cwd": "${workspaceRoot}",
            "executable": "build/test.elf", //根据自己工程实际生成最终.elf 路径修改
            "request": "launch",
            "type": "cortex-debug",
            "servertype": "openocd",
            "configFiles": [  //根据自己开发版以及调试器修改
                "interface/stlink-v2.cfg",
                "target/stm32f1x.cfg"
            ],
            "armToolchainPath": "/opt/arm-none-eabi/bin",
        }
    ]
}

```

然后在 main.c 里打上断点，按下`f5`或者在 vscode 顶栏依次点击`运行`->`启用调试` 即可。

## 调试遭遇问题

调试一直卡在 `HAL_Init` 函数里...

![issue](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_debug_issue1.png)

![issue](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_debug_issue2.png)

---

解决方法

1.打开`.../<Your_Project>/Core/Src/stm32f1xx_hal_msp.c`，在其中找到`HAL_MspInit`函数，默认情况下，函数内部是这样的：

```c
void HAL_MspInit(void)
{
  __HAL_RCC_AFIO_CLK_ENABLE();
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_AFIO_REMAP_SWJ_NOJTAG();
}
```

2.将`HAL_MspInit`函数内部的`__HAL_RCC_PWR_CLK_ENABLE()`和`__HAL_AFIO_REMAP_SWJ_NOJTAG()`这两个函数注释，就像这样：

```c
void HAL_MspInit(void)
{
  __HAL_RCC_AFIO_CLK_ENABLE();
  // __HAL_RCC_PWR_CLK_ENABLE();
  // __HAL_AFIO_REMAP_SWJ_NOJTAG();
}
```

然后 `打开终端把之前的调试任务全部停止` -> `再次 make ` -> `重新启动调试` 。

> 如需要减少编译优化等级，可以进入makefile，在 `if DEBUG` 判断的编译流程添加 `-O0` ,之后重新 `make DEBUG=1` 

