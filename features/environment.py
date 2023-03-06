from appium import webdriver

def before_scenario(context, scenario):
    if 'test' in scenario.tags:
        context.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                    "bundleId": "com.xxx.chandler.ios1",
                    "automationName": "XCUITest",
                    "platformVersion": "12.2",
                    "deviceName": "iPhone SE ",
                    "platformName": "iOS",
                    "udid": "c321b6ddb700d805590a9fff1d0ec572e8b2c5d0"
            }
        )