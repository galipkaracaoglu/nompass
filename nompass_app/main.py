from flask import Flask, request , render_template
from placeoperations import fetcher
app = Flask(__name__)

@app.route('/')
def mainWork():
    return render_template('mainpage.html')

@app.route("/addPlace",methods=["GET","POST"])
def addPlace():
    if request.method == "POST":
        return fetcher.extractPlace("İTÜ")
    return render_template('addplace.html')

#app.run(debug=True,port=5000,host='0.0.0.0')
