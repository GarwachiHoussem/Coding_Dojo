from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Party:
    def init(self,data_dict):
        self.id=data_dict['id']
        self.user_id=data_dict['user_id']
        self.title=data_dict['title']
        self.location=data_dict['location']
        self.date=data_dict['date']
        self.all_ages=data_dict['all_ages']
        self.description=data_dict['description']


    @classmethod
    def create(cls,data):
        query="""INSERT INTO parties (user_id, title, location, date, all_ages, description)
            VALUES (%(user_id)s,%(title)s,%(location)s,%(date)s,%(all_ages)s,%(description)s)"""
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def get_all(cls):
        query = "SELECT *FROM parties;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_parties = []
        for row in results:
            all_parties.append(cls(row))
        return all_parties
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM parties WHERE id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return None
    @classmethod
    def get_user_parties(cls, data):
        query = """SELECT * FROM parties WHERE user_id=%(user_id)s;"""
        results = connectToMySQL(DATABASE).query_db(query, data)
        user_parties = []
        for row in results:
            user_parties.append(cls(row))
        return user_parties
    # 3 update
    @classmethod
    def update(cls, data):
        query = """UPDATE parties set title = %(title)s, location = %(location)s,
                                      date = %(date)s, all_ages = %(all_ages)s, 
                                      description = %(description)s 
                            WHERE id = %(id)s"""
        return connectToMySQL(DATABASE).query_db(query, data)
    # 4 destroy
    @classmethod
    def destroy(cls, data):
        query = """DELETE * FROM parties WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)
    # ! static method for validation 
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['title'])<2:
            is_valid = False
            flash("party Title is required.")
        if len(data['location'])<2:
            is_valid = False
            flash("party Location is required.")
        if len(data['description'])<10:
            is_valid = False
            flash("party Description is required.")
        if len(data['description'])<10:
            is_valid = False
            flash("party Description is required.")
        if data["date"] == "":
            is_valid = False
            flash("Party Date must be provided")
        return is_valid