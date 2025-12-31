# 自动化测试示例项目
这是为面试官Code Challenge准备的示例项目，展示了对Web登录功能的自动化测试思路与实现。

## 项目概述
- 测试目标：`https://www.saucedemo.com/` 公共测试网站的登录功能。
- 测试场景：1. 成功登录；2. 密码错误登录失败。
- 设计思路：将页面元素定位与测试逻辑分离，提高代码的可读性和可维护性。 技术栈：Python, pytest, Selenium, Page Object Model, 数据驱动等

## 如何运行本项目
1.  环境准备：已安装Python ，并将ChromeDriver路径加入系统环境变量。
2.  安装依赖：在项目根目录下运行：
bash
pip install -r requirements.txt 

3.  执行测试：运行以下命令执行测试并生成HTML报告：
bash
pytest test_cases/ -v --html=report.html --self-contained-html

4.  查看报告：运行完成后，打开生成的 `report.html` 文件查看测试结果
