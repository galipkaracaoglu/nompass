from flask import Flask
app = Flask(__name__)

@app.route('/')
def mainWork():
    return 'Merhaba'


app.run()
