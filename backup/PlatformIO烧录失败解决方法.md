## 遭遇问题
​***platformIO一直卡在烧录程序中，导致开发版一直处于断电状态***
![问题](https://wowpb.pages.dev/file/de26c769e7e33ab9a64bb.png)


## 解决方法

将main.py里的这一行注释即可
![解决1](https://wowpb.pages.dev/file/09761eef7eccb03e78bf3.png)


该文件在以下路径
`~/.platformio/intel_mcs51/builder/main.py`
![解决2](https://wowpb.pages.dev/file/546b2d5e45c306275722c.png)
