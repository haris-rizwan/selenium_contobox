from selenium import webdriver
from base.SeleniumDriver import SeleniumDriver
import Utilities.custom_logger as cl
import logging



class TestStatus(SeleniumDriver):


    log = cl.customLogger(logging.INFO)
    
    def __init__(self,driver):
     super(TestStatus, self).__init__(driver)
     self.resultlist = []

    def setResult(self,result,resultMessage):
        try:
            if result is not None:
            #we dont have to right if result is true
             if result:
                 self.resultlist.append("Pass")
                 self.log.info("Verification Successful" + resultMessage)
             else:
                 self.resultlist.append("Fail")
                 self.log.info("Verification Unsuccessful" + resultMessage)
                 self.screenShot(resultMessage)

            else:
                self.resultlist.append("Fail")
                self.log.error("Result has no value" + resultMessage)
                self.screenShot(resultMessage)

        except:
            self.resultlist.append("Fail")
            self.log.error("###### Exception occurred" + resultMessage)
            self.screenShot(resultMessage)

    def mark(self,result,resultMessage):
        # it will mark the result of all the verfication/assertion
# points in the code
       self.setResult(result,resultMessage)


    def markFinal(self,testName,result,resultMessage):

        self.setResult(result,resultMessage)


        if "Fail" in self.resultlist:
            self.log.error(testName + " Test Failed")
            self.resultlist.clear()
            assert True == False

        else:
            self.log.info(testName + " Test pass")
            self.resultlist.clear()
            assert True == True

