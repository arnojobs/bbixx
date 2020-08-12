# H5 Navigation Generator

使用Jinja2的模板引擎生成一个简单的纯静态导航首页，方便部署于家庭网络或者内部服务器上，使用效果如下：

![image-20200525155023118](./imgs/image-20200525155023118.png)

其中的图标可到[font awesome](http://www.fontawesome.com.cn/faicons/)上参考，不指定时默认使用`fa fa-edge`样式。

## 使用

`python navupd.py`

```
verbose:False
generated: "index.html"
deployment: Use scp/sftp/ftp to upload file "index.html", directories "css" and "webfonts" to web directory of your web server.
```

![image-20200525151225700](./imgs/image-20200525151225700.png)

将生成的`index.html`更新到服务器中即可。如果是第一次部署，请连同`css`、`webfonts`这2个目录一起上传，再次访问服务器地址即可看到更新的内容，建议连同脚本一起上传到服务器，在服务器端即可完成首页链接的更新。

## 更新

按如下说明在服务器端修改navupd.py：

```python
# 实例化H5Navigation对象
h5 = H5Navigation()
# 取消回显
h5.set_verbose(False)
# 设置标签页标题
h5.set_head_title('THIS IS HEAD TITLE')
# 设置大标题
h5.set_main_title('THIS IS MAIN TITLE')
# 设置小标题
h5.set_sub_title('THIS IS SUB TITLE')
# 设置导航内容，参数为二维列表，二层列表的元素顺序依次为链接标题、链接内容和链接图标，不填写则为默认。
h5.set_navigations([['WEB1'], ['百度', 'http://www.baidu.com'], ['Facebook']])
# 更新到index.html
h5.generate()
```

本来想做成读取json文件的模式，但是暂时这也够用，欢迎大家自行提交commit。

## 引用

类H5Navigation存在于`libs/navupd`中，包含如下几个方法：

- set_verbose：开启详细输出
- set_head_title：设置标签页标题
- set_main_title：设置大标题
- set_sub_title：设置小标题
- set_navigations：设置导航项目内容
- check：检查数据
- generate：更新首页文件（默认为index.html）

## 其他

源模板只能实现7个导航内容，与css样式相关，希望前端童鞋可以研究研究，更新为任意个导航内容添加的css。