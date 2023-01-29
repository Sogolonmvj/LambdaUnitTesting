from core.lambda_processor import Processor


def lambda_handler(event, context):
    first_number = event["first"]
    second_number = event["second"]
    operator = event["operator"]

    processor = Processor(first=first_number, second=second_number, operator=operator)
    return processor.calculate()


if __name__ == '__main__':
    print(lambda_handler(event={'first': 128, 'second': 512, 'operator': str('*')}, context=''))
