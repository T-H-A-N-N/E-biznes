import unittest
import requests

class TestKtorServer(unittest.TestCase):

    BASE_URL = "http://localhost:8080"

    def test_get_root(self):
        response = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, world!")

    def test_post_message_valid(self):
        message = "This is a test message."
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_empty(self):
        message = ""
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_long(self):
        message = "a" * 10000  # Long message
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_special_characters(self):
        message = "!@#$%^&*()_+-=<>?"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_numeric(self):
        message = "1234567890"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_json(self):
        message = '{"key": "value"}'
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_xml(self):
        message = "<note><body>Test</body></note>"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/xml'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_html(self):
        message = "<p>This is a test message.</p>"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'text/html'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_script_injection(self):
        message = "<script>alert('test');</script>"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_sql_injection(self):
        message = "' OR '1'='1"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_plain_text(self):
        message = "This is plain text."
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'text/plain'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_invalid_json(self):
        message = "{this is invalid json}"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_large_json(self):
        message = '{"key": "' + 'a' * 10000 + '"}'
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_with_spaces(self):
        message = "    This is a test message with spaces.    "
        response = requests.post(f"{self.BASE_URL}/message", data=message.strip(), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_unicode(self):
        message = "こんにちは世界"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_emojis(self):
        message = "Hello, world! 😊"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_very_short(self):
        message = "a"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_different_content_type(self):
        message = "Test message."
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'text/plain'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_large_number(self):
        message = "1234"
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

    def test_post_message_special_headers(self):
        message = "Special message"
        headers = {'Content-Type': 'application/json', 'X-Custom-Header': 'CustomValue'}
        response = requests.post(f"{self.BASE_URL}/message", data=message, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent to Discord")

if __name__ == "__main__":
    unittest.main()

