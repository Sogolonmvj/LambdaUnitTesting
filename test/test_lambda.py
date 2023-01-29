import json
import unittest
from main import lambda_handler


class TestLambda(unittest.TestCase):
    def test_result_status_code(self):
        event = {'first': 236, 'second': 1024, 'operator': str('+')}
        result = lambda_handler(event=event, context='')
        self.assertEqual(first=result['statusCode'], second=200)

    def test_result_body(self):
        event = {'first': 236, 'second': 1024, 'operator': str('+')}
        result = lambda_handler(event=event, context='')
        operation_result = 236 + 1024
        self.assertEqual(first=json.loads(result['body'])['result'], second=operation_result)
