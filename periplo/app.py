from flask import Flask, escape, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)

def todo():
    resp = requests.get('https://todolist.example.com/tasks/')


#Stormglass
#API KEY 846e41d6-d412-11e9-a64e-0242ac130004-846e42ee-d412-11e9-a64e-0242ac130004
#https://dashboard.stormglass.io/
# https://docs.stormglass.io/#

#MSW
#https://pt.magicseaweed.com/developer/sign-up
#https://pt.magicseaweed.com/docs/developers/59/querying-the-api/9909/
#https://magicseaweed.com/docs/developers/59/api-response-reference/9919/


#Windy
#https://github.com/windycom/API

#IPMA API
# https://api.ipma.pt/#
# https://www.ipma.pt/pt/maritima/costeira/index.jsp?selLocal=27&idLocal=27 Scrape...

#Flask tutorial
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

#Beautiful soup
# https://www.codementor.io/python/tutorial/python-web-scraping-beautiful-soup