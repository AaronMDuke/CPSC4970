import unittest
from unittest.mock import patch, MagicMock

from module5.emailer import Emailer


class EmailerTest(unittest.TestCase):
    def setUp(self):
        Emailer._sole_instance = None
        Emailer.sender_address = None

    def test_singleton_instance(self):
        self.assertIs(Emailer.instance(), Emailer.instance())

    def test_configure_sender_address(self):
        Emailer.configure("aaron.m.duke85@gmail.com")
        self.assertEqual(Emailer.sender_address, "aaron.m.duke85@gmail.com")

    @patch("module5.emailer.yagmail.SMTP")
    def test_send_plain_email_calls_yagmail_send(self, mock_smtp):
        mock_connection = MagicMock()
        mock_smtp.return_value = mock_connection

        Emailer.configure("aaron.m.duke85@gmail.com")
        Emailer.instance().send_plain_email(
            ["aaron.m.duke85@gmail.com"], "hello", "body text"
        )

        mock_smtp.assert_called_once_with("aaron.m.duke85@gmail.com")
        mock_connection.send.assert_called_once_with(
            to="aaron.m.duke85@gmail.com", subject="hello", contents="body text"
        )



if __name__ == "__main__":
    unittest.main()