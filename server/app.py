#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:integer>')
def count(integer):
    number = range(1,101)
    if number:
    # if integer > 10 or integer < 1:
        # return "Integer must be between 1-10",400
        return "\n".join(map(str,range(integer))) + "\n"
        
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
       result = num1 + num2
    elif operation == "-":
       result = num1 - num2
    elif operation == "*":
       result = num1 * num2
    elif operation == "div":
       if num2 == 0:
           return "Cannot divide by zero."
       result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "put correct operation."
    return str(result)
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)


my_list = [1, 2, 3]
print(str(my_list))  # Output: "[1, 2, 3]"