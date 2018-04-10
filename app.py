import requests
from  flask import Flask, render_template, request
#import follower_info_twitter

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")
#def hello_someone(name):
         return render_template("hello.html", name=name.title())
#@app.route("/signup", methods=["POST"])
#def sign_up():
	form_data = request.form
	print (form_data["email"])
	return "All OK"

#if __name__ == "__main__":
    app.run()
