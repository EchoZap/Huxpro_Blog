# 1.建立 Makefile 工程

通过 STM32CubeMX 建立适于自己开发版的 Makefile 工程（步骤不赘述，百度一下，你就知道），并且记住「**工程名**」和「**工程存放路径**」。

# 2.新建 platformIO 工程

新建 platformIO 工程时的「Framework」**一定要选择「STM32Cube」**，新建工程的「**工程名**」和「**工程存放路径**」要与之前建立的 Makefile 工程**一致**。

工程建立完成后，你应该会得到如下项目结构：

```shell
├── Core
│   ├── Inc
│   │   ├── gpio.h
│   │   ├── main.h
│   │   ├── ...
│   └── Src
│       ├── gpio.c
│       ├── main.c
│       ├── ...
├── Drivers
│   ├── CMSIS
│   │   ├── Device
│   │   │   └── ST
│   │   │       └── STM32F1xx
│   │   │           ├── Include
│   │   │           │   ├── stm32f103xb.h
│   │   │           │   ├── stm32f1xx.h
│   │   │           │   └── system_stm32f1xx.h
│   │   │           ├── LICENSE.txt
│   │   │           └── Source
│   │   │               └── Templates
│   │   ├── Include
│   │   │   ├── cmsis_armcc.h
│   │   │   ├── cmsis_armclang.h
│   │   │   ├── cmsis_compiler.h
│   │   │   ├── cmsis_gcc.h
│   │   │   ├── ...
│   │   └── LICENSE.txt
│   └── STM32F1xx_HAL_Driver
│       ├── Inc
│       │   ├── Legacy
│       │   │   └── stm32_hal_legacy.h
│       │   ├── stm32f1xx_hal.h
│       │   ├── stm32f1xx_hal_cortex.h
│       │   ├── stm32f1xx_hal_def.h
│       │   ├── ...
│       ├── LICENSE.txt
│       └── Src
│           ├── stm32f1xx_hal.c
│           ├── stm32f1xx_hal_cortex.c
│           ├── stm32f1xx_hal_dma.c
│           ├── ...
├── Makefile
├── STM32F103C8Tx_FLASH.ld
├── include
│   └── README
├── lib
│   └── README
├── one.ioc
├── platformio.ini
├── src
├── startup_stm32f103xb.s
└── test
    └── README
```

# 3.配置工程

- 修改 platformio.ini

在 **platformIo.ini**中添加：

```shell
;烧录方式，有 jlink、stlink 以及 serial 等方式，根据自身情况选择
upload_protocol = stlink

[platformio]
src_dir = Core/Src
include_dir = Core/Inc
```

- 精简结构

删除工程根目录下的「src」和「include」文件夹

好了！现在点击 **build** ，没有报错，可以完美运行了！！！

# 4.添加自己的库

在 platformIO 建立的工程中，根目录下有一个 lib 文件夹，这里就可以存放自己的库。

示例：假设现在有一个 led.c 和 led.h，那么你就可以**在 lib 目录中新建一个 led 目录**，然后将 led.c 和 led.h 放到 ./lib/led 中，之后，在 ./Core/Src/main.c 中直接导入 led.h

```c
#include <led.h>

int main (void)
{
  ...
}

```
