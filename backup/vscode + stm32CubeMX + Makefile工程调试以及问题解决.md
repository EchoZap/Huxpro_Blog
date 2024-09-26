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

# 使用 openocd + stlink 调试

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

# 使用 vscode 的 cortex-debug 调试

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
            "preLaunchTask": "openocd debug"
        }
    ]
}

```

然后在 main.c 里打上断点，按下`f5`或者在 vscode 顶栏依次点击`运行`->`启用调试` 即可。

# 遭遇问题

![issue](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_debug_issue1.png)

![issue](https://imgs-dx3.pages.dev/blog_imgs/vscode_stm32_debug_issue2.png)

# 解决方法

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

然后再次开启调试就可以完美运行了。
