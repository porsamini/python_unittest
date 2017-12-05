import unittest
from unittest.mock import Mock, patch
import sys
sys.modules['name'] = Mock()
from lib import hello

class TestHello(unittest.TestCase):
    @patch('name.getName')
    def test_hello(self, mockName):
        mockName.return_value = 'Vineeth'
        print(hello.say_hello())
        self.assertEqual(hello.say_hello(), "Hello Vineeth")
