from flask import Flask

# ! CHANGE DATABASE NAME
DATABASE = 'login_registration_schema'

app = Flask(__name__)
app.secret_key = "shhhhhhhhhhhhhhh"