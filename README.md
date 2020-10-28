# Veterinary project


Veterinary project is a simple Flask project that simulates a Content Management System where user is able to handle customers and appointments.

APP URL: https://veterinary-app-demo.herokuapp.com/
### Users

In this section user is able to:
  - Create a new user
  - Remove existing users
  - View list of current users
  - Update user data

For this purpose "admin" is able to insert a user wich is created by: name, surname, country, city, address, email and phone number.

### Appointments

In this section user is able to:
  - Create a new appointment
  - Remove existing appointment
  - View list of existing appointments
  - Update an appointment
 
For this section, "admin" is able to create a new appointment choosing: data, hour, cause of the appointment, description and select an existing user from the given options.

### Database structure
Everything is based on MongoDB, the main db is hosted on free tire using mLab.
There are 2 main collections: "Customer" and "Appointment"

Customers:
```json
{
    "city" : "",
    "surname" : "",
    "name" : "",
    "country" : "",
    "phone" : "",
    "address" : "",
    "email" : ""
}
```
Appointments:
```json
{
    "_id" : "",
    "customer" : "",
    "description" : "",
    "hour" : "",
    "date" : "",
    "cause" : ""
}
```

### Tech

Used Heroku CLI for heroku deployment

This project uses:
- Python
- MongoDB
- Bootstrap
- Flask
- bson (handling mongo ObjectId)
- pymongo (handling connections and DB interactions)
- flask_bootstrap (setting up Flask for Bootstrap)

Also used:
https://github.com/StartBootstrap/startbootstrap-sb-admin as base template
fontawesome for icons