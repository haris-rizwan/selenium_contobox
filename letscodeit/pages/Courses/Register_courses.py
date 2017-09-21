from selenium.webdriver.common.by import By
import time
from base.SeleniumDriver import SeleniumDriver
import Utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

      ##########################
       #loctors for elements#####
      ##########################

    _search_Box = "search-courses"  # id
    _all_courses = "course-listing-title" # class
    _course = ".//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _enroll_button = "enroll-button-top"  # id
    _cc_num = "cc_field"  # id
    _cc_exp = "cc-exp"  # id
    _cc_ccv = "cc_cvc"
    _country_select = "country-select-inside"  # id
    _pay_now_button = "verify_cc_btn"
    _enroll_error_message = ".//div[@id='checkout_form_errors']//div[contains(text(),'The card number is invalid.')]"


        #########################################
        # actions to be performed on the elements
        #########################################


    def enterCourse(self,course):
        self.sendKeys(course,locator=self._search_Box,locatorType="id")

    def selectCourseToEnroll(self,fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName),locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button,locatorType="id")

    def enterCardnum(self,num):
        self.sendKeys(num,locator=self._cc_num,locatorType="id")

    def enterCardExp(self,exp):
        self.sendKeys(exp,locator=self._cc_exp,locatorType="id")

    def enterCardCcv(self,ccv):
        self.sendKeys(ccv,locator=self._cc_ccv,locatorType="id")

    def selectCountry(self):
        Select(self.getElement(self._country_select,locatorType="id")).select_by_index(3)



    def clickPaynow(self):
        self.elementClick(locator=self._pay_now_button,locatorType="id")

    def enterCcInformation(self,num,exp,ccv):
        self.enterCardnum(num)
        self.enterCardExp(exp)
        self.enterCardCcv(ccv)


    def enrollCourse(self,num="",exp="",ccv="",):
        self.clickOnEnrollButton()
        time.sleep(3)
        self.webScroll(direction="down")
        time.sleep(3)
        self.enterCcInformation(num,exp,ccv)
        time.sleep(3)
        self.selectCountry()
        time.sleep(2)
        self.clickPaynow()

    # def errorMessage(self):
    #     messageElement = self.waitForElement(self._enroll_error_message,locatorType="xpath")
    #     result = self.isElementDisplayed(element=messageElement)
    #     print(result)
    #     return result


    # def errorMessagePresent(self):
    #     error = self.elementPresenceCheck(self._enroll_error_message,"xpath")
    #     if error == True:
    #         print("element present")
    #
    #     else:
    #         print("not present")


    def verifyError(self):
         creditField = self.isElementDisplayed(self._cc_num,locatorType="id")
         print("%%%%%%%%%%%%%%%%%")
         print(creditField)
         print("%%%%%%%%%%%%%%%%%")
         message =self.getElement(self._enroll_error_message,locatorType="xpath")
         check = message.is_displayed()
         print("###############")
         print(check)
         print("###############")
         view = self.isElementDisplayed(self._enroll_error_message,locatorType="xpath")
         print("*****************")
         print(view)
         print("*****************")
