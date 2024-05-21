from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
import re	

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.role = data_dict['role']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']


    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users (first_name, last_name, email,password , role) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(role)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    

    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM users WHERE id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data_dict):
        query = """SELECT * FROM users WHERE email=%(email)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        if result :
            return cls(result[0])
        return False
    
    @classmethod
    def get_by_role(cls, data_dict):
        query = """SELECT * FROM users WHERE role=%(role)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        users = []
        if result:
            for row in result:
                users.append(cls(row))
            return users
        return []
    
    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['first_name']) < 3:
            is_valid = False
            flash("First Name must be at least 3 characters", "first_name")

        if len(data_dict['last_name']) < 5:
            is_valid = False
            flash("Last Name must be at least 5 characters", "last_name")

        if not EMAIL_REGEX.match(data_dict['email']):
            is_valid = False
            flash("Invalid Email format", "email")
        elif User.get_by_email({'email': data_dict['email']}):
            is_valid = False
            flash("Email is already taken", "email")

        if len(data_dict["password"]) < 8:
            is_valid = False
            flash("Password must be at least 8 characters", "password")
        elif data_dict["password"] != data_dict["confirm_password"]:
            is_valid = False
            flash("Password and Confirm Password must match", "confirm_password")

        if data_dict["role"] not in ["client", "agency"]:
            is_valid = False
            flash("Please select a valid role", "role")

        return is_valid