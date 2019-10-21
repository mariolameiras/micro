from flask import Flask, escape, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return todo
    #return f'Hello, {escape(name)}!'

if __name__ == '__main__':
    app.run()


@staticmethod
def todo():
    resp = requests.get('https://todolist.example.com/tasks/')
    for todo_item in resp.json():
        print('{} {}'.format(todo_item['id'], todo_item['summary']))