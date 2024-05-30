# Dangdang_GoodsSpider（当当网商品爬虫）

**注：** 本脚本编写于2024年4月，采用JS读取DOM内容实现爬取内容，如果当当网页面发生结构变化，此脚本可能不再有效。

本项目采用 `Selenium` 通过调用JS方式爬取当当网商品搜索页的商品列表数据，可以实现自动滚动页面到底部（使图片加载完整）、自动翻页（可以设置总页数）。

获取到的数据字段描述如下：

```
url: 商品图片URL
book_name: 商品名称
publish: 出版社名称
author: 作者名称
pub_date: 出版日期
```

## 使用方法

### 安装依赖

```shell
pip install selenium
pip install webdriver_manager
```

### 本地运行

```shell
python main.py
```

程序运行时，会自动打开一个 Chrome 窗口并访问当当网的商品搜索结果页面：

![image-20240530155455944](https://cdn.jsdelivr.net/gh/bochili/cdn3/202405301554031.png)

开始爬取内容时，会在项目目录下创建一个 `data.json` ，后续每页获取到的内容都会写入该文件：

![image-20240530154110365](https://cdn.jsdelivr.net/gh/bochili/cdn3/202405301541437.png)

## 代码修改

### 设置页数

此处设置循环次数即可：

```python
for i in range(1, 100):
```

### 设置关键词

关键词在 `main.py` 中的：

```python
keyword = "图书"
```

