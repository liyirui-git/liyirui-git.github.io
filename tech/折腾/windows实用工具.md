# Windows 实用工具

### 1. QtScrcpy

QtScrcpy是在开源项目 [Scrcpy](https://github.com/Genymobile/scrcpy) 的基础上，利用Qt重构，加入了可视化界面，其GitHub地址：[QtScrcpy](https://github.com/barry-ran/QtScrcpy/) 

#### 介绍

QtScrcpy可以通过USB(或通过TCP/IP)连接Android设备，并进行显示和控制。**不需要root权限**。单个应用程序最多支持16个安卓设备同时连接。而且，**同时支持GNU/Linux，Windows和MacOS三大主流桌面平台**。

它专注于:

- **精致** (仅显示设备屏幕)
- **性能** (30~60fps)
- **质量** (1920×1080以上)
- **低延迟** ([35~70ms](https://github.com/Genymobile/scrcpy/pull/646))
- **快速启动** (1s内就可以看到第一帧图像)
- **非侵入性** (不在设备上安装任何软件)

[![win](windows实用工具.assets/win.png)](https://github.com/barry-ran/QtScrcpy/blob/master/screenshot/win.png)

[![mac](windows实用工具.assets/mac.jpg)](https://github.com/barry-ran/QtScrcpy/blob/master/screenshot/mac.jpg)

[![linux](windows实用工具.assets/ubuntu.png)](https://github.com/barry-ran/QtScrcpy/blob/master/screenshot/ubuntu.png)



#### 建议

如果能想办法加入文件互传和声音传输就好了。