import pytest
from page_objects.login_page import LoginPage

# 用一个网上找的公共测试网站来测试：https://www.saucedemo.com/
BASE_URL = "https://www.saucedemo.com/"

class TestLogin:
    """测试登录功能的各个场景"""

    def test_successful_login(self, browser):
        """测试1: 用正确的用户名密码登录，应该成功"""
        # 步骤1: 打开网站
        browser.get(BASE_URL)
        login_page = LoginPage(browser)

        # 步骤2: 输入正确的用户名和密码 (这是该网站提供的演示账号)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # 步骤3: 验证是否登录成功
        assert "/inventory.html" in browser.current_url
        print("测试通过：正确用户登录成功")

    def test_failed_login_with_wrong_password(self, browser):
        """测试2: 用错误的密码登录，应该看到错误提示"""
        browser.get(BASE_URL)
        login_page = LoginPage(browser)

        login_page.enter_username("standard_user")
        login_page.enter_password("wrong_password")  # 故意输错
        login_page.click_login()

        # 验证页面上出现了预期的错误信息
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text
        print(f"测试通过：错误密码登录被拦截，提示信息为: {error_text}")