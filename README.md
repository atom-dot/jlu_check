# 环境配置

* Anaconda

  1. 安装[Anaconda](https://www.anaconda.com/products/individual)。因为安装包比较大，所以就没放安装包，需要自行去官网下载安装。

  2. 创建python环境：打开Anaconda Promopt，运行以下命令

     ```
     conda create -n <your_env_name> python=3.6
     ```

     其中<your_env_name>是自己要创建的python环境名称

* Chrome

  1. 安装Chrome浏览器
  2. 对应chrome版本下载[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/home)，并将其放到对应python环境的Scripts文件夹下。

* python库

  * 如果安装了Anaconda，打开Anaconda Promopt，运行以下命令

    ```
    conda activate <your_env_name>
    conda install requests -y
    conda install selenium -y
    conda install schedule -c jholdom -y
    ```

  * 如果没有安装Anaconda，则可以通过pip安装

    ```
    pip install requests
    pip install selenium
    pip install schedule
    ```

  

# 程序文件配置

整个程序分为两部分：一部分是jlu_check模拟登录打卡，一部分是upload_screenshot上传打卡截图，其中一些配置内容需要根据个人情况做修改

* 模拟打卡相关部分（程序19-23行）
  需要根据个人信息做修改，示例如下：

  ```python
  user_name = "wangjy19" # 自己的校园网用户名
  password = "123456" # 自己的校园网密码
  JLU_CHECK_URL = "https://ehall.jlu.edu.cn/jlu_portal/index" # 健康打卡系统登录页URL，这个不需要修改
  SAVE_PATH = '.' # 打卡截图的保存路径，默认'.'即为程序当前路径，
  ```

* 截图上传部分（程序28-29行）
  如果不需要截图上传功能则不需要修改这一部分。
  主要是为了方便班级负责人统计班内同学打卡情况。这一部分利用了XZC上传到百度网盘中，需要根据班级负责人给定的的XZC的URL进行填写。而st_number和st_name部分就填写个人的姓名和学号，示例如下：

  ```python
  # 假如我的XZC的URL链接是http://www.xzc.cn/x877ZRj111
  # 那么就分成两部分XZC_URL和XZC_CODE
  st_number = "2019548063" # 学号
  st_name = "张三" # 姓名
  XZC_URL = "http://www.xzc.cn/"
  XZC_CODE = "x877ZRj111"
  ```

  其中XZC是一个群收取文件并保存到百度网盘中的第三方工具，班级负责人如果有统计打卡情况的需求，则需要注册XZC账号并发放收取文件的链接。





# 程序运行使用

打开Anaconda Promopt并进入到程序所在文件夹

运行如下命令可完成一次打卡

```
python .\everyday_check.py 
```

如果有截图并上传的需求，需要加上`--screenshot`参数。如果具有每天定时打卡的需求，需要加上`--everyday`参数。如：

```
python .\everyday_check.py --screenshot --everyday
```