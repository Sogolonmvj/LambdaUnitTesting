import json

from core.lambda_processor import Processor


def lambda_handler(event, context) -> json:
    first_number: int = event["first"]
    second_number: int = event["second"]
    operator: str = event["operator"]

    processor: json = Processor(first=first_number, second=second_number, operator=operator)
    return processor.calculate()


if __name__ == '__main__':
    print(lambda_handler(event={'first': 128, 'second': 512, 'operator': str('*')}, context=''))
