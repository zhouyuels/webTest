#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :LoginPage.py
# @Time      :2019/12/5 18:13
# @Author    :ZhouYue

from main.commom.base.BasicPage import BasicPage

class loginPage(BasicPage):
    """
    登录页面
    """

    URL = "https://pro.formtalk.net/login.do"

    VERIFY_CODE_ICON = "span.verifyCode-icon"
    """验证码按钮"""

    LABEL_TIP = "span.labelTip"
    """滑动轨迹"""

    MAIN_PAGE_KEYWORD = "云端应用自定义构建平台"
    """主页面名称"""

    name = "input[name=loginName]"
    """用户名"""

    pd = 'input[name=loginPassword]'
    """密码"""

    ok = 'input#doLogin'
    """登录按钮"""

    def loginUrl(self,url = URL):
        """

        打开登录页面
        :param url: 登录页面地址
        """
        self.openUrl(url)

    def login(self,user,pd):
        """

        登录
        :param user: 用户名
        :param pd: 密码
        """
        self.loginUrl()
        self.editLoginInfo(user,pd)
        self.click(self.ok)
        window = self.getTitle()
        if "云端应用自定义构建平台" in window:
            loginPage.logger.debug(f"登录成功 ")
        else:
            loginPage.logger.error(f"登录失败")

    def editLoginInfo(self,user,pd):
        """

        编辑登录信息
        :param user: 用户名
        :param pd: 密码
        """
        loginPage.logger.debug(f"使用用户：[{user}/{pd}]进行登录 ")
        self.type(self.name, user)
        self.type(self.pd, pd)
        self.moveSlider(self.VERIFY_CODE_ICON,self.LABEL_TIP)




if __name__ == "__main__":
    aa =123