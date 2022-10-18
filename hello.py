# from flask import Flask
# app = Flask(__name__)
#
# if __name__ == "__main__":
#     app.run()
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()

    return wrapper_function()

@delay_decorator
def say_hello():
   print('King')
