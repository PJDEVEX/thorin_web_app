# Importing the Flask class
# render_template function from the Flask module
from flask import Flask, render_template
# Importing the JSON module
import json
# Importing the 'os' module for operating system
# related functionalities
import os


# instance of the Flask class
app = Flask(__name__)


#  route for the index page
@app.route("/")
def index():
    return render_template("index.html")


#  Route for the about page. Fetches company data from JSON
@app.route("/about")
def about():
    data = []
    # Opens company.json file in read mode and assigns to json_data variable
    with open("data/company.json", "r") as json_data:
        # Loads JSON data into the 'data' variable
        data = json.load(json_data)
    # Renders about page with data passed to company variable
    return render_template("about.html", page_title="About", company=data)


#  route for the contact page
@app.route("/contact")
def contact():
    # Renders "contact.html" template with "Contact" title.
    return render_template("contact.html", page_title="Contact Us")


#  route for the career page
@app.route("/careers")
def careers():
    # Renders "careers.html" template with "Careers" title.
    return render_template("careers.html", page_title="Careers")



# Check if the script is running as the main program
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),  # Set the host to listen on
        port=int(os.environ.get("PORT", "5000")),  # port to listen on
        debug=True)  # Enable debug mode (to be false when running the program)
