# 老马你做天上星，iFan心里小甜心！
## mo-old-Ma
### 包含一个表情包生成和定时自动发送qq消息的Python3文件
##### 使用说明：
* 1、所有表情包由q.jpg生成，并直接根据月日存储在当前文件夹下，总计大小约为5Mb左右
* 2、先运行pi.py生成表情包，才能运行send.py
* 3、通过更改send.py中的时间限制可以更换定时发送的时间
* 4、运行send.py时需要确保qq消息窗口存在且只有“老马夸夸群”一个窗口存在
* 5、通过更改to_who变量改变要发送的好友/群
* 6、运行py程序前 必须先开启qq消息窗口，否则会发送失败
##### 使用的python库：
* 1、PIL：图像处理
* 2、win32：获取qq窗口句柄、剪切板等功能
* 3、datetime：获取当前日期和时间
##### 改进方向：
* 1、文件结构
* 2、自动后台运行
* 3、增加输入功能
##### 问题说明：
* 1、qqbot无法使用：smartqq停止使用后Tencent关闭了webqq导致没有可以直接操作qq的api可用，故这里使用了pywin32库来通过交互发送
* 2、新版本qq窗口可以重叠，此时无法获得句柄，故只有保证只有一个聊天窗口时程序才能正常运行
