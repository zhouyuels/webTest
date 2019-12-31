#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :BasicPage.py
# @Time      :2019/12/3 17:13
# @Author    :ZhouYue
# @Description    :基础页面，父类。封装页面基础操作，所有页面均继承该页面

from selenium  import webdriver
from main.config.Browser import Browser
import time

class BasicPage():
    """
    基础页面，封装页面基础操作
    """

    FIND_ELEMENT_TIMEOUT_IN_SECONDS = 5
    FLASH_TIMES = 1
    STYLE = "background: red; border: 2px solid red;"

    def __init__(self):
        self.driver = Browser().driver

    def openUrl(self,url):
        """打开url地址"""
        self.driver.get(url)
        self.browserMax()

    def browserMax(self):
        """窗口最大化"""
        self.driver.maximize_window()

    def browserMin(self):
        """窗口最小化"""
        self.driver.minimize_window()

    def getUrl(self):
        """获取页面url"""
        return self.driver.current_url

    def refresh(self):
        """刷新页面"""
        self.driver.refresh()

    def forward(self):
        """页面前进"""
        self.driver.refresh()

    def back(self):
        """返回上一页"""
        self.driver.back()

    def close(self):
        """关闭浏览器"""
        self.driver.close()

    def quit(self):
        """关闭浏览器并退出驱动"""
        self.driver.quit()



    """----------------------------------------元素操作----------------------------------------------"""
    def executescript(self , js,*args):
        """执行一段Js"""
        # print('execute_script("%s",%s)'%(js,args))
        return  self.driver.execute_script(js,*args)

    def timeout(self , func,timeout_seconds,*args):
        """超时处理"""
        start_milli_time = int(time.time()*1000)
        sleep_milli_time = 100
        timeout = timeout_seconds*1000
        while int(time.time()*1000) - start_milli_time <= timeout:
            els_list = func(*args)
            time.sleep(float(sleep_milli_time/1000))
            if len(els_list) != 0:
                return els_list
        return  None

    def isElement(self, el):
        """判断是否为WebElement元素"""
        assert isinstance(el, webdriver.remote.webelement.WebElement) , ("el参数类型错误，不是WebElement元素：%s" % el)

    def findElementByJQuery(self , selector, timeout_seconds = FIND_ELEMENT_TIMEOUT_IN_SECONDS):
        """
        用JQuery查找元素,返回匹配的第一个元素

        :Args:
         - selector: 元素选择器
         - timeout: 超时时间，默认没有
        :return:
            匹配的第一个WebElement元素
        :Usage:
            findElementByJQuery('#id')
        """
        els_list = self.findElementsByJQuery(selector, timeout_seconds)
        return els_list[0] if els_list != None else None

    def findElementsByJQuery(self , selector, timeout_seconds):
        """
        用JQuery查找元素,返回元素列表

        :Args:
         - selector: 元素选择器
         - timeout: 超时时间，默认没有
        :return:
            匹配的WebElement元素列表
        :Usage:
            findElementsByJQuery('#id')
        """
        assert timeout_seconds >= 0 ,"超时时间必须大于等于0"
        JQuery = 'return $("%s")' % selector
        if timeout_seconds == 0:
            els_list = self.executescript(JQuery)
        else:
            els_list = self.timeout(self.findElementsByJQuery, timeout_seconds, selector, 0)
        return els_list

    def findElementByJs(self , selector ,timeout_seconds = FIND_ELEMENT_TIMEOUT_IN_SECONDS):
        """
        用Js查找元素,返回匹配的第一个元素

        :Args:
         - selector: 元素选择器
         - timeout: 超时时间，默认没有
        :return:
            匹配的第一个WebElement元素
        :Usage:
            findElementByJs('#id')
        """
        els_list = self.findElementsByJs(selector,timeout_seconds)
        return els_list[0] if els_list != None else None

    def findElementsByJs(self , selector,timeout_seconds):
        """
        用Js查找元素,返回元素列表

        :Args:
         - selector: 元素选择器
         - timeout: 超时时间，默认没有
        :return:
            匹配的WebElement元素列表
        :Usage:
            findElementsByJs('#id')
        """
        assert timeout_seconds >= 0, "超时时间必须大于等于0"
        Js = 'return document.querySelectorAll("%s");' % selector
        if timeout_seconds == 0:
            els_list = self.executescript(Js)
        else:
            els_list = self.timeout(self.findElementsByJs, timeout_seconds, selector, 0)
        return els_list

    def Location(self,arg):
        """
        获取元素坐标

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
        :Usage:
            location(el)，location('#id')
        """
        if isinstance(arg,str):
            return  self.findElementByJQuery(arg).location
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            return arg.location

    def Size(self,arg):
        """
        返回元素大小

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
        :Usage:
            size(el)，size('#id')
        """
        if isinstance(arg,str):
            return  self.findElementByJQuery(arg).size
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            return arg.size

    def isSelected(self,arg):
        """
        元素是否被选中

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
        :Usage:
            size(el)，size('#id')
        """
        if isinstance(arg,str):
            return  self.findElementByJQuery(arg).is_selected()
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            return arg.is_selected()

    def isDisplayed(self,arg):
        """
        元素是否显示

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
        :Usage:
            size(el)，size('#id')
        """
        if isinstance(arg,str):
            return  self.findElementByJQuery(arg).is_displayed()
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            return arg.is_displayed()

    def focus(self,el):
        """
        将元素设置为焦点

        :Args:
         - el: WebElement元素
        """
        self.isElement(el)
        try:
            self.executescript("arguments[0].focus();", el)
        except:
            print("元素置为焦点错误")

    def flash(self , el ):
        """
        将元素闪烁

        :Args:
         - el: WebElement元素
        """
        assert self.FLASH_TIMES > 0 ,"闪烁次数应大于0"
        self.isElement(el)
        attributeName = "style"
        oldStyle = self.getAttributeByJs(el,attributeName)
        for times in range(self.FLASH_TIMES):
            self.setAttributeByJs(el,attributeName,self.STYLE)
            if oldStyle == None or len(oldStyle) == 0:
                self.removeAttributeByJs(el, attributeName)
            else:
                self.setAttributeByJs(el,attributeName,oldStyle)

    def getAttribute(self, arg,attrName):
        """
        通过JQuery获取元素的属性值，第一个匹配的元素

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
         - attrName: 属性名称
        :return:
            元素属性值
        :Usage:
            getAttribute('#id','style')、getAttribute(el,'style')
        """
        if isinstance(arg,str):
            JQuery = 'return $("%s").attr("%s")' % (arg,attrName)
            attr = self.executescript(JQuery)
        if isinstance(arg, webdriver.remote.webelement.WebElement):
            attr = arg.get_attribute(attrName)
        return attr

    def getAttributeByJs(self, arg,attrName):
        """
        通过Js获取元素的属性值，第一个匹配的元素

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
         - attrName: 属性名称
        :return:
            元素属性值
        :Usage:
            getAttributeByJs(el,'style')、getAttributeByJs('#id','style')
        """
        if isinstance(arg,str):
            Js = 'return document.querySelectorAll("%s")[0].getAttribute("%s");' % (arg,attrName)
            attr = self.executescript(Js)
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            Js = "return arguments[0].getAttribute('%s');" % attrName
            attr = self.executescript(Js,arg)
        return attr

    def getTest(self,arg):
        """
        获取元素文本中

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
        :Usage:
            getTest(el)，getTest('#id')
        """
        if isinstance(arg,str):
            return  self.findElementByJQuery(arg).text
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            return arg.text

    def setAttribute(self,selector,attrName,attrValue):
        """
        通过JQuery设置元素的属性值，第一个匹配的元素

        :Args:
         - selector: 元素选择器
         - attrName: 属性名称
         - attrValue: 属性值
        :Usage:
            setAttribute('#id','style','abc')
        """
        JQuery = '$("%s").attr("%s","%s");' % (selector,attrName,attrValue)
        self.executescript(JQuery)

    def setAttributeByJs(self,arg,attrName,attrValue):
        """
        通过Js设置元素的属性值，第一个匹配的元素

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
         - attrName: 属性名称
         - attrValue: 属性值
        :Usage:
            setAttributeByJs(el,'style','abc')、setAttributeByJs("#id","style","abc")
        """
        if isinstance(arg,str):
            Js = 'document.setAttribute("%s","%s")[0].getAttribute("%s");' % (arg,attrName,attrValue)
            self.executescript(Js)
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            Js = 'arguments[0].setAttribute(arguments[1], arguments[2]);'
            self.executescript(Js,arg,attrName,attrValue)

    def removeAttribute(self,selector,attrName):
        """
        通过JQuery删除元素的属性，第一个匹配的元素

        :Args:
         - selector: 元素选择器
         - attrName: 属性名称
        :Usage:
            removeAttribute('#id','style')
        """
        JQuery = '$("%s").removeAttr("%s")' % (selector,attrName)
        self.executescript(JQuery)

    def removeAttributeByJs(self,el,attrName):
        """
        通过Js删除元素的属性，第一个匹配的元素

        :Args:
         - el: WebElement元素
         - attrName: 属性名称
        :Usage:
            removeAttributeByJs(el,'style')
        """
        self.isElement(el)
        Js = 'arguments[0].removeAttribute(arguments[1]);'
        self.executescript(Js,el,attrName)

    def click(self,arg):
        """
        点击元素

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
        :Usage:
            click(el)，click('#id')
        """
        if isinstance(arg,str):
            self.el_click(self.findElementByJQuery(arg))
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            self.el_click(arg)

    def el_click(self,el):
        """
        点击元素

        :Args:
         - el: WebElement元素
        :Usage:
            el_click(el)
        """
        self.isElement(el)
        self.focus(el)
        self.flash(el)
        el.click()

    def clickByJs(self,arg):
        """
        点击元素

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
        :Usage:
            clickByJs(el)，clickByJs('#id')
        """
        if isinstance(arg,str):
            el = self.findElementByJQuery(arg)
            print(el)
            Js = 'document.querySelectorAll("%s")[0].click();' % arg
            self.focus(el)
            self.flash(el)
            self.executescript(Js)
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            Js = 'arguments[0].click();'
            self.focus(arg)
            self.flash(arg)
            self.executescript(Js,arg)

    def doubleclick(self,arg):
        """
        双击元素

        :Args:
         - arg: 元素参数，可为Selector元素选择器，或WebElement元素
        :Usage:
            doubleclick(el)，doubleclick('#id')
        """
        if isinstance(arg,str):
            self.el_doubleclick(self.findElementByJQuery(arg))
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            self.el_doubleclick(arg)

    def el_doubleclick(self,el):
        """
        双击元素

        :Args:
         - el: WebElement元素
        :Usage:
            el_doubleclick(el)
        """
        self.isElement(el)
        self.focus(el)
        self.flash(el)
        webdriver.ActionChains(self.driver).double_click(el).perform()

    def doubleclickByJs(self,selector):
        """
        双击元素

        :Args:
         - selector: Selector元素选择器
        :Usage:
            doubleclickByJs('#id')
        """
        if isinstance(selector,str):
            JQuery = '$("%s").dblclick();' % selector
            el = self.findElementByJQuery(selector)
            self.focus(el)
            self.flash(el)
            self.executescript(JQuery)

    def assertTagName(self,message ,arg,TagNameList = []):
        """
        验证元素为期望的元素

        :Args:
         - message: 需要抛出异常的信息
         - arg: 需验证的元素，可为Selector元素选择器，或WebElement元素
         - TagName: 元素的tagName列表，验证元素是否为该类型
        :Usage:
            assertTagName(el,[input])，assertTagName('#id',[input])
        """
        if isinstance(arg,str):
            TagName = self.findElementByJQuery(arg).tag_name
            assert TagName in TagNameList , message
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            TagName =arg.tag_name
            assert TagName in TagNameList , message

    def type(self, arg, content):
        """
        在input,textarea中输入内容，清除后输入，仅支持input,textarea

        :Args:
         - arg: 输入框元素，可为Selector元素选择器，或WebElement元素
         - content: 输入的信息
        :Usage:
            input(el,"姓名")，input('#id',"姓名")
        """
        self.assertTagName("input方法仅对input,textarea元素生效",arg,["input","textarea"])
        if isinstance(arg,str):
            self.findElementByJQuery(arg).clear()
            self.type_sendkeys(self.findElementByJQuery(arg), content)
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            arg.clear()
            self.type_sendkeys(arg, content)

    def type_sendkeys(self, el, content):
        """
        在input,textarea中输入内容，不清除，追加输入，仅支持input,textarea

        :Args:
         - el: 输入框元素，WebElement元素
         - content: 输入的信息
        :Usage:
            input_sendkeys(el,"姓名")
        """
        self.assertTagName("input方法仅对input,textarea元素生效",el,["input","textarea"])
        if isinstance(el,webdriver.remote.webelement.WebElement):
            self.focus(el)
            self.flash(el)
            el.send_keys(content)

    def typeByJs(self, arg, content):
        """
        在input,textarea中输入内容，清除后输入，仅支持input,textarea

        :Args:
         - arg: 输入框元素，可为Selector元素选择器，或WebElement元素
         - content: 输入的信息
        :Usage:
            inputByJs(el,"姓名")，inputByJs('#id',"姓名")
        """
        self.assertTagName("input方法仅对input,textarea元素生效",arg,["input","textarea"])
        if isinstance(arg,str):
            Js = 'document.querySelectorAll("%s")[0].value="%s";' % (arg,content)
            el = self.findElementByJQuery(arg)
            self.focus(el)
            self.flash(el)
            self.executescript(Js)
        if isinstance(arg,webdriver.remote.webelement.WebElement):
            Js = 'arguments[0].value=arguments[1];'
            self.focus(arg)
            self.flash(arg)
            self.executescript(Js,arg,content)

    def moveSlider(self,Icon,LabelTip):
        """移动滑块

        :Args:
         - Icon: 滑块Selector元素选择器
         - LabelTip: 滑块路径按Selector元素选择器
        :Usage:
            moveSlider("#id",".id")
        """
        if self.getSliderVerifyCodeIcon(Icon) and self.getLabelTip(LabelTip):
            action = webdriver.ActionChains(self.driver)
            SliderVerifyCodeIcon = self.getSliderVerifyCodeIcon(Icon)
            action.drag_and_drop_by_offset(SliderVerifyCodeIcon ,self.Size(self.getLabelTip(LabelTip))["width"] ,0).perform()
            action.release().perform()
            action.move_to_element(SliderVerifyCodeIcon).release()

    def getLabelTip(self,selector):
        """获取滑动验证码文本元素

        :Args:
         - selector: 滑块Selector元素选择器
        :Usage:
            getLabelTip(arg)
        """
        return self.findElementByJQuery(selector)

    def getSliderVerifyCodeIcon(self,selector):
        """获取滑动验证码按钮

        :Args:
         - arg: 滑块路径Selector元素选择器
        :Usage:
            getSliderVerifyCodeIcon(selector)
        """
        return self.findElementByJQuery(selector)

    """----------------------------------------frame操作----------------------------------------------"""

    def switchMainFrame(self):
        """切换到最外层主页"""
        self.driver.switch_to.default_content()
        print("已切换到最外层frame/iframe")

    def switchToNextFrame(self,arg):
        """切换到下一层frame/iframe

        :Args:
         - arg: frame/iframe元素或定位，可为Selector元素选择器，或WebElement元素
        :Usage:
            switchToNextFrame(arg)
        """
        self.assertTagName("要切换frame只能是iframe和frame元素",arg,["iframe","frame"])
        try:
            if isinstance(arg,str):
                self.driver.switch_to.frame(self.findElementByJQuery(arg))
            if isinstance(arg, webdriver.remote.webelement.WebElement):
                self.driver.switch_to.frame(arg)
            print("已切换到frame:%s" % arg)
        except Exception as e:
            print("切换frame失败：%s" % e)

    def switchToParentFrame(self):
        """切换到上一层的frame"""
        self.driver.switch_to.parent_frame()

    def switchToFrame(self,frameList = None):
        """切换到指定的frame

        :Args:
         - frameList: frame/iframe列表，按层级关系从做往右，若为[]或None，则切换到主页面，可为Selector元素选择器，或WebElement元素
        :Usage:
            switchToFrame(["#frame1",".frame2",frame3]
        """
        assert isinstance(frameList,list) or frameList == None, "frameList必须为一个list或None"
        if frameList == None or frameList == []:
            self.switchMainFrame()
        else:
            for i in range(len(frameList)):
                try:
                    if isinstance(frameList[i], str):
                        self.driver.switch_to.frame(self.findElementByJQuery(frameList[i]))
                    if isinstance(frameList[i], webdriver.remote.webelement.WebElement):
                        self.driver.switch_to.frame(frameList[i])
                    print("已切换到frame:%s" % frameList[i])
                except Exception as e:
                    print("切换frame失败：%s" % e)

    """----------------------------------------窗口操作----------------------------------------------"""

    def getTitle(self):
        """获取窗口标题"""
        return self.driver.title

    def getHandle(self):
        """"获取到当前页面的句柄"""
        handle = self.driver.current_window_handle
        return handle

    def getHandles(self):
        """"获取到当前所有页面的句柄"""
        handles = self.driver.window_handles
        return handles

    def switchToWindowByHandle(self,handle):
        """根据句柄切换到窗口

        :Args:
         - handle: 要切换到的窗口句柄
        :Usage:
            switchToWindowByHandle(handle)
        """
        self.driver.switch_to.window(handle)
        print(f"已经切换到窗口：{self.getTitle()}")

    def switchToWindowByName(self,windowName):
        """根据窗口标题切换到窗口

        :Args:
         - windowName: 要切换到的窗口的标题文本或文本的一部分
        :Usage:
            switchToWindowByName(windowName)
        """
        handles = self.getHandles()
        for i in handles:
            self.switchToWindowByHandle(i)
            if windowName in self.getTitle():
                 break

    def switchToLastWindow(self):
        """切换到最新的窗口"""
        self.driver.switch_to.window(self.getHandles()[-1])
        print(f"已经切换到窗口：{self.getTitle()}")

    def switchToFirstWindow(self):
        """切换到第一个窗口"""
        self.driver.switch_to.window(self.getHandles()[0])
        print(f"已经切换到窗口：{self.getTitle()}")



if __name__ == "__main__":
    aa = 123