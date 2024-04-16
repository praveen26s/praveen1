from flask import flask, render_template, request,redirect, url_for
from pymongo import mongoclient
from dotenv import load_dotenv
import os
# pip install python-dotenv
load_dotenv()

app = flask(__name__)

mongo_uri = os.environ.get('MONGO_URI')
client = mongoclient(mongo_url)

db_name = "user_details"
database = client[db_name]
collection_name = 'users'
new_collection = database[collection_name]
@app.route("/form/submit", methods=["POST"])
def form_submit():
    firstname = request.form.get("fname")
    lastname = request.form.get("lname")

    data = {
        "fname" : firstname,
        "lname" : lastname
    }

    new_collection.insert_one(data)
    return redirect(url_for("success", fname = firstname, lname = lastname))
    @app.route("/find/details",methods=["GET"])
    def find_details():

        details = new_collection.find()
        print(details)
        details_list = []
        for detail in details:
            data = {
                "fname" : detail["fname"],
                "lname" : detail["lname"]
            }
            details_list.append(data)

            return render_template('display.html', userdetails = details_list)

        @app.route("/success/<fname>/<lname>",methods=["GET"])
        def success(fname,lname):
            return "fname= " + fname + ""

