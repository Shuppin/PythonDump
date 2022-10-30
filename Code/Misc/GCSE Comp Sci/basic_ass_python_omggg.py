import random

class RuntimeError(Exception):
    def __init__(self, message="RuntimeError: An error has occured during runtime"):
        self.message = message
        super().__init__(self.message)

errors = [SyntaxError, ValueError, ArithmeticError, NotImplementedError, RuntimeError]
raise random.choice(errors)



