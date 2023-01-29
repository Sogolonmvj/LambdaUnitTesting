import json

from exception.invalid_operator_exception import InvalidOperatorException

class Processor:
    def __init__(self, first: int, second: int, operator: str) -> None:
        self.first = first
        self.second = second
        self.operator = operator

    def calculate(self) -> json:
        return {
            'statusCode': 200,
            'body': json.dumps(self.verify_operator())
        }

    def verify_operator(self) -> json:
        match self.operator:
            case "+":
                return {'result': self.first + self.second}
            case "-":
                return {'result': self.first - self.second}
            case "*":
                return {'result': self.first * self.second}
            case "/":
                return {'result': self.first / self.second}
            case default:
                raise InvalidOperatorException("Invalid operator!")
