## 遭遇问题

***platformIO一直卡在烧录程序中，导致开发版一直处于断电状态***
![问题](https://imgs-dx3.pages.dev/blog_imgs/PIO1.png)

## 解决方法

将main.py里的这一行注释即可
![解决1](https://imgs-dx3.pages.dev/blog_imgs/PIO2.png)

该文件在以下路径
`~/.platformio/platforms/intel_mcs51/builder/main.py`
![解决2](https://imgs-dx3.pages.dev/blog_imgs/PIO3.png)
