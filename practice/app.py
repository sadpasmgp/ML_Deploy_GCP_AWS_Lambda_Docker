# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

''' http://localhost:5000/hello_world '''

from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_world')
def hello():
    return "Hello World"


''' http://127.0.0.1:5000/add?a=3&b=5 '''
@app.route('/add', methods=["GET"])
def add_GET():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a) + int(b))


'''
http://127.0.0.1:5000/add
{
"a" : 3,
"b" : 5
}
'''

@app.route('/add', methods=["POST"])
def add_POST():
    data = request.get_json()
    a = data['a']
    b = data['b']
    return str(int(a) + int(b))



#app.run()


''' If Run from command line remove below comment. '''

if __name__ == '__main__':
    app.run()
