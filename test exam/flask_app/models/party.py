from flask import flash
from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL

class Party:
    def __init__(self,data_dict):
        self.id=data_dict["id"]
        self.user_id=data_dict["user_id"]
        self.title= data_dict["title"]
        self.location= data_dict["location"]
        self.date=data_dict["date"]
        self.all_ages=data_dict["all_ages"]
        self.description= data_dict["description"]
        
# CRUd QUERIES = CLASS-METHODS
# 1- CREATE 
classmethod
def create(cls,data):
    query ="""INSERT INTO parties (user_id, title ,location, date, all_ages, description)
    VALUES (%(user_id)s, %(title)s ,%(location)s, %(date)s, %(all_ages)s, %(description)s);"""
    return connectToMySQL(DATABASE).query_db(query.data)

#2- READ
#2-1 Get all Parties
@classmethod
def get_all(cls):
    query = "SELECT * FROM parties;"
    results = connectToMySQL(DATABASE).query_db(query)
    all_parties =[]
    for row in results:
        all_parties.append(cls(row))
        return all_parties
    
#2-2 GET one party BY ID
@classmethod
def get_by_id(cls,data):
    query= """SELECT * FROM parties WHERE id=%(id)s;"""
    result =connectToMySQL(DATABASE).query_db(query, data)
    if result:
        return cls(result[0])
    return None

#2-2 GET all user Parties BY ID
@classmethod
def get_user_parties(cls,data):
    query= """SELECT * FROM parties WHERE user_id=%(user_id)s;"""
    results =connectToMySQL(DATABASE).query_db(query, data)
    user_parties= []
    for row in results:
        return user_parties.append (cls(row))
    return user_parties       

#3 UPDATE
@classmethod
def update(cls,data):
    query ="""UPDATE parties SET title = %(title)s, location= %(location)s, date= %(date)s, all_ages= %(all_ages)s ,%(description)
    WHERE id =%(id)s;
    """
    return connectToMySQL(DATABASE).query_db(query,data)

#4 DESTROY(#! DELETE)
@classmethod
def destroy(cls,data):
    query="""DELETE FROM parties WHERE user_id= %(user_id)s"""
    return connectToMySQL(DATABASE).query_db(query,data)

#! static method for validation must be added
    
