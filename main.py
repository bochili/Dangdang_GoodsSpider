import json
import os
from time import sleep

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
keyword = "图书"
# 打开开发者调试
option = webdriver.ChromeOptions()
# 开启开发者工具（F12）
option.add_argument("--auto-open-devtools-for-tabs")
driver = webdriver.Chrome(options=option,service=ChromeService(ChromeDriverManager().install()))
# 打开网页
i = 1
for i in range(1, 100):
    url = f'https://search.dangdang.com/?key={keyword}&act=input&show=list&page_index={i}&show_shop=0#J_tab'  # 指定网页的 URL
    driver.get(url)
    # 执行 JavaScript 脚本
    script = '''
    var data = []
    function scrollToBottom() {
      const currentPosition = window.pageYOffset; // 当前滚动位置
      const windowHeight = window.innerHeight; // 窗口高度
      const documentHeight = document.documentElement.scrollHeight; // 文档总高度

      if (currentPosition + windowHeight < documentHeight) {
        // 如果当前滚动位置加上窗口高度小于文档总高度，则继续滚动
        window.scrollTo(0, currentPosition + windowHeight);
        setTimeout(scrollToBottom, 100); // 每隔100毫秒滚动一次
      }
    }
    function a(){
        scrollToBottom()
        setTimeout(()=>{
            data = [];
            for(let el of document.querySelector(".bigimg").querySelectorAll("li")){
                data.push({
                    url:el.querySelector("img").src,
                    book_name: el.querySelector("a")?.title,
                    publish: el.querySelector(".search_book_author a[name='P_cbs']")?.title,
                    author: el.querySelector(".search_book_author a[name='itemlist-author']")?.innerText,
                   pub_date: el.querySelector(".search_book_author>span:nth-child(2)")?.innerText.split("/")[1]
                })
            }
            let div = document.createElement("div")
            div.innerHTML = JSON.stringify(data)
            div.id="div"
            document.body.appendChild(div)
        },2000)
    }
    a()
    '''
    getVar = '''
        return document.querySelector("#div").innerHTML
    '''
    driver.execute_script(script)
    sleep(3)
    res = driver.execute_script(getVar)
    print(res)
    data = json.loads(res)

    # 检查文件是否存在，如果不存在则创建文件
    file_path = 'data.json'
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write('[]')

    # 读取已有的 JSON 数据
    with open(file_path, 'r') as file:
        existing_data = json.load(file)

    # 将解析后的 Python 对象追加到已有的 JSON 数据中
    existing_data.extend(data)

    # 将更新后的 JSON 数据写入文件
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)
# 关闭浏览器
# driver.quit()