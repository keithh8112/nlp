from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)

@app.route('/index', methods=['GET'])
@app.route('/', methods =['GET'])
def index():
	#bind the index page to the database
	#userinputs = [x for x in handle.mycollection.find()]
	return render_template('index.html', name= "Ryan")

@app.route('/write', methods=['POST'])
def write():
	userinput= request.form.get("userinput")
	#oid = handle.mycollection.insert({"message": userinput})
	return redirect ("/")
# host="10.2.20.39", port=port, 
if __name__ == '__main__':
    # port = int(os.environ.get('PORT, 5000'))
    app.run(debug = True)