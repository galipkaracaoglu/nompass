from flask import Flask
app = Flask(__name__)

@app.route('/')
def mainWork():
    return 'Merhaba'


#app.run(debug=True,port=5000,host='0.0.0.0')
