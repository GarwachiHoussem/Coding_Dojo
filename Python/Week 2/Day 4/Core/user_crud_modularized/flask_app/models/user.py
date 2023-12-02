from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask import flash




class User:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name= data_dict['last_name']
        self.email= data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        

    @classmethod
    def create_User(cls, data_dict):
        query = """
                INSERT INTO Users (user_id,name,description,instructions,date,under_30)
                VALUES (%(user_id)s,%(name)s,%(description)s,%(instructions)s,%(date)s,%(under_30)s);
                """
        # result = connectToMySQL(DATABASE).query_db(query,data_dict)
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def update_User(cls, data_dict):
        query = """
                UPDATE Users 
                SET name = %(name)s, description = %(description)s,
                            instructions = %(instructions)s , date = %(date)s,
                            under_30 = %(under_30)s
                WHERE id = %(id)s   ;
                """
        # result = connectToMySQL(DATABASE).query_db(query,data_dict)
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_User_by_id(cls,data_dict):
        query = """
                    SELECT * FROM Users 
                    JOIN users ON Users.user_id = users.id 
                    WHERE Users.id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        User = cls(result[0])
        User.poster = result[0]['first_name']
        return User
    
    @classmethod
    def destroy(cls, data_dict):
        query = """
                DELETE FROM Users WHERE id = %(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_all_Users(cls):
        query = "SELECT * FROM Users JOIN users ON Users.user_id = users.id;"
        result = connectToMySQL(DATABASE).query_db(query)
        all_Users = []
        for row in result:
            User = cls(row)
            User.poster = row['first_name']
            all_Users.append(User)
        return all_Users
    

    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['name']) < 3:
            flash("name too short!","name")
            is_valid = False
        if len(data_dict['description']) < 3:
            flash("description too short!","description")
            is_valid = False
        if len(data_dict['instructions']) < 3:
            flash("instructions too short!","instructions")
            is_valid = False
        if len(data_dict['date']) < 1:
            flash("date required!","date")
            is_valid = False

        return is_valid