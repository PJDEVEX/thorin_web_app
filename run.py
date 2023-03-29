# Importing the Flask class
# render_template, request, and flash function from the Flask module
from flask import Flask, render_template, request, flash
# Importing the JSON module
import json
# Importing the 'os' module for operating system
# related functionalities
import os
# Imports environment variables from "env.py" if it exists
if os.path.exists("env.py"):
    import env

# Creates a new Flask application instance named app
app = Flask(__name__)
# Sets Flask app's secret key value of "SECRET_KEY" environment variable
app.secret_key = os.environ.get("SECRET_KEY")


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


# Returns the name of a member from JSON data based on URL
@app.route("/about/<member_name>")
def about_member(member_name):
    # Create an empty dictionary to store member's details
    member = {}
    # Open the company's JSON file and load the data
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # Iterate over each object in the JSON data and 
        # match the URL to get member's details
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # return "<h1>" + member["name"] + "</h1>"
    # Render the member.html template with the member's details
    return render_template("member.html", member=member)


# Defines a Flask route for the /contact URL path. 
# If the request method is POST, 
# it prints the values of the "name" and "email" fields. 
# Finally, it renders a "contact.html" template 
# with the page title "Contact Us".
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
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
