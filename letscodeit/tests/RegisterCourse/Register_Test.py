from pages.Courses.Register_courses import RegisterCoursesPage
from pages.home.login_page import LoginClass
import pytest
import unittest
from Utilities.teststatus import TestStatus
import time




@pytest.mark.fixture("OnetimesetUp","setUp")
class RegisterCourse(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,OnetimesetUp):
        driver = self.driver
        self.lp = LoginClass(driver)
        self.Rc = RegisterCoursesPage(driver)
        self.ts = TestStatus(driver)
        self.lp.Login("test@email.com","abcabc")

    @pytest.mark.run(order=1)
    def test_invalidRegistration(self):
        time.sleep(3)
        self.Rc.enterCourse("JavaScript")
        time.sleep(5)
        self.Rc.selectCourseToEnroll("JavaScript for beginners")
        time.sleep(5)
        self.Rc.enrollCourse(num="12234",exp="1020",ccv="345")
        time.sleep(5)
        result1 = self.Rc.verifyError()
        # self.ts.markFinal("test_invalidRegistration ",result1," Invalid Registration")






