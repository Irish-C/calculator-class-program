# Define a class for Calculator
class Calculator:

    # This is a method for addition
    def add(self, num1, num2):
        return round(num1 + num2, 2)    # return value is round off to two decimals

    # This is a method for subtraction
    def subtract(self, num1, num2):
        return round(num1 - num2, 2)    # return value is round off to two decimals
    
    # This is a method for multiplication
    def multiply(self, num1, num2):
        return round(num1 * num2, 2)    # return value is round off to two decimals
    
    # This is a method for division
    def divide(self, num1, num2):
        if num2 ==0:                    # raise zero error value for num2
            raise ZeroDivisionError('\nCannot divide by zero!')
        else:
            return round(num1 / num2, 2)    # return value is round off to two decimals