import json


class Calculator:
    def add(self, operands):
        return operands[0] + operands[1]
    def subtract(self, operands):
        return operands[0] - operands[1]
    def divide(self, operands):
        return operands[0] / operands[1]
    def multiply(self, operands):
        return operands[0] * operands[1]
    
    def parse(self, cmd):
        # TODO: implement this function to parse json string into syntax tree
        data = json.loads(cmd) # decode json to object
        return data

    def eval(self, expr):
        # TODO: implement this function to evaluate an expression
        pairs = expr.items()
        operator = ''
        result = 0;
        for key, value in pairs:
            operator = key 
            operands = value 
            for index, item in enumerate(operands):
                if isinstance(item,dict):
                    operands[index] = self.eval(item)           
            if operator == '*':
                result = self.multiply(operands)
            elif operator == '/':
                result = self.divide(operands)
            elif operator == '+':
                result = self.add(operands)
            elif operator == '-':
                result = self.subtract(operands)
        return result
        
    def exec(self, cmd):
        expr = self.parse(cmd)
        return self.eval(expr)