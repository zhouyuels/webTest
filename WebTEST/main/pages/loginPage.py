#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :LoginPage.py
# @Time      :2019/12/5 18:13
# @Author    :ZhouYue

from main.pages.BasicPage import BasicPage

class loginPage(BasicPage):
    """
    登录页面
    """

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

    def loginUrl(self,url):
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
        self.editLoginInfo(user,pd)
        self.click(self.ok)
        self.logger.debug(f"登录完成")

    def editLoginInfo(self,user,pd):
        """

        编辑登录信息
        :param user: 用户名
        :param pd: 密码
        """
        self.logger.debug(f"使用用户：[{user}]进行登录")
        self.type(self.name, user)
        self.type(self.pd, pd)
        self.moveSlider(self.VERIFY_CODE_ICON,self.LABEL_TIP)




if __name__ == "__main__":
    aa =123