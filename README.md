# Beatrice

1、音频上传功能
主要处理音频上传，上传的音频会生成一个md5值的音频。
例如：您好上传的音频为“都是夜归人.mp3”，该程序会将改文件重命名为“md5.mp3”

2、API接口功能

API接口主要是处理图片和文件上传的API接口
如果你要上传图片，可以访问http://ip:port/img

如果你要上传音频获取其他文件，可以访问http://ip:port/media

3、后续增加批量执行的功能
基于当前最流行的（salt、ansible、paramiko）

4、使用
默认使用的数据库是sqlite
启动： python manage.py runnserver
数据库迁移：python manage.py makemigrations; python manage.py migrate

5、如果你git clone下来使用代码库里面的sqlite数据库，默认的用户和密码：farmer@163.com/redhat

6、缺陷

本程序在css、js方面尚未做细致的网络优化、后续将做优化

7、增加ldap认证
