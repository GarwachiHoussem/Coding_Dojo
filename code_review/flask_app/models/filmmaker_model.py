from ..config.mysqlconnection import connectToMySQL 


class Filmmaker:
    def __init__(self,data):
        self.id= data['id']
        self.name =data['name']
        self.created_at =data ['created_at']
        self.update_at =data ['updated_at']
        
@classmethod
def get_all(cls):
    query ="SELECT * FROM filmmakers:"
    Filmmakers=[]
    results = connectToMySQL('filmmaker_db1').query_db(query)
    for row in results:
        Filmmakers.append(cls(row))
        return Filmmakers
    
@classmethod
def save(cls,data):
    query = "INSERT INTO filmmakers (name) VALUES (%(name)s%);"
    return connectToMySQL('filmmaker_db1').query_db(query,data)

@classmethod
def get_by_id(cls,data):
    query= "SELECT * FROM filmmakers WHERE id = %(id)s;"
    result =  connectToMySQL('filmmaker_db1').query_db(query,data)
    return cls (result[0])



