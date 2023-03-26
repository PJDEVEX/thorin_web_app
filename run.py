# Importing the Flask class 
# render_template function from the Flask module
from flask import Flask, render_template

# Importing the 'os' module for operating system 
# related functionalities
import os


# instance of the Flask class
app = Flask(__name__)


#  route for the index page
@app.route("/")
def index():
    return render_template("index.html")


#  route for the about page
@app.route("/about")
def about():
    return render_template("about.html")


#  route for the contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")


#  route for the career page
@app.route("/careers")
def careers():
    return render_template("careers.html")



# Check if the script is running as the main program
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),  # Set the host to listen on
        port=int(os.environ.get("PORT", "5000")),  # port to listen on
        debug=True)  # Enable debug mode (to be false when running the program)