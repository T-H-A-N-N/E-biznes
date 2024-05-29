import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class TestKtorServerOnBrowserStack(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os': 'Windows',
            'os_version': '10',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'name': 'Ktor Server Tests',
            'build': 'Ktor Server Build 1'
        }
        self.driver = webdriver.Remote(
            command_executor='https://YOUR_USERNAME:YOUR_ACCESS_KEY@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap)
        
    def test_get_root(self):
        self.driver.get("http://localhost:8080/")
        time.sleep(3)  # Wait for the page to load
        self.assertIn("Hello, world!", self.driver.page_source)

    def test_post_message_valid(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("This is a test message.")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_empty(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_long(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("a" * 10000)
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_special_characters(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("!@#$%^&*()_+-=<>?")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_numeric(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("1234567890")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_json(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys('{"key": "value"}')
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_xml(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("<note><body>Test</body></note>")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_html(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("<p>This is a test message.</p>")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_script_injection(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("<script>alert('test');</script>")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_sql_injection(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("' OR '1'='1")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_plain_text(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("This is plain text.")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_invalid_json(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("{this is invalid json}")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_large_json(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys('{"key": "' + 'a' * 10000 + '"}')
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_with_spaces(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("    This is a test message with spaces.    ")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_unicode(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("Hi")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_emojis(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("Hello, world! 😊")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_very_short(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("a")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_different_content_type(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("This is a test message.")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_large_number(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name("textarea")
        textarea.send_keys("1")
        button = self.driver.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(3)  ;
        self.assertIn("Message sent to Discord", self.driver.page_source)

    def test_post_message_special_headers(self):
        self.driver.get("http://localhost:8080/")
        textarea = self.driver.find_element_by_tag_name
