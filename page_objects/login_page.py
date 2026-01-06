from selenium.webdriver.common.by import By

class LoginPage:
    """登录页面"""
    # 1. 定义这个页面上所有的元素
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'user-name')       # 用户名输入框
        self.password_input = (By.ID, 'password')        # 密码输入框
        self.login_button = (By.ID, 'login-button')      # 登录按钮
        self.error_message = (By.CLASS_NAME, 'error-message-container') # 错误提示

    # 2. 定义在这个页面上能做的操作
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        # 获取错误提示文本，如果没有找到元素就返回空字符串
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return ""