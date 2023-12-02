from flask import Flask

# ! CHANGE DATABASE NAME
DATABASE = 'users'

app = Flask(__name__)
app.secret_key = "shhhhhhhhhhhhhhh"