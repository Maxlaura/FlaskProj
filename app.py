import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from bson import ObjectId
from pymongo import MongoClient


app = Flask(__name__)
Bootstrap(app)

# MongoDb connecting
#client = MongoClient("mongodb://127.0.0.1:27017")  # local host uri
client = MongoClient(os.environ.get('MONGO_URI'))

db = client.test  # used database
customers = db.Customer  # customers collection
appointments = db.Appointment  # appointment collection


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def gotoIndex():
    return render_template('index.html')

# Customer part
#Asking for the customer list, redirect the user to correct page passing to the page the list of customers
@app.route('/customerList')
def customerList():
    _customers = customers.find()
    return render_template('customerlist.html', customerList=_customers)

#Using this route to update an existing user
@app.route("/updateCustomer")
def updateCustomer():
    id = request.values.get("_id")
    if id:
        _customer = customers.find_one({"_id": ObjectId(id)})
        _buttonText = "Update"
        _pageTitle = "Update current user " + _customer['name']
    else:
        _customer = {"_id": "", "name": "", "surname": "", "country": "", "city": "", "address": "", "phone": "",
                     "mail": ""}
        _buttonText = "Insert"
        _pageTitle = "Insert new customer"

    return render_template('newupdatecustomer.html', customer=_customer,
                           pageTitle=_pageTitle, actionButtonText=_buttonText)


#Using this route for both update and insert a new user
#Added form validity check
@app.route("/updateOrInsertUser", methods=['GET', 'POST'])
def actionUpdateUser():
    if request.method == 'POST':
        id = request.values.get("_id")
        name = request.values.get("name")
        surname = request.values.get("surname")
        country = request.values.get("country")
        city = request.values.get("city")
        address = request.values.get("address")
        phone = request.values.get("phone")
        mail = request.values.get("email")

        obj = {"name": name, "surname": surname, "country": country, "city": city, "address": address, "phone": phone,
           "email": mail}

        if id:
            customers.update({"_id": ObjectId(id)}, {'$set': obj})
        else:
            customers.insert_one(obj)

        return customerList() # after inserting the current user, returning the customer list


#using this roufe for removing an existing customer
@app.route("/removeCustomer")
def removeCustomer():
    _id = request.values.get("_id")
    customers.remove({"_id": ObjectId(_id)})
    return customerList()

# Appointment part

@app.route('/appointmentsList')
def appointmentsList():
    listOfAppointments = appointments.find()
    return render_template('appointlist.html', appointmentList=listOfAppointments)

#updating an appointment
@app.route("/updateAppointment")
def updateAppointment():
    #changing button title according to the _id, if the id exists its an update, insert otherwise
    id = request.values.get("_id")
    if id:
        _appo = appointments.find_one({"_id": ObjectId(id)})
        _buttonText = "Update"
        _pageTitle = "Updating current appointment: " + _appo['cause']
    else:
        _appo = {}
        _buttonText = "Insert"
        _pageTitle = "Insert new appointment"

    _customers = customers.find()

    return render_template('newupdateappointment.html', appointment=_appo,
                           pageTitle=_pageTitle, action_button_text=_buttonText, customers=_customers)

#updating or inserting a new appointment
@app.route("/updateOrInsertAppointment", methods=['GET', 'POST'])
def actionUpdateOrInsertAppointment():
    id = request.values.get("_id")
    date = request.values.get("date")
    hour = request.values.get("hour")
    cause = request.values.get("cause")
    description = request.values.get("description")

    customer = request.form.get('customer')

    obj = {"date": date, "hour": hour, "cause": cause, "description": description, "customer" : customer}

    if id:
        appointments.update({"_id": ObjectId(id)}, {'$set': obj})
    else:
        appointments.insert_one(obj)

    return appointmentsList()

# removing an existing appointment
@app.route("/removeAppointment")
def removeAppointment():
    id = request.values.get("_id")
    appointments.remove({"_id": ObjectId(id)})
    return appointmentsList()

if __name__ == '__main__':
    app.run()
