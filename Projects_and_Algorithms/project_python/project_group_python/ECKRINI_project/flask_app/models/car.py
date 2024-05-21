from datetime import date,datetime
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user

class Car:
    def __init__(self,data):
        self.id=data["id"]
        self.agency_id=data["agency_id"]
        self.model=data["model"]
        self.make=data["make"]
        self.year=data["year"]
        self.price=data["price"]
        self.car_condition=data["car_condition"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.poster=user.User.get_by_id({'id':self.agency_id})
        self.owner=""
        self.is_in=False
        
    @classmethod
    def create(cls ,data) :
        query = """ INSERT INTO cars 
                        (model , year , price , make , car_condition, agency_id)
                        VALUES
                        (%(model)s ,%(year)s , %(price)s , %(make)s, %(car_condition)s , %(agency_id)s );
        """
        
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update_car(cls, data_dict):
        query = """
                UPDATE cars 
                SET model = %(model)s, make = %(make)s,
                            year = %(year)s , price = %(price)s
                WHERE id = %(id)s   ;
                """
        # result = connectToMySQL(DATABASE).query_db(query,data_dict)
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def get_all_cars(cls):
        query="""
            SELECT * FROM cars;
            """
        results=connectToMySQL(DATABASE).query_db(query)
        cars=[]
        for row in results:
            cars.append(cls(row))
        return cars
    
    @classmethod
    def get_car_by_id(cls,data_dict):
        query = """
                    SELECT * FROM cars 
                    JOIN users ON cars.user_id = users.id 
                    WHERE cars.id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        car = cls(result[0])
        car.poster = result[0]['first_name']
        return car
    
    @classmethod
    def destroy_two(cls, data_dict):
        query = """
                DELETE FROM cars WHERE id = %(id)s;
                """
        result= connectToMySQL(DATABASE).query_db(query,data_dict)
        print(result,"*******************")
        return result
    
    @classmethod
    def destroy(cls, data_dict):
        query = """
                DELETE FROM rents WHERE id = %(id)s AND user_id=%(user_id)s;
                """
        result= connectToMySQL(DATABASE).query_db(query,data_dict)
        print(result,"*******************")
        return result
    
    #* ------ Check if the car is rented in that date --------
    @classmethod
    def is_car_rented_d (cls , data_dict):
        query = """
                    SELECT * FROM rents  
                    WHERE car_id = %(car_id)s
                    AND start_time <= %(end_time)s
                    AND end_time >= %(start_time)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        if result:
            return True
        return False
    

    @classmethod
    def create_rented_car(cls ,data) :
        query = """ INSERT INTO rents 
                        (user_id , car_id , status , start_time , end_time)
                        VALUES
                        (%(user_id)s ,%(car_id)s , %(status)s , %(start_time)s, %(end_time)s );
        """
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def get_user_rented_cars (cls , data_dict):
        query = """
                    SELECT * FROM rents  
                    WHERE user_id = %(user_id)s
                """
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return  result
        
    @staticmethod
    def validate(data_dict):
        is_valid = True
        if len(data_dict['model']) < 3:
            flash("name too short!","model")
            is_valid = False
        if len(data_dict['year']) < 3:
            flash("description too short!","description")
            is_valid = False
        if len(data_dict['price']) < 3:
            flash("price too short!","price")
            is_valid = False
        if len(data_dict['make']) < 1:
            flash("date required!","make")
            is_valid = False
        if len(data_dict['car_condition']) < 1:
            flash("date required!","make")
            is_valid = False
        return is_valid