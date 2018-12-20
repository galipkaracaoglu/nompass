from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def mainWork():
    return render_template('mainpage.html')


#app.run(debug=True,port=5000,host='0.0.0.0')
