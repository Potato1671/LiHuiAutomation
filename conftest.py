import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # 1. 启动浏览器
    print("【启动浏览器】")
    driver = webdriver.Chrome()  # 这会自动打开一个Chrome窗口
    driver.maximize_window()     # 最大化窗口
    driver.implicitly_wait(10)   # 设置隐式等待，让脚本更稳定

    # 2. 将浏览器实例“传递”给测试用例
    yield driver

    # 3. 关闭浏览器
    print("【关闭浏览器】")
    driver.quit()