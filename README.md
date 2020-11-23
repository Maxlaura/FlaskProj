

## Overview

[Veterinary ABC](https://veterinary-app-demo.herokuapp.com/index) is a CMS (Content Management System) concept, t was created with the intention of helping veterinarians manage clients and appointments.

The vet, once into the platform, is able to easely manage customers and appointments on within the app.

The appointments and customers are displayed using tables, for easy CRUD operations (Create, Read, Update, Delete). 

------



## UX

### User

As a customer what i am able to do?

- Easy access to list of customers
- Insert a new customer to the existing customers base
- Being able to add a new appointment, choosing the correct date, and associate the appointment to a existing customer
- View the list of current added appointments

### Design

The project is very clean, user have the main and core functionality availlable on a responsive web application. The goal was to keep it as clean as possibile avoiding user on do mistakes using the app.

### Wireframes

The project wireframes was build using wireframe.cc. An online free tool for online wireframes.

#### Base 

[Here](https://wireframe.cc/va06Xu) is the base wireframe, used to describe and understand also the Base.html template using within the entire app. It mainly describes how the base structure is like.


#### New Customer
[Here](https://wireframe.cc/7KGzaw) is the customer insert page. This page describes all the input fields and their position. Some of those fields are also mandatory once inserting a new customer.

#### New Appointment
[Here](https://wireframe.cc/Qk0Qcv) is the appointment insert page. This page also is very simple and very clear, because this is the goal of the app, being clear and fast to the final user.

#### Lists
[Here](https://wireframe.cc/3W0Rar) Both customers and appointments lists are made simple, with the possibility to edit the current row or simply delete it within the list. For this page datatable was used display different column based on data that is displayed (appointments or customers). 


### Code structure

The project code structure is showed below. It tries to be as clean as possibile.

```bash
.
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       └── script.js
├── templates
│   ├── appointmentlist.html
│   ├── base.html
│   ├── customerlist.html
│   ├── index.html
│   ├── newupdateappointment.html
│   ├── newupdatecustomer.html
└── app.py

```

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

### Features to Implement

Would be cool to have those features:

- User statistics 
- Include social media like whatsapp or telegram for direct messages


---

## Technologies Used

The following list contains used technology for this project.

- Python 
- MongoDB
- Bootstrap
- Flask
- Bson
    - Used to handle MongoDB ObjectId
- pymongo
    - Used to handle connection and DB interactions
- flask_bootstrap
    - Used to setup flask for bootstrap


### Other Tools

- Wireframecc
    - Used to create web app wireframes
- mLab
    - Used to host the MongoDB instance


------

## Testing

This is the list of testing has done on the web application.

### W3C Validation
A W3C HTML validatio test has done on the website wich canbe cound [here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fveterinary-app-demo.herokuapp.com%2F) to check out if everything is correct and no errors appears.

### User testing
The list of tests that has been done:
- Test insert a new customer
    - Test insert a new customer with different data, also test the part of validation forms that application contains, see if all the errors appears accordly
- Test insert a new appointment
    - Check if all the fields are checked within validation, insert a new appointment picking a user from the existing list of customers
- Test the validation part on the interted data
- Test the edit customer
    - Check if all data is display correctly on the fields, update the existing customer with new data
- Test update appointment
    - Pick an existing appointment and check if the data is correctly display on fields, also edit some fields and update the appointment, check if data is correclty saved on the databse
- Delete a customer
    - Test if the customer is correctly deleted after interation with the delete button
- Delete an appointment
    - Test if the appointment is correctly deleted after interation with the delete button
- Test if the website is responsive, open it with the browser and using mobile devices, also try to resize the window to see if the menu handles accordly.



------



### Deployment

The project is hosted on Github and uses Heroku as main platform for deployment. In order to contibute to the repository you should have a Github Account. 

#### Prerequisites

In order to contribute to this repository you will need to have the following installed:

- Python 3.8.3 or higher
- Git version control
- Code editor, for this project Pycharm was used

#### Development

How to local deploy the project.

##### Requirements

After clonig the project to your local machine, you will need to install all the projects dependencies type `pip install -r requirements.txt`. If you add or update any new packages to the project use `pip freeze --local > requirements.txt ` to update the requirements.txt file with the new dependencies

##### Environment Variables

You will need to setup the following environment variables.

MONGO_URI : This is the URI to connect to the Mongo Database


##### Contribution

- If you want to make changes on this project is better to use a different branch
- Use `git checkout -b <brancname>` to create a new branch and edit the files
- If you are happy with the changes to use `git commit -m "my commit message"` to commit the changes.
- Use `git push `to push the changes to the repository
- If youd like to see those changes online, please do a pull request

##### Deployment

You can easely pull request on this project on master banch. If accepted all the edits that was made, will be deployed to Heroku. You can run your own heroku application by creating an account on the Heroku website and following the tutorial on how to deploy a Python project wich can be find here: https://devcenter.heroku.com/articles/getting-started-with-python 
For questions or errors, i suggest use StackOverflow
