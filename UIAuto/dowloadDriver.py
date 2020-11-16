#-*- coding:utf-8 -*-
'''
chromedriver:http://npm.taobao.org/mirrors/chromedriver/
firxfoxdriver:https://github.com/mozilla/geckodriver/releases/
IE :https://www.nuget.org/packages/Selenium.WebDriver.IEDriver/
'''
chromedriver_url = "http://npm.taobao.org/mirrors/chromedriver/"
firxfoxdriver_url = "https://github.com/mozilla/geckodriver/releases/"
iedriver_url = "https://www.nuget.org/packages/Selenium.WebDriver.IEDriver/"

#appium
'''
npm install appium
npm install appium-doctor

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install node
npm install -g  appium
npm install -g  appium-doctor
brew install libimobiledevice --HEAD
brew install carthage
npm install -g ios-deploy
gem install xcpretty
'''
'''
vim ~/.bash_profile
JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home
CLASSPAHT=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ANDROID_HOME=/Users/zhenghong/Library/Android/sdk
export PATH=${PATH}:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/build-tools/29.0.3
PATH=${JAVA_HOME}/bin:$PATH:
export JAVA_HOME
export CLASSPATH
export PATH
source ~/.bash_profile
'''