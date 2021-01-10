## Description

This repository contains some Flask examples for a CRUD app.

To run this sample code, run the command below:

```pipenv install flask flask-pymongo python-dotenv```

Run the environment by using:

```pipenv shell```

Next, create these files:

.flaskenv
.env

.flaskenv should contain the following:

FLASK_APP=app
FLASK_ENV=development

.env will contain the connection string for mongodb:

MONGO_URI='mongodb+srv://<username>:<password>@cluster0.daxh6.mongodb.net/<DB>?retryWrites=true&w=majority'

You should get the url from the mongo Atlas website.



