from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from bson import ObjectId
from pymongo import MongoClient

app = Flask(__name__)
Bootstrap(app)

# MongoDb connecting
client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.veterinary  # used database
customers = db.Customer  # customers collection
appointments = db.Appointment  # appointment collection


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def gotoIndex():
    return render_template('index.html')

# Customer part

@app.route('/customerList')
def customerList():
    listOfCustomers = customers.find()
    return render_template('customerlist.html', customerList=listOfCustomers)


@app.route("/updateCustomer")
def updateCustomer():
    id = request.values.get("_id")
    if id:
        _customer = customers.find_one({"_id": ObjectId(id)})
        button_text = "Update"
        page_title = "Update current user " + _customer['name']
    else:
        _customer = {"_id": "", "name": "", "surname": "", "country": "", "city": "", "address": "", "phone": "",
                     "mail": ""}
        button_text = "Insert"
        page_title = "Insert new customer"

    return render_template('newupdatecustomer.html', customer=_customer,
                           pageTitle=page_title, action_button_text=button_text)


@app.route("/updateOrInsertUser", methods=['GET', 'POST'])
def actionUpdateUser():
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

    return customerList()


@app.route("/removeCustomer")
def removeCustomer():
    id = request.values.get("_id")
    customers.remove({"_id": ObjectId(id)})
    return customerList()

# Appointment part

@app.route('/appointmentsList')
def appointmentsList():
    listOfAppointments = appointments.find()
    return render_template('appointlist.html', appointmentList=listOfAppointments)

@app.route("/updateAppointment")
def updateAppointment():
    id = request.values.get("_id")
    if id:
        _appo = appointments.find_one({"_id": ObjectId(id)})
        button_text = "Update"
        page_title = "Updating current appointment: " + _appo['cause']
    else:
        _appo = {}
        button_text = "Insert"
        page_title = "Insert new appointment"

    _customers = customers.find()

    return render_template('newupdateappointment.html', appointment=_appo,
                           pageTitle=page_title, action_button_text=button_text, customers=_customers)

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

@app.route("/removeAppointment")
def removeAppointment():
    id = request.values.get("_id")
    appointments.remove({"_id": ObjectId(id)})
    return appointmentsList()

if __name__ == '__main__':
    app.run()
