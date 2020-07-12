from appium import webdriver
from time import sleep

desired_caps = {
    "platformName":"Android",   #使用操作系统
    "deviceName":"emulator-5554",   #设备名称
    "platformVersion":"5.1.1",    #系统版本
    "appPackage":"com.taobao.taobao",   #apk包名
    "appActivity":"com.taobao.tao.welcome.Welcome",   #apk的launchable-activity
    "noReset":True,   #不清除缓存
    "unicodeKeyboard":True,   #使用unicode编码发送字符串
    "resetKeyboard":True   #隐藏键盘
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
sleep(5)

#text定位(text属性)
driver.find_element_by_android_uiautomator('text("注册/登录")').click()
sleep(3)

#textContains模糊匹配定位，text比较长时适用该方法（text属性）
# driver.find_element_by_android_uiautomator('textContains("注册")').click()
# sleep(3)

#通过resourceId定位（reource_id属性）
# id = 'resourceId("com.taobao.taobao:id/aliuser_recommend_login_account_et")'
# driver.find_element_by_android_uiautomator(id).send_keys("嘿菇凉")
# sleep(3)

#通过className定位（class属性）
# driver.find_element_by_android_uiautomator('className("android.widget.Button")').click()
# sleep(3)

#通过description定位（content_desc属性）
# driver.find_element_by_android_uiautomator('description("扫一扫")').click()
# sleep(3)

#------------------uiautomator组合定位----------------------
#id和text组合定位
# id_text = 'resourceId("com.taobao.taobao:id/aliuser_recommend_login_account_et").text("请输入手机号码/会员名/邮箱")'
# driver.find_element_by_android_uiautomator(id_text).send_keys("嘿菇凉")
# sleep(3)

#class和text组合定位
# class_text = 'className("android.widget.EditText").text("请输入手机号码/会员名/邮箱")'
# driver.find_element_by_android_uiautomator(class_text).send_keys("嗨菇凉")
# sleep(3)

#层级定位childSelector(通过父级元素定位子级元素）
# son = 'description("我的淘宝").childSelector(className("android.widget.ImageView"))'
# driver.find_element_by_android_uiautomator(son).click()
# sleep(3)

#同级定位fromParent(一个元素的多个属性）
# brother = 'text("注册/登录").fromParent(className("android.widget.Button")'
# driver.find_element_by_android_uiautomator(brother).click()
# sleep(3)

#退出释放资源
driver.quit()